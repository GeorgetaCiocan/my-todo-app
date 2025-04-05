FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of t-do items.
    :param filepath: the path and file name where the to-do items are stored
    :return: the list of to-do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file.
    :param todos_arg: list of to-dos
    :param filepath: the path and name of the file
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
