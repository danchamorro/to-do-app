def add_todo():
    todo = input("What do you want to add? ").strip()
    with open("todos.txt", "a") as f:
        f.write(f"{todo}\n")


def show_todos():
    with open("todos.txt", "r") as f:
        todos = f.readlines()
    if not todos:
        print("There are no todos.")
        return
    for i, todo in enumerate(todos):
        print(f"{i + 1}: {todo.strip()}")


def edit_todo():
    with open("todos.txt", "r") as f:
        todos = f.readlines()
    if not todos:
        print("There are no todos to edit.")
        return
    for i, todo in enumerate(todos):
        print(f"{i + 1}: {todo.strip()}")
    try:
        todo_index = int(input("Which todo do you want to edit? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if not 1 <= todo_index <= len(todos):
        print("Invalid todo index.")
        return
    new_todo = input("What do you want to change it to? ").strip()
    todos[todo_index - 1] = f"{new_todo}\n"
    with open("todos.txt", "w") as f:
        f.writelines(todos)


def complete_todo():
    with open("todos.txt", "r") as f:
        todos = f.readlines()
    if not todos:
        print("There are no todos to complete.")
        return
    for i, todo in enumerate(todos):
        print(f"{i + 1}: {todo.strip()}")
    try:
        todo_index = int(input("Which todo do you want to complete? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if not 1 <= todo_index <= len(todos):
        print("Invalid todo index.")
        return
    todos[todo_index - 1] = f"X {todos[todo_index - 1]}"
    with open("todos.txt", "w") as f:
        f.writelines(todos)


def delete_todo():
    with open("todos.txt", "r") as f:
        todos = f.readlines()
    if not todos:
        print("There are no todos to delete.")
        return
    for i, todo in enumerate(todos):
        print(f"{i + 1}: {todo.strip()}")
    try:
        todo_index = int(input("Which todo do you want to delete? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if not 1 <= todo_index <= len(todos):
        print("Invalid todo index.")
        return
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
