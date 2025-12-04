# Search Algorithms Explainer

A command-line learning tool for comparing search algorithms (Linear Search vs Binary Search) with step-by-step execution tracing and history logging.

## 📌 Project Overview

`Search Algorithms Explainer` is a Python CLI application designed to teach search algorithms interactively. It includes:

- Linear Search (O(n)) explanation and trace
- Binary Search (O(log n)) explanation and trace with sorted list view
- Comparison mode (run both algorithms with same input)
- History and results tracking (`results.json`)
- Flexible question sources: pre-defined data, inline list, or manual input

## 🧩 Repository Structure

- `bin/search_algorithms.py` - executable launcher (calls `main()`)
- `search_algorithms/__main__.py` - CLI argument parser and command handler
- `search_algorithms/core/search_algorithms.py` - algorithm implementations
- `search_algorithms/cli/commands.py` - menus and algorithm interaction
- `search_algorithms/cli/menu.py` - menu UI text
- `search_algorithms/utils/data_handler.py` - JSON load/save/history operations
- `search_algorithms/utils/input_handler.py` - input parsing helpers
- `data/questions.json` - pre-set question arrays
- `questions.json` - top-level, likely duplicate/test data

## 🚀 Setup

1. Clone repository:

```bash
git clone <your-repo-url>
cd "Search_Algorithms_Explainer"
```

2. (Optional) create virtual environment and activate:

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux
```

3. Install dependencies:

- No external libraries are required as implemented; pure Python standard library only.  
- If you have a `requirements.txt` (not present), run:

```bash
pip install -r requirements.txt
```

4. Verify Python version (recommended 3.8+):

```bash
python --version
```

## ▶️ Run the Program

### Option 1: Module entrypoint

```bash
python -m search_algorithms
```

### Option 2: CLI script

```bash
python bin/search_algorithms.py
```

### Option 3: as package command (if installed as package)

```bash
search-algorithms
```

## 🛠️ Available Commands

The CLI supports these commands:

- `/start` (default) - Enter interactive learning mode
- `/end` - Exit immediately
- `/history` - Display past run history from `results.json`
- `/clearresult` - Remove the last entry from `results.json`
- `-h`, `--help` - Show help message
- `-v`, `--version` - Show version (currently `1.0.0`)

### Example invocation

```bash
python -m search_algorithms /history
python -m search_algorithms /clearresult
python -m search_algorithms /end
```

## 🧭 Interactive Usage (when `/start`)

1. Select a question identifier:
   - Predefined key from `data/questions.json` (e.g., `Q1`, `Q2`)
   - `manual` to type a custom list
   - Inline list directly (e.g. `1 2 3 4` or `1,2,3`)
2. After list loads, choose:
   - `1` : Linear Search
   - `2` : Binary Search
   - `3` : Compare Linear vs Binary
   - `b` : Back to prior menu
   - `exit` : Quit program
3. Enter target value (integer) when prompted.

## 🧮 Data & Persistence

- `data/questions.json`: Predefined learning questions with arrays.
- `results.json` created automatically to store run history.
- `/history` prints all previous runs.
- `/clearresult` deletes last history record.

## 🔍 Algorithm Details

### Linear Search
- Iterates left to right
- Prints per-step status
- Returns index or `-1`
- Tracks and logs number of steps

### Binary Search
- Sorts a copy of the array, then performs binary search
- Prints sorted list + per-step low/high/mid
- Returns index in sorted list or `-1`
- Logs same metrics as linear

## ❗ Deployment

This is a local CLI app (no web frontend) and currently has no hosted URL.

- If you want a hosted link, deploy as a small web app (Flask/FastAPI) separately.

## 🧪 Common Commands Summary

| Command | Description |
|---|---|
| `python -m search_algorithms` | Start interactive mode (default command `/start`) |
| `python -m search_algorithms /history` | Show saved search history |
| `python -m search_algorithms /clearresult` | Remove last history entry |
| `python -m search_algorithms /end` | Exit with message |
| `python -m search_algorithms -v` | Print version |
| `python -m search_algorithms -h` | Show help |

## 🛠️ Optional Improvements

- Pad invalid input handling with explicit error messages (currently robust but can be extended)
- Add a `--no-history` mode or stats report
- Add unit tests in `tests/` and CI integration
- Add Dockerfile for repeatable setup

## ✨ Notes

- The CLI is educational and intentionally prints trace details to the console.
- `Binary Search` is based on a sorted copy of the list; original index may differ.

---
