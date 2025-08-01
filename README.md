# 🔐 FactVerse – Hacker-Style Fact Generator

**Made by w7nx_z**

A terminal-based hacker-themed random fact generator with category selection, typing animations, and terminal aesthetics.

## 🚀 Features

- 🎯 **Hacker Terminal UI**: Dark theme with green/cyan text styling
- 🎬 **Startup Animations**: ASCII banner, progress bars, and typing effects
- 📚 **5 Fact Categories**: Hacking Intel, Fun Bytes, Attitude Logs, Lazy Logs, Motivation Doses
- 🎲 **Random Selection**: Different facts each session
- 💾 **Save to File**: Export facts to `saved_facts.txt`
- 🖥️ **Terminal Animations**: Typing effects and loading sequences
- � **Hacker Exit Sequence**: Dramatic logout with encryption simulation
- 📱 **Termux Compatible**: Perfect for Android hacking environments

## 📁 Project Structure

```
factverse/
├── main.py                ← Core hacker-style interface
├── facts.json             ← Database of categorized facts
├── start.sh               ← Launcher with colored terminal output
├── assets/
│   └── banner.txt         ← ASCII art banner
├── saved_facts.txt        ← Auto-generated saved facts (optional)
└── README.md              ← This documentation
```

## 🎮 Hacker UI Experience

### 🔐 Startup Sequence
```
🟢 Initializing... ⏳
🔐 Launching: FactVerse – Category-Based Fact Generator
👨‍💻 Creator: w7nx_z
🧬 Terminal Interface Active...

████████████████████████████████████
█───█────█────█────█───█────█──────█
█ F A C T V E R S E   T O O L █
█───█────█────█────█───█────█──────█
████████████████████████████████████

[ Loading tool... ] ████████████████████ 100%
```

### 💾 Category Dashboard
```
💾 Choose a Category to Extract Random Data:

[1] 🧠 Hacking Intel
[2] � Fun Bytes
[3] 😎 Attitude Logs
[4] � Lazy Logs
[5] � Motivation Doses
[6] 🛑 Exit Terminal

📥 Enter your command code: _
```

### 🧠 Terminal Output Style
```
[✔️] Access Granted.
[🧠] Fetching random entry from: Hacking Intel...

📄 Terminal Output:
>> "Most black-hat hackers start learning before the age of 16."

------------------------------------------------------------
🔁 Actions:
[1] Get Another  [2] Change Category  [3] Exit Tool
💾 Save this fact to `saved_facts.txt`? [Y/n]: _
```

## �️ Installation & Usage

in termux first install 
1) pip install pandas
2) pip install openai

### Quick Start (Hacker Mode)
```bash
cd factverse
bash start.sh
```

### Direct Python Launch
```bash
cd factverse
python main.py
```

### PowerShell (Windows)
```powershell
cd factverse
python main.py
```

## 🎭 Special Features

### 💾 Auto-Save Function
- Facts can be saved to `saved_facts.txt`
- Timestamped entries for session tracking
- Persistent fact collection across sessions

### 🎬 Terminal Animations
- **Typing effects**: Facts appear character by character
- **Progress bars**: Loading sequences with visual feedback
- **Startup sequence**: Dramatic initialization process
- **Exit sequence**: Hacker-style logout with encryption simulation

### 🔒 Hacker Logout Sequence
```
📴 Disconnecting from FactVerse Terminal...
💾 Saving session data...
🔒 Encrypting your activity logs...
🔁 Terminating session variables...

👨‍💻 Agent: w7nx_z
🟢 Status: Safe Disconnect

[████████████████████████████████████████] 100%
✅ Logout successful.

📁 Your saved facts are in: saved_facts.txt
🕶️ Stay anonymous, stay curious.

👋 Goodbye, hacker.
```

## 🔧 Customization

### Adding New Facts
Edit `facts.json` and add facts to any category:

```json
{
  "category_name": [
    "Your new fact here",
    "Another interesting fact"
  ]
}
```

### Adding New Categories
1. Update `facts.json` with your new category
2. Modify the `categories` dictionary in `main.py`
3. Update the menu display in `show_menu()` method

## 🎯 Why FactVerse?

- ✅ **Educational**: Learn interesting facts across different topics
- ✅ **Safe**: No network access, no data collection
- ✅ **Portable**: Runs anywhere Python is available
- ✅ **Lightweight**: Minimal resource usage
- ✅ **Expandable**: Easy to add more facts and categories

## 📱 Perfect for Termux Users

This tool is specifically designed to work great in Termux:
- No external dependencies required
- Terminal-based interface
- Offline functionality
- Quick startup and execution

## 🐛 Troubleshooting

### Python not found error
- Make sure Python is installed: `python --version`
- Try using `python3` instead of `python`

### JSON format error
- Verify `facts.json` has valid JSON syntax
- Use a JSON validator if needed

### Permission denied (Linux/Termux)
```bash
chmod +x start.sh
```

## 📄 License

This project is open source. Feel free to modify and distribute.

## 👨‍💻 Creator

**w7nx_z** - Original concept and implementation

---

*Enjoy exploring random facts with FactVerse! 🎉*
