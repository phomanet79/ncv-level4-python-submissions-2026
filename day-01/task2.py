athletes = []

name = input("Enter athlete name (or x to finish): ")

while name != "x":
    time = input("Enter time (mm:ss): ")

    if len(time) == 5 and time[2] == ":" and \
       time[0:2].isdigit() and time[3:5].isdigit():

        minutes = int(time[0:2])
        seconds = int(time[3:5])

        if seconds <= 59:
            athletes.append([name, time])
        else:
            print("Invalid time ignored.")
    else:
        print("Invalid time ignored.")

    name = input("Enter athlete name (or x to finish): ")

if len(athletes) == 0:
    print("No valid entries.")
else:
    qualified = 0

    first_time = athletes[0][1]
    winner = athletes[0][0]

    minutes = int(first_time[0:2])
    seconds = int(first_time[3:5])
    lowest_time = minutes * 60 + seconds

    for athlete in athletes:
        name = athlete[0]
        time = athlete[1]

        minutes = int(time[0:2])
        seconds = int(time[3:5])

        total_seconds = minutes * 60 + seconds

        if total_seconds <= 1500:
            qualified = qualified + 1

        if total_seconds < lowest_time:
            lowest_time = total_seconds
            winner = name
            winner_time = time

    print()
    print("--- RACE RESULTS ---")
    print(f"Athletes  : {len(athletes)}")
    print(f"Winner    : {winner}")
    print(f"Time      : {winner_time}")
    print(f"Qualified : {qualified} of {len(athletes)}")
