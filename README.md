# Python for LeetCode

This repository documents my journey learning Python specifically for technical interviews and LeetCode problems. The goal is to master the language's core syntax and data structures before applying them to algorithmic challenges.

---

## Study Roadmap

Topics are prioritized by frequency and importance in coding interviews:

1. **Foundations** — Variables, basic math, and conditional if-statements
2. **Control Flow** — `for` and `while` loops
3. **Basic Data Structures** — Arrays (lists), strings, and tuples
4. **Advanced Data Structures**
   - HashSets & HashMaps — O(1) lookups
   - Queues & Heaps — BFS and priority-based problems
5. **Code Organization** — Functions and classes for object-oriented design

---

## Repository Structure

```
pythonForLeetcode/
├── concepts/               # Notes and practice snippets per topic
│   ├── 01_foundations/
│   ├── 02_control_flow/
│   ├── 03_basic_data_structures/
│   └── 04_advanced_data_structures/
└── leetcode/               # LeetCode solutions (after finishing foundations)
```

---

## Running Python in This Repo

### Prerequisites

- Python 3.10+ recommended — check with `python3 --version`
- No external dependencies required for concepts; pure stdlib throughout

### Run any file

```bash
python3 concepts/01_foundations/variables.py
```

### Interactive exploration (REPL)

```bash
python3
```

Useful for quickly testing snippets from the concept notes.

### Run with output visible (one-liner)

```bash
python3 -c "print('hello')"
```

### Checking your solution against expected output

```bash
python3 leetcode/two_sum.py
```

Each solution file includes a `if __name__ == "__main__":` block with sample test cases you can run directly.

---

## Key Resources

- [Python 3 Tutorial](https://docs.python.org/3/tutorial/) — tour of syntax and features
- [Library Reference](https://docs.python.org/3/library/) — standard library and built-ins
- [Language Reference](https://docs.python.org/3/reference/) — detailed syntax and language elements
- [Python Cheat Sheet](https://www.pythoncheatsheet.org/) — quick reference for data structures and algorithms
