# DSA Practice

Personal repository of Data Structures & Algorithms problems, organized by platform and language.

## 📁 Structure

```
dsa-practice/
├── leetcode/
│   ├── python/
│   ├── cpp/
│   └── csharp/
├── hackerrank/
│   ├── python/
│   ├── cpp/
│   └── csharp/
├── codeforces/
│   ├── python/
│   ├── cpp/
│   └── csharp/
└── notes/
    └── complexity-cheatsheet.md
```

- **Top level** = platform (LeetCode, HackerRank, Codeforces, ...). Add more platform folders as needed.
- **Second level** = language (Python, C++, C#).
- Files are named `<problem-id>-<kebab-case-title>.<ext>`, e.g. `0001-two-sum.py`.
- Each solution file starts with a header comment: problem link, difficulty, topic/tags, approach, and time/space complexity.

## ✅ Progress Tracker

| # | Problem | Platform | Difficulty | Topic | Python | C++ | C# |
|---|---------|----------|------------|-------|--------|-----|----|
| 1 | Two Sum | LeetCode | Easy | Array, Hash Map | [✓](leetcode/python/0001-two-sum.py) | [✓](leetcode/cpp/0001-two-sum.cpp) | [✓](leetcode/csharp/0001-two-sum.cs) |

> Update this table as you go. You don't need to solve every problem in all three languages — leave the cell blank or mark it `—` if skipped.

## 🧭 Conventions

- **Numbering**: use the platform's official problem ID where available (LeetCode #, Codeforces problem code, etc.).
- **Difficulty tags**: Easy / Medium / Hard (or platform-specific rating for Codeforces).
- **Commit habit**: commit each solved problem as its own commit — the history doubles as a practice log.
- **Revisit flag**: if a problem needs revisiting, prefix the filename with `REVISIT-` or track it in a GitHub Issue/Project board.

## 📓 Notes

The `notes/` folder holds general concept write-ups (e.g. graph traversal patterns, DP recurrence templates, complexity cheat sheets) that aren't tied to a single problem.

## 🚀 Getting Started

Clone the repo and add solutions as you solve problems:

```bash
git clone https://github.com/<your-username>/dsa-practice.git
cd dsa-practice
```

Running examples:

```bash
# Python
python leetcode/python/0001-two-sum.py

# C++
g++ leetcode/cpp/0001-two-sum.cpp -o two_sum && ./two_sum

# C#
dotnet run --project leetcode/csharp/0001-two-sum.cs   # or use `csc` / an IDE
```
