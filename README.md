# A basic GIT tutorial

This is a dummy repository created for educational purposes. It demonstrates a basic project structure and organization. This tutorial demonstrates how to perform basic Git operations such as cloning a repository, checking the status, creating and switching branches, and pushing changes to a remote repository.

## Repository Structure
```bash
.
├── README.md
├── docs
│ └── example_docs
├── examples
│ └── example1
├── scripts
│ └── script1.py
├── data
│ └── sample_data
└── tests
└── test_script
```

## Directories

### docs

Contains project documentation.

- `example_docs`: Example documentation files.

### examples

Includes example code or usage scenarios.

- `example1`: First example.

### scripts

Stores utility scripts and main project code.

- `script1.py`: An example Python script.

### data

Houses data files used in the project.

- `sample_data`: Example data for testing or demonstration.

### tests

Contains test files and test suites.

- `test_script.py`: Script for running tests.

## Getting Started

## Create and Navigate to a Directory on your local computer

```bash
$ mkdir Git_Tutorial
$ cd Git_Tutorial
```

## Clone the repository
```bash
$ git clone https://github.com/omidvarnia/git_tutorial
Cloning into 'git_tutorial'...
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 23 (delta 4), reused 11 (delta 0), pack-reused 0
Receiving objects: 100% (23/23), 6.24 KiB | 1.56 MiB/s, done.
Resolving deltas: 100% (4/4), done.
```

## View Repository Contents
```bash
$ cd git_tutorial
$ tree
.
├── README.md
├── docs
│   └── example_docs
├── examples
│   └── example1
├── scripts
│   └── script1.py
├── data
│   └── sample_data
└── tests
    └── test_script

5 directories, 6 files
```

## Check Repository Status
```bash
$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main

$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## Add and Commit a File
```bash
$ touch new_file.txt
$ git add .
$ git commit -m "Added a new file for demonstration purposes."
[main 6446be7] Added a new file for demonstration purposes.
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 new_file.txt
```

## Push Changes to Remote
```bash
$ git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 312 bytes | 312.00 KiB/s, done.
To https://github.com/omidvarnia/git_tutorial
   952e06a..6446be7  main -> main
```

## Delete and Commit File Changes
```bash
$ rm -f new_file.txt
$ git add .
$ git commit -m "Removed the new file."
[main 6c600dc] Removed the new file.
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 new_file.txt
```

## Create and Switch Branches
```bash
$ git branch feature_branch
$ git checkout feature_branch
Switched to branch 'feature_branch'

$ touch additional_file.txt
$ git add .
$ git commit -m "Created a new branch and added a new file."
[feature_branch a30118d] Created a new branch and added a new file.
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 additional_file.txt

$ git push origin feature_branch
To https://github.com/omidvarnia/git_tutorial
 * [new branch]      feature_branch -> feature_branch
```

## Return to Main Branch
```bash
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

## Merge Branches
Switch to the branch you want to merge into (e.g., main).
```bash
$ git checkout main
```
Merge another branch into it (e.g., feature_branch).
```bash
$ git merge feature_branch
```

## Resolve Merge Conflicts
Open conflicting files and resolve conflicts manually. After resolving, add and commit changes.
```bash
$ git add .
$ git commit -m "Resolved merge conflicts."
```

## Revert a Commit
```bash
$ git revert HEAD
```

## Reset to a Previous Commit
Soft reset (preserves changes).
```bash
$ git reset --soft commit_hash
```
Hard reset (discards changes)—be careful!
```bash
$ git reset --hard commit_hash
```
