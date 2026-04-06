# 02 — Control Flow: Loops

Loops allow you to repeat a block of code. Use `for` loops for iterating over a known range or collection, and `while` loops for repeating until a condition changes.

---

## 1. The `while` Loop

Repeats as long as a condition is `True`.

```python
n = 0
while n < 5:
    print(n)
    n += 1
```

---

## 2. The `for` Loop and `range()`

Most commonly used with `range()` to generate sequences of numbers.

| Expression | Generates |
|------------|-----------|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(2, 6)` | `2, 3, 4, 5` |
| `range(5, 0, -1)` | `5, 4, 3, 2, 1` |

```python
for i in range(5):
    print(i)
```

---

## 3. Iteration Patterns

```python
# Loop a list directly
for name in names:
    print(name)

# Loop with index and value
for i, name in enumerate(names):
    print(i, name)

# Loop two lists together
for a, b in zip(list1, list2):
    print(a, b)
```

---

## 4. Loop Control

- `continue` — skip the rest of the current iteration, move to the next
- `break` — stop the loop entirely

```python
for i in range(10):
    if i == 3:
        continue   # skips 3
    if i == 7:
        break      # stops at 7
    print(i)
```

---

## Gotchas for LeetCode

- **Off-by-one errors** — `range(n)` stops at `n-1`. Common source of bugs in array problems.
- **Modifying while looping** — never add or remove elements from a list while iterating over it. Leads to unpredictable behavior.

---

## Practice

- [practice_fizzbuzz.py](practice_fizzbuzz.py)