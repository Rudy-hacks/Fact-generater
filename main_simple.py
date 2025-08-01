#!/usr/bin/env python3
"""
FactVerse - AI-Enhanced Hacker-Style Fact Generator
Made by w7nx_z
"""

import json
import random
import os
import sys
import time

def load_facts():
    """Load facts from JSON file"""
    try:
        with open('facts.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ Error: facts.json file not found!")
        sys.exit(1)

def typing_animation(text, delay=0.02):
    """Simulate typing animation"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_banner():
    """Display hacker-style banner"""
    print("🟢 Initializing... ⏳")
    time.sleep(0.5)
    print("🔐 Launching: FactVerse – AI-Enhanced Fact Generator")
    time.sleep(0.5)
    print("👨‍💻 Creator: w7nx_z")
    time.sleep(0.5)
    print("🧬 Terminal Interface Active...")
    print("📚 Local Fact Database: ACTIVE")
    print()
    
    # Show ASCII banner
    try:
        with open('assets/banner.txt', 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print("████████████████████████████████████")
        print("█───█────█────█────█───█────█──────█")
        print("█ F A C T V E R S E   T O O L █")
        print("█───█────█────█────█───█────█──────█")
        print("████████████████████████████████████")
    print()

def show_menu():
    """Display category menu"""
    print("💾 Choose a Category to Extract Random Data:")
    print()
    print("[1] 🧠 Hacking Intel")
    print("[2] 🎭 Fun Bytes")
    print("[3] 😎 Attitude Logs")
    print("[4] 💤 Lazy Logs")
    print("[5] 🚀 Motivation Doses")
    print("[6] 🛑 Exit Terminal")
    print()

def get_random_fact(facts, category):
    """Get random fact from category"""
    categories = {
        '1': 'hacking',
        '2': 'fun',
        '3': 'attitude',
        '4': 'lazy',
        '5': 'motivation'
    }
    
    category_key = categories.get(category)
    if category_key and category_key in facts:
        return random.choice(facts[category_key]), category_key
    return "No facts available.", "unknown"

def show_fact(fact, category):
    """Display fact with hacker styling"""
    category_names = {
        'hacking': '🧠 Hacking Intel',
        'fun': '🎭 Fun Bytes',
        'attitude': '😎 Attitude Logs',
        'lazy': '💤 Lazy Logs',
        'motivation': '🚀 Motivation Doses'
    }
    
    print("[✔️] Access Granted.")
    time.sleep(0.5)
    typing_animation(f"[🧠] Fetching random entry from: {category_names.get(category, category)}...")
    print()
    
    print("📄 Terminal Output:")
    print(">> ", end='')
    typing_animation(f'"{fact}"', delay=0.015)
    print("[📚 Database]")
    print("-" * 60)
    print()

def save_fact(fact):
    """Save fact to file"""
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open("saved_facts.txt", 'a', encoding='utf-8') as file:
            file.write(f"[{timestamp}] [DB] {fact}\n")
        print("✅ Fact saved successfully!")
    except Exception as e:
        print(f"❌ Error saving fact: {e}")

def show_exit():
    """Show exit sequence"""
    print("📴 Disconnecting from FactVerse Terminal...")
    time.sleep(0.5)
    print("💾 Saving session data...")
    time.sleep(0.5)
    print("🔒 Encrypting your activity logs...")
    time.sleep(0.5)
    print("✅ Logout successful.")
    print()
    print("🕶️ Stay anonymous, stay curious.")
    print("👋 Goodbye, hacker.")

def main():
    """Main application loop"""
    # Load facts
    facts = load_facts()
    
    # Show startup sequence
    show_banner()
    
    while True:
        show_menu()
        choice = input("📥 Enter your command code: ").strip()
        
        if choice == '6':
            show_exit()
            break
        elif choice in ['1', '2', '3', '4', '5']:
            os.system('cls' if os.name == 'nt' else 'clear')
            fact, category = get_random_fact(facts, choice)
            show_fact(fact, category)
            
            print("🔁 Actions:")
            print("[1] Get Another  [2] Change Category  [3] Exit Tool")
            save_choice = input("💾 Save this fact to `saved_facts.txt`? [Y/n]: ").lower()
            
            if save_choice in ['y', 'yes', '']:
                save_fact(fact)
            print()
            
            while True:
                action = input("📥 Enter your choice: ").strip()
                if action == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    fact, category = get_random_fact(facts, choice)
                    show_fact(fact, category)
                    
                    print("🔁 Actions:")
                    print("[1] Get Another  [2] Change Category  [3] Exit Tool")
                    save_choice = input("💾 Save this fact to `saved_facts.txt`? [Y/n]: ").lower()
                    
                    if save_choice in ['y', 'yes', '']:
                        save_fact(fact)
                    print()
                elif action == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    show_banner()
                    break
                elif action == '3':
                    show_exit()
                    return
                else:
                    print("❌ Invalid choice! Please select 1, 2, or 3.")
        else:
            print("❌ Invalid command code! Please select 1-6.")
            print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        show_exit()
        sys.exit(0)
