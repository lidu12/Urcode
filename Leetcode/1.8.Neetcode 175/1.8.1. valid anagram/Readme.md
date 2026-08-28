# LeetCode #242 — Valid Anagram

## Problem

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An **anagram** is a word or string that contains the same characters with the same frequency, but the characters can be in a different order.

### Example 1

```text
Input:
s = "anagram"
t = "nagaram"

Output:
True
```

### Example 2

```text
Input:
s = "rat"
t = "car"

Output:
False
```

---

## Data Structure

**Hash Map / Hash Table**

In Python, we use a **dictionary (`dict`)** to store the frequency of each character.

```python
count_s = {}
count_t = {}
```

The dictionary stores:

```text
Character → Number of occurrences
```

For example:

```text
s = "anagram"

count_s = {
    "a": 3,
    "n": 1,
    "g": 1,
    "r": 1,
    "m": 1
}
```

---

## Algorithm

1. Check whether `s` and `t` have the same length.
2. If their lengths are different, return `False`.
3. Create an empty dictionary `count_s` to count characters in `s`.
4. Create an empty dictionary `count_t` to count characters in `t`.
5. Loop through every character in `s` and increase its count.
6. Loop through every character in `t` and increase its count.
7. Compare `count_s` and `count_t`.
8. If they are equal, return `True`.
9. Otherwise, return `False`.


---

## Complexity

### Time Complexity

```text
O(n)
```

We go through the characters of `s` and `t` once.

### Space Complexity

```text
O(n)
```

We use dictionaries to store the character frequencies.

> Note: If the input is restricted to a fixed character set, such as only 26 lowercase English letters, the auxiliary space can be considered `O(1)` because the number of possible characters is fixed.

---

## Key DSA Concept

```text
Valid Anagram
      ↓
Hash Map / Hash Table
      ↓
Frequency Counting
      ↓
Python Dictionary
```

### Pattern to Remember

When a problem asks:

> "How many times does each item appear?"

Think:

**Hash Map + Frequency Counting**

---

## LeetCode

Problem: **#242 — Valid Anagram**

Difficulty: **Easy**

Data Structure: **Hash Map / Hash Table**

Technique: **Frequency Counting**
