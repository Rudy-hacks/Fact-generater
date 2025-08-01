#!/bin/bash

# FactVerse Hacker-Style Launcher Script
# Created by w7nx_z

# Color codes for terminal styling
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔐 Initializing FactVerse Terminal...${NC}"
echo -e "${CYAN}👨‍💻 Hacker Tool by w7nx_z${NC}"
echo ""

# Check if figlet and lolcat are available for enhanced banner
if command -v figlet >/dev/null 2>&1 && command -v lolcat >/dev/null 2>&1; then
    figlet "FactVerse" | lolcat
    echo -e "${YELLOW}🎨 Enhanced banner mode: ACTIVE${NC}"
else
    echo -e "${RED}================================${NC}"
    echo -e "${GREEN}🔐      FactVerse Tool        🔐${NC}"
    echo -e "${RED}================================${NC}"
    echo -e "${YELLOW}� Tip: Install figlet & lolcat for enhanced visuals${NC}"
fi

echo ""
echo -e "${CYAN}🚀 Launching hacker interface...${NC}"
echo -e "${GREEN}📡 Connecting to fact database...${NC}"
echo ""

# Small delay for dramatic effect
sleep 1.5

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if Python is available
if command -v python3 >/dev/null 2>&1; then
    python3 "$SCRIPT_DIR/main.py"
elif command -v python >/dev/null 2>&1; then
    python "$SCRIPT_DIR/main.py"
else
    echo "❌ Error: Python is not installed or not in PATH"
    echo "Please install Python to run FactVerse"
    exit 1
fi
