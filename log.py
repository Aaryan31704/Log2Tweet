#!/usr/bin/env python3
"""
Log2Tweet - Task Logging Script
Logs individual work sessions with timestamps for daily summary generation.
"""

import json
import sys
import os
from datetime import datetime
from pathlib import Path

def load_tasks():
    """Load existing tasks from tasks.json file."""
    tasks_file = Path("tasks.json")
    if tasks_file.exists():
        try:
            with open(tasks_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_tasks(tasks):
    """Save tasks to tasks.json file."""
    with open("tasks.json", 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def log_task(description):
    """Log a new task with current timestamp."""
    if not description.strip():
        print("Error: Task description cannot be empty")
        return False
    
    tasks = load_tasks()
    
    new_task = {
        "description": description.strip(),
        "timestamp": datetime.now().isoformat(),
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    
    print(f"✅ Logged: {description}")
    print(f"📅 Date: {new_task['date']}")
    print(f"⏰ Time: {new_task['timestamp']}")
    return True

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python log.py \"Task description\"")
        print("Example: python log.py \"LeetCode – Two Sum\"")
        sys.exit(1)
    
    # Join all arguments as the task description
    task_description = " ".join(sys.argv[1:])
    
    if log_task(task_description):
        print(f"\n📝 Total tasks logged today: {len([t for t in load_tasks() if t['date'] == datetime.now().strftime('%Y-%m-%d')])}")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
