# Day 1 - Prefix Sum

Imagine you are tracking your expenses day by day in an array. A **Prefix Sum array** is simply a new array where each position stores the *running total* (or cumulative sum) up to that point.

Example:

* **Original Array:** `[1, 2, 3, 4]`
* **Prefix Sum Array:** `[1, 3, 6, 10]`
*(Calculated as: `1`, `1+2`, `1+2+3`, `1+2+3+4`)*

By spending a little time building this total array upfront, you can instantly answer questions like "How much did I spend between Day 2 and Day 4?" without running a loop to add them up every single time.

If you have an array representing daily steps: `[1000, 4000, 2000]`

What would the three numbers look like in its **Prefix Sum array**?
*(solution: `[1000,5000,7000]`)*

Imagine a LeetCode interviewer asks you: *"Find the total steps taken between Day 2 and Day 3 inclusive."*

Without the prefix sum, you would have to loop through the original array from index 1 to index 2 and add $4000 + 2000 = 6000$. If the array had a million elements, that loop could take a long time.

But with your **Prefix Sum array** `[1000, 5000, 7000]`, you can get the answer instantly using a simple subtraction formula:

$$\text{Total} = \text{Prefix}[2] - \text{Prefix}[0]$$

$$7000 - 1000 = 6000$$

By subtracting the steps *before* Day 2, you get the answer in a single step ($O(1)$ time) without any loops!

Let's try a quick test of this logic. Using your prefix sum array `[1000, 5000, 7000]`, how would you instantly find the total steps taken from **Day 1 to Day 2** using subtraction?
*(solution: 5000 (Day 2 is sum of day 1 and 2))*

---

### Recommended Prefix Sum Problems

| LeetCode # | Problem Name | Difficulty | Why Solve It? |
| --- | --- | --- | --- |
| **1480** | Running Sum of 1d Array | Easy 🟢 | Direct practice of building the prefix sum array. |
| **303** | Range Sum Query - Immutable | Easy 🟢 | Exactly what we practiced: answering range sum queries in $O(1)$ time. |
| **724** | Find Pivot Index | Easy 🟢 | Uses the total sum and prefix sum to find a balance point. |
| **560** | Subarray Sum Equals K | Medium 🟡 | A classic interview question that combines prefix sums with a Hash Map to find specific targets. |

---

Let's start practicing with the logic behind **LC 303 (Range Sum Query)** or **LC 724 (Find Pivot Index)**.

In **Find Pivot Index**, you need to find a spot in the array where the sum of all numbers to the left equals the sum of all numbers to the right.