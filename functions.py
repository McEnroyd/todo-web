FILEPATH = r'D:\Python\practice\to-do-app\to-do-list\todos.txt'

def get_todos(filepath=FILEPATH):
    """ read a text files and get a list of
    to-do items"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """write a to-do items list in text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")
