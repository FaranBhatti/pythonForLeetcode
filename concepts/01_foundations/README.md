# 01 — Foundations: Variables, Types, Math, and Conditionals

## 1. Variables and Data Types

Python is dynamically typed — no need to declare types explicitly.

| Type | Example |
|------|---------|
| `str` | `"Alice"` |
| `int` | `25` |
| `float` | `98.6` |
| `bool` | `True` or `False` |
| `None` | equivalent of `null` in other languages |

**Multiple assignment**
```python
x, y, z = 1, 2, 3
```

**Type conversion**
```python
int("42")     # 42
str(25)       # "25"
float("3.14") # 3.14
```

**Checking types**
```python
type(variable)
```

### Gotchas for LeetCode

- **No `x++`** — syntax error in Python. Use `x += 1` to increment.
- **`None` vs `False`** — not the same. When checking for null values (tree nodes, linked list pointers), use `if x is None`.

---

## 2. Math and Numbers

### Basic Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` `-` `*` | Add, Subtract, Multiply | `5 * 2` | `10` |
| `/` | Division — always returns a float | `5 / 2` | `2.5` |
| `//` | Floor division — rounds down | `5 // 2` | `2` |
| `%` | Modulo — remainder | `5 % 2` | `1` |
| `**` | Power | `2 ** 10` | `1024` |

> `//` is essential for finding the midpoint in binary search: `mid = (lo + hi) // 2`

### `math` Module
```python
import math
math.floor(4.9)   # 4
math.ceil(4.1)    # 5
math.sqrt(16)     # 4.0
```

### Infinity
```python
float("inf")   # positive infinity — use as initial min tracker
float("-inf")  # negative infinity — use as initial max tracker
```

### Built-ins
```python
abs(-7)          # 7
min(3, 1, 2)     # 1
max(3, 1, 2)     # 3
```

### Gotchas for LeetCode

- **Negative floor division** — `-7 // 2` gives `-4` (Python floors toward −∞). To truncate toward zero like C++/Java: `int(-7 / 2)` gives `-3`.
- **No overflow** — Python integers grow as large as needed. No need to worry about overflow errors common in C++ or Java.

---

## 3. Conditionals (If-Statements)

Conditionals execute different blocks of logic based on whether a condition is `True` or `False`.

### Basic Syntax
```python
if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")
```

### Logical Operators

Python uses plain English instead of symbols:

| Python | Other languages |
|--------|----------------|
| `and` | `&&` |
| `or` | `\|\|` |
| `not` | `!` |

### Ternary Operator (Inline If)
```python
label = "big" if x > 10 else "small"
```

### Membership Checks
```python
if "apple" in fruits:
    print("found it")
```

### Gotchas for LeetCode

- **Indentation is syntax** — Python uses indentation instead of `{}` to define blocks. Inconsistent spacing will break your code.
- **`elif` not `if`** — use `elif` for multiple conditions. Using separate `if` statements means multiple blocks can execute; `elif` stops after the first match.

---

## Practice

- [practice_profile_card.py](practice_profile_card.py)
- [practice_grade_calculator.py](practice_grade_calculator.py)