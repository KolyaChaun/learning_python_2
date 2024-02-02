search_string = input("Enter the string: ")

with open("rockyou.txt", mode="r", encoding="utf-8", errors="ignore") as file:
    lines_found = 0

    for line in file:
        if search_string in line:
            lines_found += 1
    if lines_found > 0:
        print(f"Lines found: {lines_found}")
    else:
        print("The requested string does not exist")
