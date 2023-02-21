def add_todo():
    todo = input("What do you want to add? ").strip()
    with open("todos.txt", "a") as f:
        f.write(f"{todo}\n")


def show_todos():
    with open("todos.txt", "r") as f:
        todos = f.readlines()
    for i, todo in enumerate(todos):
        print(f"{i + 1}: {todo.strip()}")


def edit_todo():
    with open("todos.txt", "r") as f:
        todos = f.readlines()
    for i, todo in enumerate(todos):
        print(f"{i + 1}: {todo.strip()}")
    todo_index = int(input("Which todo do you want to edit? "))
    new_todo = input("What do you want to change it to? ").strip()
    todos[todo_index - 1] = f"{new_todo}\n"
    with open("todos.txt", "w") as f:
        f.writelines(todos)


def complete_todo():
    with open("todos.txt", "r") as f:
        todos = f.readlines()
    for i, todo in enumerate(todos):
        print(f"{i + 1}: {todo.strip()}")
    todo_index = int(input("Which todo do you want to complete? "))
    todos[todo_index - 1] = f"X {todos[todo_index - 1]}"
    with open("todos.txt", "w") as f:
        f.writelines(todos)


def delete_todo():
    with open("todos.txt", "r") as f:
        todos = f.readlines()
    for i, todo in enumerate(todos):
        print(f"{i + 1}: {todo.strip()}")
    todo_index = int(input("Which todo do you want to delete? "))
    del todos[todo_index - 1]
    with open("todos.txt", "w") as f:
        f.writelines(todos)


def main():
    while True:
        user_action = input("Type add, show, edit, complete, delete or quit: ").strip()
        if user_action == "add":
            add_todo()
        elif user_action == "show":
            show_todos()
        elif user_action == "edit":
            edit_todo()
        elif user_action == "complete":
            complete_todo()
        elif user_action == "delete":
            delete_todo()
        elif user_action == "quit":
            break
        else:
            print("Invalid action")


if __name__ == "__main__":
    main()
