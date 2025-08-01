#!/usr/bin/env python3
"""
FactVerse - Simple Test Version
Made by w7nx_z
"""

import random
import time

# Hardcoded facts for testing
FACTS = {
    'hacking': [
        "Most black-hat hackers start learning before the age of 16.",
        "The term 'hacker' originally meant someone who was skilled at programming.",
        "White hat hackers help companies find security vulnerabilities legally.",
        "Social engineering is often more effective than technical attacks.",
        "Two-factor authentication can prevent 99.9% of automated attacks."
    ],
    'fun': [
        "Honey never spoils - archaeologists have found edible honey in ancient Egyptian tombs.",
        "A group of flamingos is called a 'flamboyance'.",
        "Bananas are berries, but strawberries aren't.",
        "Octopuses have three hearts and blue blood.",
        "A jiffy is an actual unit of time - 1/100th of a second."
    ],
    'attitude': [
        "Your attitude determines your altitude in life.",
        "Confidence is not 'they will like me', it's 'I'll be fine if they don't'.",
        "Don't let someone dim your light simply because it's shining in their eyes.",
        "Attitude is everything, so pick a good one.",
        "Life is 10% what happens to you and 90% how you react to it."
    ],
    'lazy': [
        "I'm not lazy, I'm on energy saving mode.",
        "I choose a lazy person to do a hard job because they will find an easy way to do it.",
        "Hard work never killed anybody, but why take a chance?",
        "I put the 'Pro' in procrastination.",
        "I'm not lazy, I'm just highly motivated to do nothing."
    ],
    'motivation': [
        "The only impossible journey is the one you never begin.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Don't watch the clock; do what it does. Keep going.",
        "Believe you can and you're halfway there.",
        "The only way to do great work is to love what you do."
    ]
}

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
    print("🔐 Launching: FactVerse – Hacker Fact Generator")
    time.sleep(0.5)
    print("👨‍💻 Creator: w7nx_z")
    time.sleep(0.5)
    print("🧬 Terminal Interface Active...")
    print("📚 Local Fact Database: ACTIVE")
    print()
    
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

def get_fact(choice):
    """Get random fact from category"""
    categories = {
        '1': 'hacking',
        '2': 'fun',
        '3': 'attitude',
        '4': 'lazy',
        '5': 'motivation'
    }
    
    category_names = {
        'hacking': '🧠 Hacking Intel',
        'fun': '🎭 Fun Bytes',
        'attitude': '😎 Attitude Logs',
        'lazy': '💤 Lazy Logs',
        'motivation': '🚀 Motivation Doses'
    }
    
    category = categories.get(choice)
    if category and category in FACTS:
        fact = random.choice(FACTS[category])
        return fact, category_names[category]
    return "No facts available.", "Unknown"

def show_fact(fact, category_name):
    """Display fact with hacker styling"""
    print("[✔️] Access Granted.")
    time.sleep(0.5)
    typing_animation(f"[🧠] Fetching random entry from: {category_name}...")
    print()
    
    print("📄 Terminal Output:")
    print(">> ", end='')
    typing_animation(f'"{fact}"', delay=0.015)
    print("[📚 Database]")
    print("-" * 60)
    print()

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
    show_banner()
    
    while True:
        show_menu()
        choice = input("📥 Enter your command code: ").strip()
        
        if choice == '6':
            show_exit()
            break
        elif choice in ['1', '2', '3', '4', '5']:
            print()  # Clear line
            fact, category_name = get_fact(choice)
            show_fact(fact, category_name)
            
            print("🔁 Actions:")
            print("[1] Get Another  [2] Change Category  [3] Exit Tool")
            
            while True:
                action = input("📥 Enter your choice: ").strip()
                if action == '1':
                    print()
                    fact, category_name = get_fact(choice)
                    show_fact(fact, category_name)
                    print("🔁 Actions:")
                    print("[1] Get Another  [2] Change Category  [3] Exit Tool")
                elif action == '2':
                    print()
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
