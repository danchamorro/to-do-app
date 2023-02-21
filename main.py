def main():
    to_do_list = []
    while True:
        user_action = input("Type add, show, edit or quit: ").strip()
        match user_action:
            case "add":
                to_do_list.append(input("What do you want to add? ").strip())
            case "show":
                for index, item in enumerate(to_do_list, start=1):
                    print(f"{index}. {item}")
            case "quit":
                break
            case "edit":
                index = int(input("Which index do you want to edit? "))
                to_do_list[index - 1] = input("What do you want to change it to? ")
            case _:
                print("Invalid action")


if __name__ == "__main__":
    main()
