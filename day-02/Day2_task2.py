import random

def generate_minutes():
    return random.randint(30, 180)

def calc_amount(machine_type, minutes):
    machine_types = ["A", "B", "C"]
    initial_cost = [50.00, 62.50, 74.87]
    additional_cost = [30.00, 36.00, 40.50]

    for n in range(len(machine_types)):
        if machine_type == machine_types[n]:
            hours = minutes / 60
            amount = initial_cost[n] + (additional_cost[n] * hours)
            return amount

    print("Invalid machine type")
    return 0

def calc_total_amount(amount):
    vat_amount = amount * 0.14
    total_payable = amount + vat_amount
    return vat_amount, total_payable

def display_summary(payments):
    print("\n--- Daily Summary ---")
    print(f"Number of customers : {len(payments)}")
    print(f"Total payments      : R{sum(payments):.2f}")
    print(f"Average payment     : R{sum(payments) / len(payments):.2f}")
    print(f"Highest payment     : R{max(payments):.2f}")
    print(f"Lowest payment      : R{min(payments):.2f}")

def process_payment():
    payments = []

    num_customers = int(input("How many customers today? "))

    for i in range(num_customers):
        print(f"\nCustomer {i + 1}")
        machine_type = input("Enter machine type (A/B/C) : ").upper()
        minutes = generate_minutes()
        print(f"Minutes used (random) : {minutes}")

        amount = calc_amount(machine_type, minutes)
        vat_amount, total_payable = calc_total_amount(amount)

        print(f"Amount before VAT : R{amount:.2f}")
        print(f"VAT (14%)         : R{vat_amount:.2f}")
        print(f"Total payable     : R{total_payable:.2f}")

        payments.append(total_payable)

    display_summary(payments)

process_payment()