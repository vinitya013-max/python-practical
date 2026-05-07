color = input("Enter color: ")

match color.lower():
    case "red": print("Stop")
    case "yellow": print("Wait")
    case "green": print("Go")
    case _: print("Invalid")