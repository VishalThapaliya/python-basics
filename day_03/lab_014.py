# match - case : the same as switch - case in JavaScript or Java

browser = str(input("Enter your browser name: ").lower())

match browser:
    case "chrome":
        print("Chrome code executed!!!")
    case "firefox":
        print("Firefox code executed!!!")
    case "safari":
        print("Safari code executed!!!")
    case "edge":
        print("Edge code executed!!!")
    case _:
        print("No browser found!!!")