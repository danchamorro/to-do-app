def main():
    while True:
        user_action = input("Type add, show, edit, complete, delete or quit: ").strip()
        match user_action:
            case "add":
                todo = input("What do you want to add? ").strip()
                with open("todos.txt", "a") as f:
                    f.write(f"{todo}\n")
            case "show":
                with open("todos.txt", "r") as f:
                    todos = f.readlines()
                for i, todo in enumerate(todos):
                    print(f"{i + 1}: {todo.strip()}")
            case "edit":
                with open("todos.txt", "r") as f:
                    todos = f.readlines()
                for i, todo in enumerate(todos):
                    print(f"{i + 1}: {todo.strip()}")
                todo_index = int(input("Which todo do you want to edit? "))
                new_todo = input("What do you want to change it to? ").strip()
                todos[todo_index - 1] = f"{new_todo}\n"
                with open("todos.txt", "w") as f:
                    f.writelines(todos)
            case "complete":
                with open("todos.txt", "r") as f:
                    todos = f.readlines()
                for i, todo in enumerate(todos):
                    print(f"{i + 1}: {todo.strip()}")
                todo_index = int(input("Which todo do you want to complete? "))
                todos[todo_index - 1] = f"X {todos[todo_index - 1]}"
                with open("todos.txt", "w") as f:
                    f.writelines(todos)
            case "delete":
                with open("todos.txt", "r") as f:
                    todos = f.readlines()
                for i, todo in enumerate(todos):
                    print(f"{i + 1}: {todo.strip()}")
                todo_index = int(input("Which todo do you want to delete? "))
                del todos[todo_index - 1]
                with open("todos.txt", "w") as f:
                    f.writelines(todos)
            case "quit":
                break
            case _:
                print("Invalid action")
                

if __name__ == "__main__":
    main()
