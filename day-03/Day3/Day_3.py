data = [65,72,48,90,55,72,48,72]
#=====QUESTION 1===================
print("===============QUESTION 1===================")

learners = {
    "2024001": {"name": "Thandi", "marks": [65, 72, 58]},
    "2024002": {"name": "Sipho", "marks": [48, 90, 55]},
    "2024003": {"name": "Lerato", "marks": [81, 39, 77]},
    "2024004": {"name": "Dumisani", "marks": [72, 72, 48]},
    "2024005": {"name": "Naledi", "marks": [90, 95, 72]}
}

print("=== 1.1 List ===")
# 1.1 Create and print a list of all marks for learner 2024001
thandi_marks = learners["2024001"]["marks"]

print("All marks for 2024001 (Thandi):", thandi_marks)
print("First mark:", thandi_marks[0])
print("Last mark:", thandi_marks[-1])
print("First two marks (slice):", thandi_marks[0:2])

print("\n=== 1.2 Tuple ===")
# 1.2 Tuple for fixed classroom coordinate (row, seat)

classroom_coordinate = (3, 12)

# Unpack the tuple
row, seat = classroom_coordinate

print("Classroom coordinate:", classroom_coordinate)
print("Row:", row)
print("Seat:", seat)

print("\n=== 1.3 Set ===")
# 1.3 Set of module codes with at least one duplicate
module_codes = {"LOL4", "LO4", "MATH4", "LOL4", "COMP4"}

print("Module codes set:", module_codes)
print("Number of unique codes:", len(module_codes))
print("Is LOL4 in the set?", "LOL4" in module_codes)
print("Is ENG4 in the set?", "ENG4" in module_codes)

print("\n=== 1.4 Explanation in comments ===")
# 1.4 Why dictionary + list suits this scenario:
# 1. Dictionary keyed by student number is good because each student
#    number is UNIQUE, so we can find a learner instantly without searching.
#    Example: learners["2024001"] gives Thandi directly.
# 2. A list of marks inside each record is good because:
#    - A learner has MANY marks, in ORDER (Test 1, Test 2, Test 3)
#    - Marks can CHANGE, be ADDED or UPDATED, and a list is mutable.
#    - We can use indexing, slicing, sum() and len() on a list easily.
# 3. Together they model the real world: One student number -> One learner -> Many ordered marks.
def is_valid_number(text):
    return text.isdigit() and len(text) == 7

def is_valid_mark(text):
    return text.isdigit() and int(text) <= 100
def add_learner(learners, number, name):
    if number in learners:
        return False
    learners[number] = {"name": name, "marks": []}
    return True

def add_mark(learners, number, mark):
    if number not in learners:
        return False
    learners[number]["marks"].append(mark)
    return True

def delete_learner(learners, number):
    if number not in learners:
        return False
    del learners[number]
    return True

def find_by_name(learners, text):
    matches = []
    for number in learners:
        if text.lower() in learners[number]["name"].lower():
            matches.append(number)
    return matches

def rename_learner(learners, number, new_name):
    if number not in learners:
        return False
    learners[number]["name"] = new_name
    return True

def average_of(values):
    total = 0
    for v in values:
        total = total + v
    return total / len(values)

def learner_average(learners, number):
    marks = learners[number]["marks"]
    if len(marks) == 0:
        return None
    return average_of(marks)
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def find_all(values, target):
    positions = []
    for i in range(len(values)):
        if values[i] == target:
            positions.append(i)
    return positions

def count_of(values, target):
    count = 0
    for v in values:
        if v == target:
            count = count + 1
    return count

def mode_of(values):
    counts = {}
    for v in values:
        if v in counts:
            counts[v] = counts[v] + 1
        else:
            counts[v] = 1
    best = 0
    for v in counts:
        if counts[v] > best:
            best = counts[v]
    modes = []
    for v in counts:
        if counts[v] == best:
            modes.append(v)
    return modes
def bubble_sort(values):
    items = values[:]
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

def selection_sort(values):
    items = values[:]
    for i in range(len(items) - 1):
        smallest = i
        for j in range(i + 1, len(items)):
            if items[j] < items[smallest]:
                smallest = j
        items[i], items[smallest] = items[smallest], items[i]
    return items
def print_ranking(learners):
    rows = ranking(learners)
    if len(rows) == 0:
        print("No marks captured yet.")
        return
    print("Rank  Number    Name          Average")
    for position in range(len(rows)):
        avg = rows[position][0]
        number = rows[position][1]
        name = learners[number]["name"]
        print(f"{position + 1:<6}{number:<10}{name:<14}{avg:>6.1f}")
        


