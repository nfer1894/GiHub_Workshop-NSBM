# Task Manager CLI 🗒️

A simple command-line task manager built with Python.  
Used as a **hands-on project** during the _From Code to Collaboration_ Git & GitHub workshop.

---

## Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/[instructor]/task-manager
cd task-manager
```

### 2. Run the app

```bash
python main.py
```

No packages to install — this project uses Python's built-in libraries only.

---

## How to Use

| Command           | What it does        |
| ----------------- | ------------------- |
| `list`            | Show all your tasks |
| `add <task name>` | Add a new task      |
| `done <id>`       | Mark a task as done |
| `remove <id>`     | Remove a task       |
| `help`            | Show all commands   |
| `quit`            | Exit the app        |

### Example session

```
Enter command: add Buy groceries
Task added: 'Buy groceries'

Enter command: add Submit assignment
Task added: 'Submit assignment'

Enter command: list

--- Your Tasks ---
  [1] ⬜  Buy groceries
  [2] ⬜  Submit assignment

Enter command: done 1
Task 1 marked as done!

Enter command: list

--- Your Tasks ---
  [1] ✅  Buy groceries
  [2] ⬜  Submit assignment
```

---

## Project Structure

```
task-manager/
├── main.py          # Entry point — run this file
├── tasks.py         # Core task logic (add, list, complete, remove)
├── storage.py       # Saves and loads tasks using a JSON file
├── requirements.txt # No external packages needed
└── README.md        # You're reading this!
```

---

## Workshop Activity

Once the app is running, your task is to:

1. **Personalise the welcome message** in `main.py` — change `WELCOME_MESSAGE`
2. **Add a confirmation message** in `tasks.py` — edit the `add_task` function
3. **Commit your changes** with Git
4. **Push to GitHub** and check the commit history

```bash
git status
git add .
git commit -m "Personalise welcome message and improve add_task output"
git push origin main
```

---

## Built With

- Python 3.7+
- `json` module (standard library)
- `os` module (standard library)
