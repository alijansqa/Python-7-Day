# match or switch statement

browser = str(input("Enter Browser Name:\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code is executed")
    case "firefox":
        print("FF code is executed")
    case _:
        print("No browser found")