def show_menu():
    print()
    print("1. Add learner")
    print("2. Add mark")
    print("3. Rename learner")
    print("4. Delete learner")
    print("5. Find by name")
    print("6. Show ranking")
    print("7. Exit")

def ask_number():
    return input("Student number (7 digits): ")
def ranking(learners):
    rows = []
    for number in learners:
        avg = learner_average(learners, number)
        if avg is not None:
            rows.append((avg, number))
    n = len(rows)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if rows[j][0] < rows[j + 1][0]:
                rows[j], rows[j + 1] = rows[j + 1], rows[j]
    return rows
def total_of(values):
    total = 0
    for v in values:
        total = total + v
    return total

def mean_of(values):
    return total_of(values)/len(values)

def max_of(values):
    best = values[0]
    for v in values:
        if v > best:
            best = v
    return best

def min_of(values):
    lowest = values[0]
    for v in values:
        if v < lowest:
            lowest = v
    return lowest
def range_of(values):
   return max_of(values) - min_of(values)
 

def above_mean(values):
   
   count = 0
   for v in values:
      if v > mean_of(values) :
        count = count + 1
   return count        

                
      
print("====================Question 2===================")                
print("Total  : ", total_of(data))
print("Mean   : ", mean_of(data))
print(f'Highest and Lowest:  ({max_of(data)},{min_of(data)})')
print("Total  :", total_of(data))
print("Above Mean : ", above_mean(data))
print("range :", range_of(data))

print("====================Question 3===================")
print("First 72 at:", find_first(data, 72))
print("All 72 at  :", find_all(data, 72))
print("Mode   :", mode_of(data))
print("Count of 72:", count_of(data, 72))


print("====================Question 4===================")
print(f'Bubble Sort : {bubble_sort(data)}')
print(f'Selection Sort : {selection_sort(data)}')
print(f'Original List : {data}')
print("They are both sorted the same,Bubble does many adjacent swaps and selection does one big swap per pass")
  
def print_ranking(learners):
    learners = {
    "2024001": {"name": "Thandi", "marks": [65, 72, 58]},
    "2024002": {"name": "Sipho", "marks": [48, 90, 55]},
    "2024003": {"name": "Lerato", "marks": [81, 39, 77]},
    "2024004": {"name": "Dumisani", "marks": [72, 72, 48]},
    "2024005": {"name": "Naledi", "marks": [90, 95, 72]}
}

    rows = ranking(learners)
    if len(rows) == 0:
        print("No marks captured yet.")
        return
    print("Rank  Number    Name          Average")
    for position in range(len(rows)):
        avg = rows[position][0]
        number = rows[position][1]
        name = learners[number]["name"]
        print(f"{position + 1:<6}{number:<10}{name:<14}{avg:>6.1f}")

def update_learner():

    student_no = input("Student Number: ")

    if student_no not in learners:
        print("Learner not found.")
        return

    print("1. Change Name")
    print("2. Add Mark")

    choice = input("Choice: ")

    if choice == "1":

        new_name = input("New name: ")
        learners[student_no]["name"] = new_name

    elif choice == "2":

        mark = int(input("New mark: "))

        if 0 <= mark <= 100:
            learners[student_no]["marks"].append(mark)

def main():
    learners = {}
    choice = ""
    while choice != "7":
        show_menu()
        choice = input("Choice: ")
        if choice == "1":
            number = ask_number()
            name = input("Name: ")
            update_learner()
            if not is_valid_number(number) or name == "":
                print("Invalid number or name.")
            elif add_learner(learners, number, name):
                print("Added.")
            else:
                print("That student number already exists.")
        elif choice == "2":
            number = ask_number()
            text = input("Mark (0-100): ")
            if not is_valid_mark(text):
                print("Invalid mark.")
            elif add_mark(learners, number, int(text)):
                print("Mark added.")
            else:
                print("No such learner.")
        elif choice == "3":
            number = ask_number()
            if rename_learner(learners, number, input("New name: ")):
                print("Renamed.")
            else:
                print("No such learner.")
        elif choice == "4":
            if delete_learner(learners, ask_number()):
                print("Deleted.")
            else:
                print("No such learner.")
        elif choice == "5":
            found = find_by_name(learners, input("Name contains: "))
            if len(found) == 0:
                print("No match.")
            for number in found:
                print(number, learners[number]["name"], learners[number]["marks"])
        elif choice == "6":
            print_ranking(learners)
        elif choice == "7":
            print("Goodbye.")
        else:
            print("Invalid choice. Enter 1 to 7.")
        update_learner()

main()

