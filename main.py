def main():
    to_do_list = []
    while True:
        user_action = input("Type add or show or quit: ").strip()
        match user_action:
            case "add":
                to_do_list.append(input("What do you want to add? ").strip())
            case "show":
                print(to_do_list)
            case "quit":
                break
            case _:
                print("Invalid action")


if __name__ == "__main__":
    main()
