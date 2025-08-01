# fact_ai_generator.py - AI-Powered Fact Generation for FactVerse
# Made by w7nx_z
# Secure AI integration with fallback to local facts

import os
import json
import random
from typing import Optional

class AIFactGenerator:
    def __init__(self):
        self.api_key = None
        self.openai_available = False
        self.local_facts_file = "facts.json"
        self.category_prompts = {
            'hacking': "Generate a fascinating cybersecurity or hacking-related fact",
            'fun': "Generate an amazing and surprising fun fact",
            'attitude': "Generate an inspiring quote about attitude and mindset",
            'lazy': "Generate a humorous fact or quote about laziness",
            'motivation': "Generate an inspiring motivational quote or fact"
        }
        self._setup_openai()
        self._load_local_facts()
    
    def _setup_openai(self):
        """Setup OpenAI API with secure key handling"""
        try:
            # Check for API key in environment variable (secure method)
            self.api_key = os.getenv('OPENAI_API_KEY')
            
            if self.api_key:
                import openai
                openai.api_key = self.api_key
                self.openai_available = True
                # Silent initialization for main app
                # print("🤖 AI Mode: ACTIVE")
            else:
                # Silent initialization for main app
                # print("🔒 AI Mode: DISABLED (No API key found)")
                # print("💡 Tip: Set OPENAI_API_KEY environment variable to enable AI facts")
                pass
                
        except ImportError:
            # Silent initialization for main app
            # print("📦 OpenAI library not installed. Using local facts only.")
            # print("💡 Install with: pip install openai")
            pass
    
    def _load_local_facts(self):
        """Load local facts as fallback"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            facts_file = os.path.join(script_dir, self.local_facts_file)
            
            with open(facts_file, 'r', encoding='utf-8') as file:
                self.local_facts = json.load(file)
        except FileNotFoundError:
            self.local_facts = {}
            print("⚠️ Warning: Local facts file not found")
    
    def generate_ai_fact(self, category: str) -> Optional[str]:
        """Generate a fact using OpenAI API"""
        if not self.openai_available:
            return None
            
        try:
            import openai
            
            prompt = self.category_prompts.get(category, f"Generate an interesting {category} fact")
            prompt += " in one concise sentence. Make it unique and engaging."
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a fact generator. Provide accurate, interesting facts in a single sentence."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=60,
                temperature=0.8,
            )
            
            fact = response['choices'][0]['message']['content'].strip()
            # Remove quotes if present
            if fact.startswith('"') and fact.endswith('"'):
                fact = fact[1:-1]
            
            return fact
            
        except Exception as e:
            print(f"🔥 AI Error: {str(e)}")
            return None
    
    def get_local_fact(self, category: str) -> str:
        """Get a random fact from local JSON file"""
        if category in self.local_facts and self.local_facts[category]:
            return random.choice(self.local_facts[category])
        return f"No local facts available for category: {category}"
    
    def generate_fact(self, category: str, prefer_ai: bool = True) -> tuple[str, str]:
        """
        Generate a fact with AI fallback to local facts
        Returns: (fact_text, source_type)
        """
        source_type = "LOCAL"
        
        # Try AI first if preferred and available
        if prefer_ai and self.openai_available:
            ai_fact = self.generate_ai_fact(category)
            if ai_fact:
                return ai_fact, "AI"
        
        # Fallback to local facts
        local_fact = self.get_local_fact(category)
        return local_fact, "LOCAL"
    
    def get_status(self) -> dict:
        """Get current AI generator status"""
        return {
            "ai_available": self.openai_available,
            "api_key_set": bool(self.api_key),
            "local_facts_loaded": bool(self.local_facts),
            "categories": list(self.category_prompts.keys())
        }

# === Standalone Demo ===
def demo_ai_generator():
    """Demo function for testing AI fact generation"""
    print("🔐 FactVerse AI Generator Demo")
    print("=" * 40)
    
    generator = AIFactGenerator()
    status = generator.get_status()
    
    print(f"🤖 AI Available: {status['ai_available']}")
    print(f"🔑 API Key Set: {status['api_key_set']}")
    print(f"📚 Local Facts: {status['local_facts_loaded']}")
    print()
    
    # Test categories
    categories = ['hacking', 'fun', 'attitude', 'lazy', 'motivation']
    
    for category in categories:
        print(f"🧠 Testing {category.upper()} category:")
        fact, source = generator.generate_fact(category)
        print(f"   [{source}] {fact}")
        print()

# === Setup Instructions ===
def show_setup_instructions():
    """Show setup instructions for AI integration"""
    print("""
🔧 AI SETUP INSTRUCTIONS:

1. Install OpenAI library:
   pip install openai

2. Get API key from OpenAI:
   https://platform.openai.com/api-keys

3. Set environment variable (SECURE METHOD):
   
   Windows (PowerShell):
   $env:OPENAI_API_KEY="your-api-key-here"
   
   Linux/Mac (Terminal):
   export OPENAI_API_KEY="your-api-key-here"
   
   Termux (Android):
   export OPENAI_API_KEY="your-api-key-here"

4. Restart your terminal and run FactVerse

⚠️ SECURITY NOTE:
Never hard-code API keys in source code!
Always use environment variables for API keys.
""")

if __name__ == "__main__":
    print("🔐 FactVerse AI Generator")
    print("Choose an option:")
    print("[1] Demo AI Generator")
    print("[2] Show Setup Instructions")
    print("[3] Exit")
    
    choice = input("\n📥 Enter choice: ").strip()
    
    if choice == '1':
        demo_ai_generator()
    elif choice == '2':
        show_setup_instructions()
    else:
        print("👋 Goodbye!")
