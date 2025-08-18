#!/usr/bin/env python3
"""
Log2Tweet - Daily Summary Posting Script
Reads logged tasks, generates a summary using LLM, and posts to Twitter.
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
import tweepy
import google.generativeai as genai
from typing import List, Dict, Optional

# LLM Prompt for generating daily summary
DAILY_SUMMARY_PROMPT = """
Create a concise, engaging tweet summarizing today's work progress.

Requirements:
- MAXIMUM 280 characters (Twitter limit)
- Use encouraging, positive tone
- Include 2-3 relevant emojis
- Be specific but brief
- Make it feel personal and motivational

Today's tasks:
{tasks_list}

Generate a SHORT tweet (under 280 chars) that captures today's progress:
"""

def load_config(config_file: str) -> Dict:
    """Load configuration from JSON file."""
    config_path = Path(config_file)
    if not config_path.exists():
        print(f"Error: {config_file} not found")
        sys.exit(1)
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {config_file}")
        sys.exit(1)

def load_tasks() -> List[Dict]:
    """Load tasks from tasks.json file."""
    tasks_file = Path("tasks.json")
    if not tasks_file.exists():
        print("No tasks.json file found. Nothing to summarize.")
        return []
    
    try:
        with open(tasks_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Invalid JSON in tasks.json")
        return []

def get_todays_tasks(tasks: List[Dict]) -> List[Dict]:
    """Filter tasks to only include today's entries."""
    today = datetime.now().strftime("%Y-%m-%d")
    return [task for task in tasks if task.get('date') == today]

def generate_summary_with_llm(tasks: List[Dict], llm_config: Dict) -> str:
    """Generate daily summary using Google Gemma API."""
    if not tasks:
        return "No tasks completed today. Time to get started! 💪"
    
    # Format tasks for the prompt
    tasks_text = "\n".join([f"• {task['description']}" for task in tasks])
    
    try:
        # Try Gemma API first
        if 'gemma_api_key' in llm_config and llm_config['gemma_api_key']:
            # Configure Gemma API
            genai.configure(api_key=llm_config['gemma_api_key'])
            
            # Get the model
            model = genai.GenerativeModel(llm_config.get('model', 'gemma-2-9b-it'))
            
            # Generate content
            response = model.generate_content(
                DAILY_SUMMARY_PROMPT.format(tasks_list=tasks_text),
                generation_config=genai.types.GenerationConfig(
                    temperature=llm_config.get('temperature', 0.7),
                    max_output_tokens=llm_config.get('max_tokens', 1000)
                )
            )
            
            # Handle different response formats
            if hasattr(response, 'text'):
                return response.text.strip()
            elif hasattr(response, 'parts') and response.parts:
                # Handle complex responses with multiple parts
                text_parts = []
                for part in response.parts:
                    if hasattr(part, 'text'):
                        text_parts.append(part.text)
                return ' '.join(text_parts).strip()
            elif hasattr(response, 'candidates') and response.candidates:
                # Handle candidate-based responses
                candidate = response.candidates[0]
                if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                    text_parts = []
                    for part in candidate.content.parts:
                        if hasattr(part, 'text'):
                            text_parts.append(part.text)
                    return ' '.join(text_parts).strip()
            else:
                # Fallback to string representation
                return str(response).strip()
        
        # Fallback to a simple template if no API key
        else:
            return generate_fallback_summary(tasks)
            
    except Exception as e:
        print(f"Warning: Gemma API call failed: {e}")
        print("Using fallback summary generation...")
        return generate_fallback_summary(tasks)

def generate_fallback_summary(tasks: List[Dict]) -> str:
    """Generate a simple summary without external LLM API."""
    if not tasks:
        return "No tasks completed today. Time to get started! 💪"
    
    task_count = len(tasks)
    first_task = tasks[0]['description']
    
    if task_count == 1:
        return f"✅ Completed: {first_task[:50]}{'...' if len(first_task) > 50 else ''} #Productivity #Progress"
    else:
        return f"�� Made progress on {task_count} tasks today! Including: {first_task[:30]}{'...' if len(first_task) > 30 else ''} #DailyProgress #Productivity"

def post_to_twitter(summary: str, twitter_config: Dict) -> bool:
    """Post summary to Twitter using Tweepy API v2."""
    try:
        # Use Twitter API v2
        client = tweepy.Client(
            consumer_key=twitter_config['consumer_key'],
            consumer_secret=twitter_config['consumer_secret'],
            access_token=twitter_config['access_token'],
            access_token_secret=twitter_config['access_token_secret']
        )
        
        # Post the tweet using v2
        response = client.create_tweet(text=summary)
        print(f"✅ Tweet posted successfully!")
        print(f"Tweet ID: {response.data['id']}")
        return True
        
    except Exception as e:
        print(f"Error posting to Twitter: {e}")
        return False

def clear_tasks():
    """Clear tasks.json file for the next day."""
    try:
        with open("tasks.json", 'w', encoding='utf-8') as f:
            json.dump([], f)
        print("🧹 Cleared tasks.json for tomorrow")
    except Exception as e:
        print(f"Warning: Could not clear tasks.json: {e}")

def main():
    """Main function to run the daily summary process."""
    print("🔄 Starting daily summary generation...")
    
    # Load configurations
    try:
        twitter_config = load_config("twitter_config.json")
        llm_config = load_config("llm_config.json")
    except SystemExit:
        return
    
    # Load and filter today's tasks
    all_tasks = load_tasks()
    todays_tasks = get_todays_tasks(all_tasks)
    
    if not todays_tasks:
        print("📝 No tasks found for today. Nothing to summarize.")
        return
    
    print(f"📋 Found {len(todays_tasks)} tasks for today")
    
    # Generate summary
    print("🤖 Generating summary with Gemma...")
    summary = generate_summary_with_llm(todays_tasks, llm_config)
    
    print(f"📝 Generated summary: {summary}")
    print(f"📏 Character count: {len(summary)}")
    
    # Check character limit and truncate if needed
    if len(summary) > 280:
        print("⚠️  Warning: Summary exceeds Twitter's 280 character limit")
        print(f"📏 Original length: {len(summary)}")
        summary = summary[:277] + "..."
        print(f"📏 Truncated to: {len(summary)} characters")
        print(f"📝 Final summary: {summary}")
    
    # Post to Twitter
    print("🐦 Posting to Twitter...")
    if post_to_twitter(summary, twitter_config):
        print("🎉 Daily summary posted successfully!")
        
        # Clear tasks for next day
        clear_tasks()
    else:
        print("❌ Failed to post to Twitter. Tasks not cleared.")

if __name__ == "__main__":
    main()
