#!/usr/bin/env python3
"""
Log2Tweet - Gemini API Setup Helper
Helps users set up their Google Gemini API key for Log2Tweet.
"""

import json
import os
from pathlib import Path

def setup_gemini_api():
    """Guide user through Gemini API setup."""
    print("🚀 Log2Tweet - Gemini API Setup")
    print("=" * 40)
    print()
    print("To use Log2Tweet with Google Gemini, you need an API key.")
    print()
    print("📋 Steps to get your Gemini API key:")
    print("1. Go to Google AI Studio: https://makersuite.google.com/app/apikey")
    print("2. Sign in with your Google account")
    print("3. Click 'Create API Key'")
    print("4. Copy the generated API key")
    print()
    
    # Check if config file exists
    config_file = Path("llm_config.json")
    if config_file.exists():
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            if config.get('gemini_api_key') and config['gemini_api_key'] != 'YOUR_GEMINI_API_KEY':
                print("✅ You already have a Gemini API key configured!")
                print(f"Current key: {config['gemini_api_key'][:10]}...")
                print()
                
                update = input("Would you like to update it? (y/n): ").lower().strip()
                if update != 'y':
                    print("Setup cancelled.")
                    return
        except:
            pass
    
    print("🔑 Enter your Gemini API key:")
    api_key = input("API Key: ").strip()
    
    if not api_key:
        print("❌ No API key provided. Setup cancelled.")
        return
    
    if api_key == 'YOUR_GEMINI_API_KEY':
        print("❌ Please enter your actual API key, not the placeholder.")
        return
    
    # Create or update config
    config = {
        "gemini_api_key": api_key,
        "model": "gemini-pro",
        "max_tokens": 100,
        "temperature": 0.7
    }
    
    try:
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print()
        print("✅ Gemini API key configured successfully!")
        print(f"📁 Configuration saved to: {config_file}")
        print()
        print("🎯 Next steps:")
        print("1. Configure your Twitter API keys in twitter_config.json")
        print("2. Test the setup: python test_setup.py")
        print("3. Start logging tasks: python log.py 'Your first task'")
        
    except Exception as e:
        print(f"❌ Error saving configuration: {e}")

def test_gemini_connection():
    """Test the Gemini API connection."""
    print("\n🧪 Testing Gemini API connection...")
    
    try:
        import google.generativeai as genai
        
        config_file = Path("llm_config.json")
        if not config_file.exists():
            print("❌ llm_config.json not found. Run setup first.")
            return
        
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        api_key = config.get('gemini_api_key')
        if not api_key or api_key == 'YOUR_GEMINI_API_KEY':
            print("❌ No valid API key found. Run setup first.")
            return
        
        # Configure and test
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        # Simple test prompt
        response = model.generate_content("Say 'Hello from Log2Tweet!' in one sentence.")
        
        if response.text:
            print("✅ Gemini API connection successful!")
            print(f"🤖 Response: {response.text.strip()}")
        else:
            print("❌ No response from Gemini API")
            
    except ImportError:
        print("❌ google-generativeai not installed. Run: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Gemini API test failed: {e}")

def main():
    """Main setup function."""
    print("Welcome to Log2Tweet Gemini Setup!")
    print()
    
    while True:
        print("Choose an option:")
        print("1. Setup Gemini API key")
        print("2. Test Gemini connection")
        print("3. Exit")
        print()
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            setup_gemini_api()
        elif choice == '2':
            test_gemini_connection()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
        
        print("\n" + "=" * 40 + "\n")

if __name__ == "__main__":
    main()





