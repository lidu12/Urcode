# Question: Reverse Between

### 🔢 Leet Code Equivalent:

**Leet Code #92 — Reverse Linked List II**

Write a method `reverse_between(start_index, end_index)` that reverses a portion of a **doubly linked list** in-place.

You are given:

- A doubly linked list with `next` and `prev` pointers
- A `start_index` and `end_index` (inclusive range)

Your task is to **reverse only the nodes between those indices**, keeping the rest of the list unchanged.

**Requirements**:

- Indexing is zero-based.
- Do not modify node values.
- Rearranging must be **in-place** (change only pointers, no new nodes).
- Maintain both `.next` and `.prev` links correctly.
- If the list has fewer than two nodes, or `start_index == end_index`, do nothing.

---

## 💡 Examples

### Example 1:

**Input**:

List: `1 <-> 2 <-> 3 <-> 4 <-> 5`,

`start_index = 1`, `end_index = 3`

**Output**:

`1 <-> 4 <-> 3 <-> 2 <-> 5`

---

### Example 2:

**Input**:

List: `10 <-> 20 <-> 30 <-> 40`,

`start_index = 0`, `end_index = 2`

**Output**:

`30 <-> 20 <-> 10 <-> 40`