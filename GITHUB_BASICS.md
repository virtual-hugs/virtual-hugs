# 💙 GitHub Basics for Virtual Hugs Contributors

Welcome to GitHub! 

If you have never used GitHub before, don't worry. This guide explains the basic GitHub terminology we will use throughout the Virtual Hugs project and how we will use these tools to collaborate as a team.

You do **not** need previous GitHub experience to contribute. Learning how to use GitHub is part of the experience!

---

# 🌎 What is GitHub?

GitHub is a platform that allows developers to store, manage, and collaborate on software projects.

Think of GitHub like a shared workspace where our team can:

- Store website code
- Track tasks and ideas
- Review each other's work
- Collaborate without overwriting each other's changes
- Keep a history of everything created

For Virtual Hugs, GitHub will be used as our main platform for organizing development.

---

# 📁 Repository (Repo)

## What is a repository?

A repository (often called a "repo") is the main folder where a project is stored.

A repository contains:

- Code
- Images and assets
- Documentation
- Project information
- Contribution guidelines

Think of a repository like a Google Drive folder for an entire project, except it is designed specifically for software development.

---

## How we use repositories in Virtual Hugs

The main Virtual Hugs repository will contain:

```
virtual-hugs/

├── frontend/
├── backend/
├── designs/
├── documentation/
├── assets/
├── README.md
├── CONTRIBUTING.md
└── GITHUB_BASICS.md
```

Each folder has a purpose and helps keep the project organized.

---

# 🌿 Branch

## What is a branch?

A branch is a separate copy of the project where you can safely make changes without affecting the main project.

Think of the `main` branch as the official version of the website.

Instead of directly editing it, contributors create their own branch to work on features.

Example:

```
main
 |
 ├── feature/homepage
 |
 ├── feature/journal-page
 |
 └── fix/navigation-bug
```

---

## How we use branches in Virtual Hugs

Contributors should create a new branch whenever they work on something.

Examples:

Frontend developer:

```
feature/homepage-layout
```

Game developer:

```
feature/breathing-game
```

Designer:

```
design/color-palette
```

Bug fixer:

```
fix/mobile-navbar
```

This allows multiple people to work at the same time without interfering with each other's work.

---

# 💾 Commit

## What is a commit?

A commit is a saved checkpoint of your work.

Every time you make a commit, GitHub records:

- What changed
- Who changed it
- When it was changed

Think of a commit like pressing "save" on your progress.

---

## Example

Instead of one giant commit:

```
Updated everything
```

we want smaller, clearer commits:

```
Added homepage navigation bar

Created journal entry component

Fixed mobile layout issue
```

Good commits make it easier for everyone to understand the project history.

---

# 🔄 Push

## What is pushing?

Pushing sends your local changes to GitHub.

Example:

You make changes on your computer:

```
Your computer
      |
      |
      ↓
   GitHub
```

The action of sending your changes to GitHub is called a **push**.

---

# 📥 Pull

## What is pulling?

Pulling downloads the newest changes from GitHub to your computer.

Example:

Another contributor updates the website:

```
GitHub
      |
      |
      ↓
Your computer
```

You pull those updates so your copy of the project is up to date.

---

# 🔀 Pull Request (PR)

## What is a pull request?

A pull request is a request to add your changes into the main project.

Before your work becomes part of the official website, another contributor reviews it.

The process:

```
Create branch
      ↓
Make changes
      ↓
Commit changes
      ↓
Push branch
      ↓
Create Pull Request
      ↓
Review
      ↓
Merge into main
```

---

## How we use Pull Requests in Virtual Hugs

Every major contribution should go through a pull request.

Examples:

- Adding a new webpage
- Creating a mini game
- Adding a new design
- Fixing a bug

Pull requests allow us to:

- Catch mistakes
- Give feedback
- Learn from each other
- Keep the project organized

---

# 🔗 Merge

## What is merging?

Merging combines changes from one branch into another.

Example:

A contributor creates:

```
feature/journal-page
```

After review, it gets merged into:

```
main
```

Now the journal page becomes part of the official website.

---

# 🐛 Issues

## What is an issue?

Issues are tasks, bugs, questions, or ideas tracked in GitHub.

Instead of sending random messages like:

"Someone should fix the homepage"

we create an issue:

```
Title:
Improve homepage mobile responsiveness

Labels:
frontend
bug
good first issue
```

---

## How we use Issues in Virtual Hugs

Issues will be used for:

### Features

Example:

```
Create journaling page
```

### Bugs

Example:

```
Button does not work on mobile
```

### Ideas

Example:

```
Add relaxing music feature
```

### Tasks

Example:

```
Create logo designs
```

---

# 🏷 Labels

## What are labels?

Labels are tags that organize issues.

Examples:

```
frontend
backend
design
testing
beginner-friendly
bug
feature
```

---

## How we use labels in Virtual Hugs

Labels help contributors quickly find tasks related to their interests.

Example:

A UI/UX designer might search:

```
design
```

A beginner developer might search:

```
good first issue
```

A frontend developer might search:

```
frontend
```

---

# 📋 Project Board

## What is a project board?

A project board helps us visualize the progress of tasks.

Our Virtual Hugs board will organize tasks into stages:

```
💡 Ideas
      ↓
📌 Planned
      ↓
🚧 In Progress
      ↓
👀 Review
      ↓
✅ Completed
```

---

## How we use the project board

Before starting a task:

1. Find an issue you want to work on.
2. Assign yourself or request the issue.
3. Move it to "In Progress."
4. Work on the task.
5. Submit a pull request.
6. Move it to "Completed" after approval.

---

# 👥 Contributors

## What is a contributor?

A contributor is anyone who helps improve the project.

Contributions can include:

- Coding
- Designing
- Testing
- Writing content
- Research
- Suggesting ideas

You do not need to write code to contribute!

---

# ⭐ Important GitHub Rules for Virtual Hugs

## 1. Do not directly edit main

Always create a branch first.

---

## 2. Communicate

If you are confused, ask questions!

GitHub is a learning experience.

---

## 3. Make small, clear changes

Small contributions are easier to review and improve.

---

## 4. Give feedback respectfully

Pull requests are for collaboration, not criticism.

Everyone is learning.

---

# 💙 Final Reminder

GitHub may seem confusing at first, but every developer starts somewhere.

The goal of Virtual Hugs is not just to build a website. It is also to help everyone learn how real software teams collaborate.

Don't be afraid to ask questions, experiment, and learn!

Welcome to the team! 💙
