# 🚀 FactVerse Setup & AI Integration Guide

## 📁 Complete File Structure
```
factverse/
├── factverse_ai.py       ← Main AI-enhanced application
├── main_simple.py        ← Simplified version (no AI)
├── fact_ai_generator.py  ← AI fact generation module
├── facts.json            ← Local fact database
├── start.sh              ← Bash launcher script
├── saved_facts.txt       ← Auto-generated saved facts
├── assets/
│   └── banner.txt         ← ASCII art banner
├── README.md              ← Documentation
└── SETUP.md               ← This file
```

## 🛠️ Quick Start (No AI)

### Basic Installation
```bash
# Clone or download the factverse folder
cd factverse

# Run the simplified version (works immediately)
python main_simple.py

# Or use the launcher script
bash start.sh
```

## 🤖 AI-Enhanced Setup

### Step 1: Install OpenAI Library
```bash
# Python pip installation
pip install openai

# Or for Python 3
pip3 install openai

# Termux (Android)
pkg install python
pip install openai
```

### Step 2: Get OpenAI API Key
1. Visit https://platform.openai.com/api-keys
2. Create an account or sign in
3. Generate a new API key
4. Copy the key (starts with `sk-`)

### Step 3: Set Environment Variable (SECURE METHOD)

#### Windows PowerShell
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
python factverse_ai.py
```

#### Linux/Mac Terminal
```bash
export OPENAI_API_KEY="your-api-key-here"
python factverse_ai.py
```

#### Termux (Android)
```bash
export OPENAI_API_KEY="your-api-key-here"
python factverse_ai.py
```

#### Persistent Setup (Recommended)
Add to your shell profile:

**Windows (.profile or PowerShell profile):**
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

**Linux/Mac (~/.bashrc or ~/.zshrc):**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**Termux (~/.bashrc):**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## 🎮 Usage Modes

### 1. Local Facts Only
```bash
python main_simple.py
```
- No API key required
- Uses curated facts from facts.json
- Fast and reliable

### 2. AI-Enhanced Mode
```bash
python factverse_ai.py
```
- Requires OpenAI API key
- Generates unique facts using AI
- Falls back to local facts if AI fails
- Toggle between AI and local modes in-app

### 3. Launcher Script
```bash
bash start.sh
```
- Colored terminal output
- Figlet banner (if installed)
- Automatically detects Python version

## 🔧 Advanced Configuration

### Optional Visual Enhancements
```bash
# For enhanced terminal banners
# Linux/Mac
sudo apt install figlet lolcat  # Ubuntu/Debian
brew install figlet lolcat      # macOS

# Termux
pkg install figlet
pkg install ruby
gem install lolcat
```

### Custom Facts
Edit `facts.json` to add your own facts:
```json
{
  "hacking": [
    "Your custom hacking fact here",
    "Another cybersecurity insight"
  ]
}
```

### AI Prompt Customization
Edit `fact_ai_generator.py` category_prompts:
```python
self.category_prompts = {
    'hacking': "Your custom AI prompt for hacking facts",
    'fun': "Your custom AI prompt for fun facts"
}
```

## 🛡️ Security Best Practices

### ✅ DO:
- Use environment variables for API keys
- Never commit API keys to version control
- Use the `.env` file method for projects
- Rotate API keys regularly

### ❌ DON'T:
- Hard-code API keys in source code
- Share API keys in chat/email
- Commit `.env` files with real keys
- Use API keys in public repositories

## 🐛 Troubleshooting

### Common Issues

#### "No module named 'openai'"
```bash
pip install openai
# or
pip3 install openai
```

#### "API key not found"
```bash
# Check if environment variable is set
echo $OPENAI_API_KEY  # Linux/Mac
echo $env:OPENAI_API_KEY  # Windows PowerShell
```

#### "Permission denied" (Linux/Termux)
```bash
chmod +x start.sh
chmod +x factverse_ai.py
```

#### Python not found
```bash
# Try different Python commands
python3 factverse_ai.py
python3.x factverse_ai.py
```

### Debug Mode
Add debug prints to see what's happening:
```python
print(f"AI Available: {AI_AVAILABLE}")
print(f"API Key Set: {bool(os.getenv('OPENAI_API_KEY'))}")
```

## 📊 Features Comparison

| Feature | main_simple.py | factverse_ai.py |
|---------|----------------|-----------------|
| Local Facts | ✅ | ✅ |
| AI Generation | ❌ | ✅ |
| Typing Animation | ✅ | ✅ |
| Hacker UI | ✅ | ✅ |
| Save to File | ✅ | ✅ |
| Progress Bars | ❌ | ✅ |
| AI Toggle | ❌ | ✅ |
| Fallback Mode | N/A | ✅ |

## 🚀 Deployment

### For Personal Use
- Use `factverse_ai.py` with your API key
- Perfect for learning and experimentation

### For Distribution
- Use `main_simple.py` (no API requirements)
- Include `facts.json` with curated facts
- Users can optionally add AI later

### For Termux Users
- All features work perfectly in Android Termux
- Great for mobile hacking/learning environments
- No root required

## 📝 License & Credits

- **Created by:** w7nx_z
- **License:** Open source
- **AI Integration:** OpenAI GPT-3.5/4
- **Compatible:** Windows, Linux, macOS, Android (Termux)

---

**Ready to hack some knowledge!** 🕶️⚡
