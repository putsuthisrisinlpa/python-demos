import signal
import sys

data_file = "temp/shopping_list.txt"
items = []
isItemsDirty = False


def readFromFile():
    """ Read items from the file.
    If the file does not exist no data will be read.
    It expected the item list to be store in a comma separated format."""

    try:
        file = open(data_file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print("An error occurred while reading the file", e)
    else:
        with file:
            content = file.read()
            file.close()
            if content == "":
                return []
            return content.split(",")


def writeToFile(items):
    """ Write items to the file.
    It writes the items to the file in a comma separated format."""

    file = open(data_file, "w")
    encodedItems = ",".join(items)
    file.write(encodedItems)
    file.close()


def on_exit():
    if isItemsDirty:
        writeToFile(items)
    print("Goodbye!")
    sys.exit(0)


def on_signal(signum, frame):
    on_exit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, on_signal)
    items = readFromFile()
    usage = """Commands:
    - add <item>: add item to list
    - remove <item>: remove item from list
    - list: return items
    - help: show usage
    - \\quit: exit\n"""
    print(usage)

    while True:
        input_str = input("$ ")

        if input_str == "\\quit":
            break
        elif input_str == "help":
            print(usage)
        elif input_str.startswith("add "):
            item = input_str.replace("add ", "")
            items.append(item)
            isItemsDirty = True
        elif input_str.startswith("remove "):
            item = input_str.replace("remove ", "")
            if item in items:
                items.remove(item)
                isItemsDirty = True
        elif input_str == "list":
            for item in items:
                print("- ", item)
        else:
            print("Invalid command")

    on_exit()
