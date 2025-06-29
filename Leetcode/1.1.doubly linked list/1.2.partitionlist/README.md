# Question: Partition List

### 🔢 LeetCode Equivalent:

 **LeetCode #86: Partition List**, 

**Write a method called `partition_list(self, x)`** that rearranges the nodes in a **doubly linked list** so that:

- All nodes with a value **less than `x`** come before all nodes **greater than or equal to `x`**.
- You **must maintain the original relative order** of nodes in both groups.
- The partition must be done **in-place** — you **can’t create new nodes**, but you can use dummy nodes if needed.
- Both `.next` and `.prev` pointers must be updated correctly.
- If the list is empty, nothing should happen.

---

## 📌 Examples

### Example 1

**Input**:

DLL: `3 <-> 8 <-> 5 <-> 10 <-> 2 <-> 1`

Partition value: `x = 5`

**Output**:

`3 <-> 2 <-> 1 <-> 8 <-> 5 <-> 10`

Nodes less than 5: `3, 2, 1`

Nodes >= 5: `8, 5, 10`

---

### Example 2

**Input**:

DLL: `1 <-> 2 <-> 3`

x = 5

**Output**: `1 <-> 2 <-> 3` — No change needed