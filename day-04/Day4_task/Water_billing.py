#PYTHON PRACTICAL ASSIGNMENT
#Community Water Consumption and Billing Management System


# ============================================================
# SECTION 1: READ LINES FROM INPUT FILE (Q1)
# ============================================================
def read_readings_file(filename):
    """Reads all lines from the specified file and handles missing files."""
    try:
        file = open(filename, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("Error: The file '" + filename + "' was not found in the working folder.")
        return []


# ============================================================
# SECTION 2: VALIDATE & STORE RECORDS IN DICTIONARY (Q2 & Q3)
# ============================================================

def process_records(lines):
    """Splits, cleans, and validates records; logs errors and stores valid records."""
    valid_records = {}
    error_logs = []
    line_num = 0

    for line in lines:
        line_num = line_num + 1
        clean_line = line.strip()

        # Skip empty lines
        if clean_line == "":
            continue

        # Skip header row if present
        if line_num == 1 and clean_line.lower().startswith("meternumber"):
            continue

        parts = clean_line.split(",")

        # Check for exact number of fields
        if len(parts) != 5:
            error_logs.append("Line " + str(line_num) + " [" + clean_line + "] -> Rejected: Missing or extra fields.")
            continue

        meter_no = parts[0].strip()
        name = parts[1].strip()
        prev_str = parts[2].strip()
        curr_str = parts[3].strip()
        area = parts[4].strip()

        # Check for empty fields
        if meter_no == "" or name == "" or prev_str == "" or curr_str == "" or area == "":
            error_logs.append("Line " + str(line_num) + " [" + clean_line + "] -> Rejected: One or more empty fields.")
            continue

        # Check for duplicate meter numbers
        if meter_no in valid_records:
            error_logs.append("Line " + str(line_num) + " [" + clean_line + "] -> Rejected: Duplicate meter number (" + meter_no + ").")
            continue

        # Check for numeric readings
        try:
            prev_reading = float(prev_str)
            curr_reading = float(curr_str)
        except ValueError:
            error_logs.append("Line " + str(line_num) + " [" + clean_line + "] -> Rejected: Non-numeric meter reading.")
            continue

        # Check for negative readings
        if prev_reading < 0 or curr_reading < 0:
            error_logs.append("Line " + str(line_num) + " [" + clean_line + "] -> Rejected: Negative meter reading.")
            continue

        # Check for current reading below previous reading
        if curr_reading < prev_reading:
            error_logs.append("Line " + str(line_num) + " [" + clean_line + "] -> Rejected: Current reading is below previous reading.")
            continue

        # Store valid record in dictionary
        valid_records[meter_no] = {
            "meter_no": meter_no,
            "name": name,
            "previous": prev_reading,
            "current": curr_reading,
            "area": area
        }

    return valid_records, error_logs


# ============================================================
# SECTION 3: CONSUMPTION, BILLING & CLASSIFICATION (Q4, Q5, Q6)
# ============================================================
def calculate_bill(consumption):
    """Calculates progressive water bill across the three tariff bands."""
    if consumption <= 6:
        bill = 0.0
    elif consumption <= 20:
        bill = (consumption - 6) * 8.50
    else:
        bill = (14 * 8.50) + ((consumption - 20) * 12.00)
    return bill


def classify_consumption(consumption):
    """Classifies consumption as LOW, MODERATE, or HIGH."""
    if consumption <= 20:
        return "LOW"
    elif consumption <= 50:
        return "MODERATE"
    else:
        return "HIGH"


def apply_billing_and_classification(valid_records):
    """Updates each valid household record with consumption, bill, and category."""
    for meter_no in valid_records:
        record = valid_records[meter_no]
        consumption = record["current"] - record["previous"]
        bill = calculate_bill(consumption)
        category = classify_consumption(consumption)

        record["consumption"] = consumption
        record["bill"] = bill
        record["category"] = category


# ============================================================
# SECTION 4: MANUAL RANKING FOR TOP 5 CONSUMERS (Q7)
# ============================================================
def get_top_five_consumers(valid_records):
    """Manually ranks households by highest consumption without using sorted() or max()."""
    records_list = []
    for meter_no in valid_records:
        records_list.append(valid_records[meter_no])

    # Manual selection sort (descending order by consumption)
    i = 0
    while i < len(records_list):
        largest_idx = i
        j = i + 1
        while j < len(records_list):
            if records_list[j]["consumption"] > records_list[largest_idx]["consumption"]:
                largest_idx = j
            j = j + 1

        # Swap elements
        temp = records_list[i]
        records_list[i] = records_list[largest_idx]
        records_list[largest_idx] = temp
        i = i + 1

    # Extract up to the top 5 records manually
    top_five = []
    k = 0
    while k < 5 and k < len(records_list):
        top_five.append(records_list[k])
        k = k + 1

    return top_five


# ============================================================
# SECTION 5: WRITE REPORTS AND DISPLAY TOTALS (Q8)
# ============================================================
def write_outputs(valid_records, error_logs, top_five):
    """Writes billing_report.txt and errors.log, and prints totals to console."""
    # Write errors.log
    err_file = open("errors.log", "w", encoding="utf-8")
    err_file.write("WATER BILLING ERROR LOG\n")
    err_file.write("=" * 60 + "\n")
    if len(error_logs) == 0:
        err_file.write("No errors found.\n")
    else:
        for err in error_logs:
            err_file.write(err + "\n")
    err_file.close()

    # Manual aggregation for summary totals
    total_consumption = 0.0
    total_revenue = 0.0
    low_count = 0
    mod_count = 0
    high_count = 0

    for meter_no in valid_records:
        rec = valid_records[meter_no]
        total_consumption = total_consumption + rec["consumption"]
        total_revenue = total_revenue + rec["bill"]

        if rec["category"] == "LOW":
            low_count = low_count + 1
        elif rec["category"] == "MODERATE":
            mod_count = mod_count + 1
        else:
            high_count = high_count + 1

    # Write billing_report.txt
    rep_file = open("billing_report.txt", "w", encoding="utf-8")
    rep_file.write("COMMUNITY WATER CONSUMPTION AND BILLING REPORT\n")
    rep_file.write("=" * 75 + "\n\n")

    rep_file.write("1. HOUSEHOLD BILLING DETAILS\n")
    rep_file.write("-" * 75 + "\n")
    rep_file.write(f"{'Meter':<8} {'Household Name':<22} {'Area':<16} {'Usage(kL)':<10} {'Category':<10} {'Bill(R)'}\n")
    rep_file.write("-" * 75 + "\n")

    for meter_no in valid_records:
        rec = valid_records[meter_no]
        rep_file.write(
            f"{rec['meter_no']:<8} {rec['name']:<22} {rec['area']:<16} "
            f"{rec['consumption']:<10.1f} {rec['category']:<10} R{rec['bill']:.2f}\n"
        )

    rep_file.write("\n2. TOP FIVE HIGHEST-CONSUMING HOUSEHOLDS\n")
    rep_file.write("-" * 75 + "\n")
    rank = 1
    for rec in top_five:
        rep_file.write(
            f"Rank {rank}: {rec['meter_no']} - {rec['name']} ({rec['area']}) | "
            f"Usage: {rec['consumption']:.1f} kL | Bill: R{rec['bill']:.2f}\n"
        )
        rank = rank + 1

    rep_file.write("\n3. SUMMARY STATISTICS\n")
    rep_file.write("-" * 75 + "\n")
    rep_file.write("Total Valid Households   : " + str(len(valid_records)) + "\n")
    rep_file.write("Total Rejected Records   : " + str(len(error_logs)) + "\n")
    rep_file.write(f"Total Water Consumed     : {total_consumption:.1f} kL\n")
    rep_file.write(f"Total Billed Revenue     : R{total_revenue:.2f}\n")
    rep_file.write("LOW Consumption (0-20)   : " + str(low_count) + "\n")
    rep_file.write("MODERATE (>20-50)        : " + str(mod_count) + "\n")
    rep_file.write("HIGH (>50)               : " + str(high_count) + "\n")
    rep_file.close()

    # Display console summary
    print("Processing complete.")
    print("Accepted records:", len(valid_records))
    print("Rejected records:", len(error_logs))
    print("Reports saved to 'billing_report.txt' and 'errors.log'.")


# ============================================================
# SECTION 6: MAIN PROGRAM EXECUTION
# ============================================================
def main():
    lines = read_readings_file("water_readings.txt")
    if len(lines) > 0:
        valid_records, error_logs = process_records(lines)
        apply_billing_and_classification(valid_records)
        top_five = get_top_five_consumers(valid_records)
        write_outputs(valid_records, error_logs, top_five)


main()