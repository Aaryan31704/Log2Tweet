#!/usr/bin/env python3
"""
Log2Tweet - Setup Test Script
Tests if all dependencies and configurations are properly set up.
"""

import sys
import json
from pathlib import Path

def test_imports():
    """Test if all required packages can be imported."""
    print("🔍 Testing package imports...")
    
    try:
        import tweepy
        print("✅ tweepy imported successfully")
    except ImportError:
        print("❌ tweepy not found. Run: pip install tweepy")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ google-generativeai imported successfully")
    except ImportError:
        print("❌ google-generativeai not found. Run: pip install google-generativeai")
        return False
    
    try:
        import schedule
        print("✅ schedule imported successfully")
    except ImportError:
        print("❌ schedule not found. Run: pip install schedule")
        return False
    
    return True

def test_config_files():
    """Test if configuration files exist and are valid JSON."""
    print("\n🔍 Testing configuration files...")
    
    config_files = ["twitter_config.json", "llm_config.json"]
    all_valid = True
    
    for config_file in config_files:
        if Path(config_file).exists():
            try:
                with open(config_file, 'r') as f:
                    json.load(f)
                print(f"✅ {config_file} exists and is valid JSON")
            except json.JSONDecodeError:
                print(f"❌ {config_file} exists but contains invalid JSON")
                all_valid = False
        else:
            print(f"❌ {config_file} not found")
            all_valid = False
    
    return all_valid

def test_script_files():
    """Test if all required script files exist."""
    print("\n🔍 Testing script files...")
    
    script_files = ["log.py", "post_daily_summary.py", "scheduler.py"]
    all_exist = True
    
    for script_file in script_files:
        if Path(script_file).exists():
            print(f"✅ {script_file} exists")
        else:
            print(f"❌ {script_file} not found")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests."""
    print("🚀 Log2Tweet Setup Test")
    print("=" * 40)
    
    # Run tests
    imports_ok = test_imports()
    configs_ok = test_config_files()
    scripts_ok = test_script_files()
    
    # Summary
    print("\n" + "=" * 40)
    print("📊 Test Results Summary:")
    print(f"  Package Imports: {'✅ PASS' if imports_ok else '❌ FAIL'}")
    print(f"  Configuration Files: {'✅ PASS' if configs_ok else '❌ FAIL'}")
    print(f"  Script Files: {'✅ PASS' if scripts_ok else '❌ FAIL'}")
    
    if imports_ok and configs_ok and scripts_ok:
        print("\n🎉 All tests passed! Log2Tweet is ready to use.")
        print("\nNext steps:")
        print("1. Configure your API keys in twitter_config.json and llm_config.json")
        print("2. Test logging: python log.py 'Test task'")
        print("3. Start scheduler: python scheduler.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("- Run: pip install -r requirements.txt")
        print("- Check that all files are in the correct directory")
        print("- Verify your configuration files have valid JSON")

if __name__ == "__main__":
    main()
