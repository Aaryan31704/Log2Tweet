#!/usr/bin/env python3
"""
Log2Tweet - Example Usage Script
Demonstrates how to use the logging functionality programmatically.
"""

from log import log_task, load_tasks
from datetime import datetime

def run_example():
    """Run example logging operations."""
    print("🚀 Log2Tweet Example Usage")
    print("=" * 40)
    
    # Example 1: Log a coding task
    print("\n📝 Example 1: Logging a coding task")
    log_task("Implemented user authentication with JWT tokens")
    
    # Example 2: Log a learning task
    print("\n📚 Example 2: Logging a learning task")
    log_task("Completed React hooks tutorial on useEffect")
    
    # Example 3: Log a bug fix
    print("\n🐛 Example 3: Logging a bug fix")
    log_task("Fixed CSS grid layout issue on mobile devices")
    
    # Show all tasks
    print("\n📋 Current Tasks:")
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task['description']}")
        print(f"     📅 {task['date']} ⏰ {task['timestamp']}")
    
    print(f"\n✅ Total tasks logged: {len(tasks)}")
    print("\n💡 Now you can run 'python post_daily_summary.py' to test the summary generation!")

if __name__ == "__main__":
    run_example()
