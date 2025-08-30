#!/usr/bin/env python3
"""
Log2Tweet - Simple Task Logger
A minimal interface to log tasks and post daily summaries.
"""

import streamlit as st
import json
from datetime import datetime
from pathlib import Path
import subprocess
import sys
import os

# Page configuration
st.set_page_config(
    page_title="Log2Tweet",
    page_icon="📝",
    layout="wide"
)

class TaskLogger:
    """Simple task logging functionality."""
    
    def __init__(self):
        self.config_dir = Path(__file__).parent
        self.tasks_file = self.config_dir / "tasks.json"
        
    def log_task(self, description: str, notes: str = "") -> dict:
        """Log a new task."""
        try:
            if not self.tasks_file.exists():
                with open(self.tasks_file, 'w', encoding='utf-8') as f:
                    json.dump([], f)
            
            with open(self.tasks_file, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
            
            new_task = {
                "description": description,
                "notes": notes,
                "time": datetime.now().strftime("%H:%M"),
                "date": datetime.now().strftime("%Y-%m-%d"),
                "timestamp": datetime.now().isoformat()
            }
            
            tasks.insert(0, new_task)
            
            with open(self.tasks_file, 'w', encoding='utf-8') as f:
                json.dump(tasks, f, indent=2, ensure_ascii=False)
            
            return {"success": True, "message": "Task logged successfully"}
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def post_summary(self) -> dict:
        """Post daily summary."""
        try:
            post_script = self.config_dir / "post_daily_summary.py"
            if not post_script.exists():
                return {"success": False, "error": "post_daily_summary.py not found"}
            
            # First try with proper encoding
            try:
                # Set environment variables for proper encoding on Windows
                env = os.environ.copy()
                env['PYTHONIOENCODING'] = 'utf-8'
                env['PYTHONLEGACYWINDOWSSTDIO'] = 'utf-8'
                
                result = subprocess.run(
                    [sys.executable, str(post_script)],
                    capture_output=True,
                    text=True,
                    cwd=self.config_dir,
                    env=env,
                    encoding='utf-8',
                    errors='replace'
                )
                
                if result.returncode == 0:
                    return {
                        "success": True,
                        "output": result.stdout.strip(),
                        "message": "Summary posted successfully"
                    }
                else:
                    return {
                        "success": False,
                        "error": result.stderr.strip(),
                        "message": "Failed to post summary"
                    }
            
            except UnicodeError:
                # Fallback: run without capturing output to avoid encoding issues
                result = subprocess.run(
                    [sys.executable, str(post_script)],
                    cwd=self.config_dir
                )
                
                if result.returncode == 0:
                    return {
                        "success": True,
                        "output": "Summary posted successfully (output not captured due to encoding)",
                        "message": "Summary posted successfully"
                    }
                else:
                    return {
                        "success": False,
                        "error": "Script failed to run",
                        "message": "Failed to post summary"
                    }
                
        except Exception as e:
            return {"success": False, "error": str(e)}

# Initialize task logger
logger = TaskLogger()

def main():
    """Main application."""
    st.title("Log2Tweet")
    st.write("Log your daily tasks and post summaries")
    
    # Task logging
    st.header("Log Task")
    
    task_description = st.text_input("What did you accomplish?", placeholder="Enter task description...")
    task_notes = st.text_area("Additional notes (optional)", placeholder="Any extra details...")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Log Task", type="primary", use_container_width=True):
            if task_description.strip():
                result = logger.log_task(task_description.strip(), task_notes.strip())
                if result['success']:
                    st.success("Task logged!")
                    st.rerun()
                else:
                    st.error(f"Error: {result.get('error', 'Unknown error')}")
            else:
                st.warning("Please enter a task description")
    
    with col2:
        if st.button("Post Summary", use_container_width=True):
            with st.spinner("Posting summary..."):
                result = logger.post_summary()
            
            if result['success']:
                st.success("Summary posted!")
                if result.get('output'):
                    st.info("Output:")
                    st.code(result['output'])
            else:
                st.error(f"Failed: {result.get('error', 'Unknown error')}")
    
    # Recent tasks
    st.header("Recent Tasks")
    
    if logger.tasks_file.exists():
        try:
            with open(logger.tasks_file, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
            
            if tasks:
                for task in tasks[:10]:  # Show last 10 tasks
                    with st.expander(f"{task.get('description', 'No description')} - {task.get('date', 'No date')}"):
                        st.write(f"**Time:** {task.get('time', 'No time')}")
                        if task.get('notes'):
                            st.write(f"**Notes:** {task['notes']}")
            else:
                st.info("No tasks logged yet.")
        except Exception as e:
            st.error(f"Error loading tasks: {e}")
    else:
        st.info("No tasks file found. Log your first task to get started!")

if __name__ == "__main__":
    main()