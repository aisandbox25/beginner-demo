# GenAI Beginner 101: From Zero to Your First Python Demo Using Cursor
# Welcome! This guide walks you through setting up Python, installing Cursor, and running your first GenAI-powered Python demo — even if you're brand new to this space.

---

# 1. Install Python with Homebrew (Mac only, at terminal)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

brew --version
brew install python
```

# After installation, check your Python path and version:

```bash
which python3
python3 --version
```

---

# 2. Create a folder for your project

```bash
mkdir ~/beginner-demo
cd ~/beginner-demo
```

# (You can replace `~/beginner-demo` with any preferred path)*

---

# 3. Download Cursor with 14-day free trial

https://cursor.com/download

---

# 4. After installation, open Cursor and load your project folder (`~/beginner-demo`).

# Follow steps in /beginner-demo/2025-10-04-beginner-101/tutorial-material/beginner-demo-101.pdf

# Create and activate virtual environment
# Why use a Virtual Environment?
# Using a virtual environment helps isolate dependencies for each project and keeps your system clean.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

# Ready to go!

# 5. Try this prompt inside Cursor's chat

# In the right-side chat window in Cursor, paste the following prompt:

```
在/beginner-demo/2025-10-04-beginner-101 中尝试这个demo

写一个 Python 程序，让用户输入一个未来日期（如 2025-12-25），输出离今天还有几天。
```

# You'll see the code appear directly in the editor.
# You can run it at terminal and get an immediate result.
# You’ll also start to understand how the logic works.