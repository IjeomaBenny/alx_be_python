Task = input("Enter your task:")
Priority = input("priority(high/medium/low):")
Time_bound = input("(yes/no):")

match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{Task}' is a high priority task. Complete it as soon as possible.")
    case "medium":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a medium priority task that needs to be done today.")
        else:
            print(f"Note: '{Task}' is a medium priority task. Try to get to it soon.")
    case "low":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a low priority task but still needs to be completed today.")
        else:
            print(f"Note: '{Task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Unknown priority level. Please enter high, medium, or low.")