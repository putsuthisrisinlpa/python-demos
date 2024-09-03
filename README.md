# Shopping List Command-Line Application

This is a simple command-line application that allows you to manage a shopping list. You can add, remove, list items, and save them to a file. The list is automatically saved when you exit the program.

## Features

- **Add Items**: Easily add items to your shopping list.
- **Remove Items**: Remove items from your shopping list.
- **List Items**: Display all items currently on your list.
- **Persistent Storage**: Automatically saves your shopping list to a file on exit.
- **Signal Handling**: Graceful shutdown on receiving `SIGINT` (Ctrl+C), ensuring data is saved.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/shopping-list-cli.git
    ```
2. Navigate to the project directory:
    ```bash
    cd shopping-list-cli
    ```

### Running the Application

To start the application, simply run the Python script:

```bash
python3 shopping_list.py
```

### Commands

Once the application is running, you can use the following commands:

- `add <item>`: Adds `<item>` to your shopping list.
- `remove <item>`: Removes `<item>` from your shopping list.
- `list`: Displays all items currently in your shopping list.
- `help`: Shows the list of available commands.
- `\quit`: Exits the application, saving your list.

### Exiting the Application

You can exit the application by typing `\quit` or by pressing `Ctrl+C`. The shopping list will be saved automatically.

## File Storage

- Your shopping list is stored in `temp/shopping_list.txt` in a comma-separated format.
- The list is read from this file when the application starts and written back to the file when you exit.
