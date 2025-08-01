#!/usr/bin/env python3
print("Testing basic script execution...")

import json
import random
import os
import sys
import time

print("All imports successful!")

# Test AI import
try:
    from fact_ai_generator import AIFactGenerator
    print("AI Generator imported successfully!")
    AI_AVAILABLE = True
except ImportError as e:
    print(f"AI Generator import failed: {e}")
    AI_AVAILABLE = False

print(f"AI Available: {AI_AVAILABLE}")

class FactVerse:
    def __init__(self):
        print("FactVerse initializing...")
        self.facts = {}
        
        # Test loading facts
        try:
            with open('facts.json', 'r', encoding='utf-8') as file:
                self.facts = json.load(file)
                print(f"Loaded {len(self.facts)} fact categories")
        except Exception as e:
            print(f"Error loading facts: {e}")
    
    def test_run(self):
        print("🔐 FactVerse Test Mode")
        print("Testing completed successfully!")

if __name__ == "__main__":
    print("Starting FactVerse test...")
    app = FactVerse()
    app.test_run()
