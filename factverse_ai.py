#!/usr/bin/env python3
"""
FactVerse - Ultimate AI-Enhanced Hacker-Style Fact Generator
Made by w7nx_z
Version 2.0 with AI Integration
"""

import json
import random
import os
import sys
import time

# AI Integration
try:
    from fact_ai_generator import AIFactGenerator
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False

class FactVerse:
    def __init__(self):
        """Initialize FactVerse with AI capabilities"""
        self.facts = self.load_facts()
        self.categories = {
            '1': 'hacking',
            '2': 'fun',
            '3': 'attitude',
            '4': 'lazy',
            '5': 'motivation'
        }
        self.category_display = {
            'hacking': '🧠 Hacking Intel',
            'fun': '🎭 Fun Bytes',
            'attitude': '😎 Attitude Logs',
            'lazy': '💤 Lazy Logs',
            'motivation': '🚀 Motivation Doses'
        }
        
        # Initialize AI if available
        self.ai_generator = None
        self.ai_mode = False
        if AI_AVAILABLE:
            try:
                self.ai_generator = AIFactGenerator()
                if self.ai_generator.openai_available:
                    self.ai_mode = True
            except:
                pass  # Silent fallback to local facts
    
    def load_facts(self):
        """Load facts from JSON file"""
        try:
            with open('facts.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("❌ Error: facts.json file not found!")
            sys.exit(1)
    
    def typing_animation(self, text, delay=0.02):
        """Simulate typing animation"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def show_progress_bar(self, duration=1.5):
        """Show loading progress bar"""
        print("[ Loading tool... ] ", end='', flush=True)
        bar_length = 20
        for i in range(bar_length + 1):
            percent = int((i / bar_length) * 100)
            filled = '█' * i
            empty = '▒' * (bar_length - i)
            print(f'\\r[ Loading tool... ] {filled}{empty} {percent}%', end='', flush=True)
            time.sleep(duration / bar_length)
        print()
    
    def show_banner(self):
        """Display hacker-style startup banner"""
        print("🟢 Initializing... ⏳")
        time.sleep(0.5)
        print("🔐 Launching: FactVerse – AI-Enhanced Fact Generator")
        time.sleep(0.5)
        print("👨‍💻 Creator: w7nx_z")
        time.sleep(0.5)
        print("🧬 Terminal Interface Active...")
        
        # Show AI status
        if self.ai_mode:
            print("🤖 AI Fact Generator: ONLINE")
        else:
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
        self.show_progress_bar()
        print()
    
    def show_menu(self):
        """Display category menu"""
        print("💾 Choose a Category to Extract Random Data:")
        print()
        print("[1] 🧠 Hacking Intel")
        print("[2] 🎭 Fun Bytes")
        print("[3] 😎 Attitude Logs")
        print("[4] 💤 Lazy Logs")
        print("[5] 🚀 Motivation Doses")
        if AI_AVAILABLE and self.ai_generator and self.ai_generator.openai_available:
            ai_status = "ON" if self.ai_mode else "OFF"
            print(f"[6] 🤖 Toggle AI Mode ({ai_status})")
            print("[7] 🛑 Exit Terminal")
        else:
            print("[6] 🛑 Exit Terminal")
        print()
    
    def get_fact(self, category_key):
        """Get fact from AI or local database"""
        category = self.categories[category_key]
        
        # Try AI first if enabled
        if self.ai_mode and self.ai_generator:
            try:
                fact, source = self.ai_generator.generate_fact(category, prefer_ai=True)
                return fact, source
            except:
                pass  # Fallback to local
        
        # Use local facts
        if category in self.facts:
            return random.choice(self.facts[category]), "LOCAL"
        return "No facts available.", "ERROR"
    
    def show_fact(self, category_key):
        """Display fact with hacker styling"""
        category = self.categories[category_key]
        category_display = self.category_display[category]
        
        print("[✔️] Access Granted.")
        time.sleep(0.5)
        
        if self.ai_mode:
            self.typing_animation(f"[🤖] Generating AI fact for: {category_display}...")
        else:
            self.typing_animation(f"[🧠] Fetching random entry from: {category_display}...")
        print()
        
        fact, source = self.get_fact(category_key)
        
        print("📄 Terminal Output:")
        print(">> ", end='')
        self.typing_animation(f'"{fact}"', delay=0.015)
        
        # Show source
        if source == "AI":
            print("[🤖 AI-Generated]")
        else:
            print("[📚 Database]")
        
        print("-" * 60)
        print()
        return fact, source
    
    def save_fact(self, fact, source):
        """Save fact to file with source tag"""
        try:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            source_tag = "[AI]" if source == "AI" else "[DB]"
            with open("saved_facts.txt", 'a', encoding='utf-8') as file:
                file.write(f"[{timestamp}] {source_tag} {fact}\\n")
            print("✅ Fact saved successfully!")
        except Exception as e:
            print(f"❌ Error saving fact: {e}")
    
    def toggle_ai_mode(self):
        """Toggle AI mode on/off"""
        if not AI_AVAILABLE or not self.ai_generator or not self.ai_generator.openai_available:
            print("🔒 AI mode requires OpenAI API key. Set OPENAI_API_KEY environment variable.")
            time.sleep(2)
            return
        
        self.ai_mode = not self.ai_mode
        status = "ENABLED" if self.ai_mode else "DISABLED"
        print(f"🤖 AI Mode: {status}")
        time.sleep(1)
    
    def show_exit(self):
        """Display exit sequence"""
        print("📴 Disconnecting from FactVerse Terminal...")
        time.sleep(0.5)
        print("💾 Saving session data...")
        time.sleep(0.5)
        print("🔒 Encrypting your activity logs...")
        time.sleep(0.5)
        print("🔁 Terminating session variables...")
        print()
        
        print("👨‍💻 Agent: w7nx_z")
        print("🟢 Status: Safe Disconnect")
        print()
        
        # Logout progress bar
        bar_length = 40
        for i in range(bar_length + 1):
            percent = int((i / bar_length) * 100)
            filled = '█' * i
            empty = ' ' * (bar_length - i)
            print(f'\\r[{filled}{empty}] {percent}%', end='', flush=True)
            time.sleep(0.02)
        
        print()
        print("✅ Logout successful.")
        print()
        if os.path.exists("saved_facts.txt"):
            print("📁 Your saved facts are in: saved_facts.txt")
        print("🕶️ Stay anonymous, stay curious.")
        print("👋 Goodbye, hacker.")
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def run(self):
        """Main application loop"""
        # Show startup
        self.show_banner()
        
        while True:
            self.show_menu()
            choice = input("📥 Enter your command code: ").strip()
            
            # Handle exit
            exit_option = '7' if (AI_AVAILABLE and self.ai_generator and self.ai_generator.openai_available) else '6'
            if choice == exit_option:
                self.show_exit()
                break
            
            # Handle AI toggle
            if choice == '6' and AI_AVAILABLE and self.ai_generator and self.ai_generator.openai_available:
                self.toggle_ai_mode()
                self.clear_screen()
                self.show_banner()
                continue
            
            # Handle fact categories
            if choice in self.categories:
                self.clear_screen()
                fact, source = self.show_fact(choice)
                
                print("🔁 Actions:")
                print("[1] Get Another  [2] Change Category  [3] Exit Tool")
                save_choice = input("💾 Save this fact to `saved_facts.txt`? [Y/n]: ").lower()
                
                if save_choice in ['y', 'yes', '']:
                    self.save_fact(fact, source)
                print()
                
                # Fact action loop
                while True:
                    action = input("📥 Enter your choice: ").strip()
                    if action == '1':
                        self.clear_screen()
                        fact, source = self.show_fact(choice)
                        
                        print("🔁 Actions:")
                        print("[1] Get Another  [2] Change Category  [3] Exit Tool")
                        save_choice = input("💾 Save this fact to `saved_facts.txt`? [Y/n]: ").lower()
                        
                        if save_choice in ['y', 'yes', '']:
                            self.save_fact(fact, source)
                        print()
                    elif action == '2':
                        self.clear_screen()
                        self.show_banner()
                        break
                    elif action == '3':
                        self.show_exit()
                        return
                    else:
                        print("❌ Invalid choice! Please select 1, 2, or 3.")
            else:
                max_option = '7' if (AI_AVAILABLE and self.ai_generator and self.ai_generator.openai_available) else '6'
                print(f"❌ Invalid command code! Please select 1-{max_option}.")
                print()

def main():
    """Entry point"""
    try:
        app = FactVerse()
        app.run()
    except KeyboardInterrupt:
        print("\\n")
        print("👋 Thanks for using FactVerse!")
        sys.exit(0)

if __name__ == "__main__":
    main()
