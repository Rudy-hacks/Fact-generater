#!/usr/bin/env python3
"""
FactVerse AI - Pure AI-Powered Fact Generator
Made by w7nx_z
Uses OpenAI API exclusively - no static files
"""

from openai import OpenAI
import time
import sys
import random

# OpenRouter API Configuration (using OpenAI-compatible client)
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# Track generated facts to avoid duplicates
generated_facts = set()

def generate_ai_fact(category: str, max_retries: int = 3) -> str:
    """
    Generate a unique fact using OpenAI API with retry logic and uniqueness checking
    Returns fact only when successfully generated and unique
    """
    # Enhanced prompts with randomization keywords
    prompts = {
        'hacking': [
            "Generate one fascinating, lesser-known cybersecurity or hacking fact that most people don't know.",
            "Share an interesting fact about cyber attacks, data breaches, or hacking techniques.",
            "Tell me a surprising fact about cybersecurity, hackers, or digital security that's educational.",
            "Give me a unique fact about the world of hacking, cyber crime, or information security.",
            "Share an amazing fact about famous hackers, security vulnerabilities, or cyber warfare."
        ],
        'fun': [
            "Generate one mind-blowing, surprising fun fact that will amaze people.",
            "Share a fascinating and unusual fact about nature, science, or the world around us.",
            "Tell me an incredible fact that sounds unbelievable but is actually true.",
            "Give me a weird and wonderful fact about animals, space, history, or science.",
            "Share an amazing fact that most people have never heard before."
        ],
        'attitude': [
            "Share an inspiring quote about mindset, success, and positive thinking.",
            "Give me a motivational fact about attitude, personal growth, or achieving goals.",
            "Share wisdom about developing a winning mindset and strong character.",
            "Tell me an empowering fact about confidence, determination, or self-improvement.",
            "Give me an inspiring insight about attitude, resilience, or mental strength."
        ],
        'lazy': [
            "Share a funny, relatable quote or fact about procrastination and laziness.",
            "Give me a humorous fact about being lazy, avoiding work, or procrastinating.",
            "Tell me a witty observation about laziness, comfort zones, or taking it easy.",
            "Share a clever joke or fact about the art of doing nothing productively.",
            "Give me a funny insight about lazy people, rest, or avoiding effort."
        ]
    }
    
    category_prompts = prompts.get(category, [f"Generate one interesting {category} fact."])
    
    for attempt in range(max_retries):
        try:
            print(f"🤖 Generating {category} fact... (attempt {attempt + 1})")
            
            # Randomize prompt selection and add uniqueness request
            selected_prompt = random.choice(category_prompts)
            unique_request = f"{selected_prompt} Make it unique and different from common knowledge. Respond in exactly one sentence."
            
            response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative fact generator. Always provide fresh, unique, and interesting facts. Never repeat the same information. Be engaging and educational."},
                    {"role": "user", "content": unique_request}
                ],
                max_tokens=80,
                temperature=0.9,  # Increased for more creativity
                top_p=0.95,       # Add randomness
                frequency_penalty=0.5,  # Reduce repetition
                presence_penalty=0.3    # Encourage new topics
            )
            
            fact = response.choices[0].message.content.strip()
            
            # Validate fact is not empty and meaningful
            if fact and len(fact) > 15:
                # Clean up quotes if present
                if fact.startswith('"') and fact.endswith('"'):
                    fact = fact[1:-1]
                
                # Check for uniqueness
                fact_key = fact.lower().strip()
                if fact_key not in generated_facts:
                    generated_facts.add(fact_key)
                    return fact
                else:
                    print(f"🔄 Duplicate fact detected, generating new one...")
                    continue
            else:
                print(f"⚠️ Empty or invalid fact received, retrying...")
                
        except Exception as e:
            print(f"🔥 API Error (attempt {attempt + 1}): {str(e)}")
            if attempt < max_retries - 1:
                print("🔄 Retrying in 2 seconds...")
                time.sleep(2)
    
    # If all retries failed, return error message
    return f"Failed to generate unique {category} fact after {max_retries} attempts. Please try again."

def show_banner():
    """Display FactVerse AI banner"""
    print("🤖 FactVerse AI - Live Fact Generator")
    print("👨‍💻 Created by w7nx_z")
    print("🧠 Powered by OpenAI GPT")
    print("=" * 40)

def show_menu():
    """Display category selection menu"""
    print("\n📂 Select a Category:")
    print("[1] 🔒 Hacking & Cybersecurity")
    print("[2] 🎉 Fun & Amazing Facts")
    print("[3] 😎 Attitude & Mindset")
    print("[4] 😴 Lazy & Humor")
    print("[5] 🛑 Exit")

def get_category_name(choice: str) -> str:
    """Convert choice number to category name"""
    categories = {
        '1': ('hacking', '🔒 Hacking & Cybersecurity'),
        '2': ('fun', '🎉 Fun & Amazing Facts'),
        '3': ('attitude', '😎 Attitude & Mindset'),
        '4': ('lazy', '😴 Lazy & Humor')
    }
    return categories.get(choice, (None, None))

def main():
    """Main application loop"""
    show_banner()
    
    while True:
        show_menu()
        choice = input("\n📥 Enter your choice (1-5): ").strip()
        
        if choice == '5':
            print("\n👋 Thanks for using FactVerse AI!")
            print("🕶️ Stay curious, stay anonymous!")
            break
        
        category_key, category_display = get_category_name(choice)
        
        if category_key:
            print(f"\n🎯 Selected: {category_display}")
            print("🔄 Connecting to AI...")
            
            # Generate fact with retry logic
            fact = generate_ai_fact(category_key)
            
            print(f"\n✅ Your {category_display} Fact:")
            print(f"💡 {fact}")
            print("\n" + "=" * 50)
            
            # Ask if user wants another fact
            continue_choice = input("\n🔄 Generate another fact? (y/n): ").lower()
            if continue_choice not in ['y', 'yes', '']:
                print("\n👋 Thanks for using FactVerse AI!")
                break
        else:
            print("❌ Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 FactVerse AI session ended.")
        print("🕶️ Stay curious!")
        sys.exit(0)
    except Exception as e:
        print(f"\n🔥 Unexpected error: {e}")
        print("Please check your internet connection and API key.")
        sys.exit(1)
