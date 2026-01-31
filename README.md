# mini-git 🧩

A lightweight Git-like version control system built from scratch in Python to understand how Git works internally.

---

## 🚀 Overview

**mini-git** is an educational project that reimplements core Git concepts using plain Python and the file system.  
The goal of this project is not to replace Git, but to **deeply understand how modern version control systems work under the hood**.

This project demonstrates low-level design, filesystem-based data management, and core VCS mechanics.

---

## ✨ Features

- Repository initialization (`init`)
- Commit creation with messages
- Branch creation and management
- HEAD pointer handling
- Commit history tracking
- Object storage similar to Git (`obj/`)
- Reference handling (`ref/branches/`)

---

## 📁 Repository Structure

```
.
├── obj/                    # Stores commit objects
├── ref/
│   └── branches/
│       └── main/
│           ├── head        # Current commit pointer
│           └── commitRef   # Commit history
├── crntBranch              # Tracks active branch
├── init.py                 # Initialize repository
├── commit.py                 # Commit operations
├── createcommit.py         # Commit logic
└── createBranch.py         # Branch creation logic
└   getBack.py              # go back to previous commit in that branch 
└   switch-branch.py        # switch between branches 

```

---

## ⚙️ How It Works (High Level)

- A **branch** is just a pointer to a commit
- `head` stores the latest commit of the current branch
- `commitRef` keeps a log of commits for a branch
- Commits are stored as objects inside the `obj/` directory
- Switching branches only changes pointers, not data

This closely follows Git’s internal design philosophy.

---

## 🛠️ Usage

### Initialize repository
```bash
python init.py
```

### Create a commit
```bash
python commit.py -m "your commit message"
```
### Create a branch 
```bash
python createBranch.py "branch Name"
```
### Switch Branch
```bash
python switch-branch.py "branchname"
```

### Go to previous commit in that branch 
```bash
python getBack.py "your commit message"
```
---

## 🎯 Learning Outcomes

- Understanding Git internals
- Filesystem-based system design
- Pointer-based architecture (HEAD & branches)
- Clean Python project structuring
- Command-line tool development

---

## 📌 Why This Project?

I want to personally explore git internals and also bilding something exciting on my own thinking 

---



---

## 👨‍💻 Author

Built by **Raghavendra**  
B.Tech student passionate about systems, backend development, and learning by building.

---



This is an educational project inspired by Git.  

