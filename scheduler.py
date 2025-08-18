#!/usr/bin/env python3
"""
Log2Tweet - Scheduler Script
Runs the daily summary posting script at 23:50 every day.
"""

import schedule
import time
import subprocess
import sys
from datetime import datetime
from pathlib import Path

def run_daily_summary():
    """Run the daily summary posting script."""
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Running daily summary...")
    
    try:
        # Get the directory where this script is located
        script_dir = Path(__file__).parent
        post_script = script_dir / "post_daily_summary.py"
        
        if not post_script.exists():
            print(f"❌ Error: {post_script} not found")
            return
        
        # Run the post_daily_summary.py script
        result = subprocess.run(
            [sys.executable, str(post_script)],
            capture_output=True,
            text=True,
            cwd=script_dir
        )
        
        if result.returncode == 0:
            print("✅ Daily summary completed successfully")
            if result.stdout:
                print("📝 Output:", result.stdout.strip())
        else:
            print(f"❌ Daily summary failed with return code {result.returncode}")
            if result.stderr:
                print("🚨 Error:", result.stderr.strip())
                
    except Exception as e:
        print(f"❌ Error running daily summary: {e}")

def main():
    """Main scheduler function."""
    print("🚀 Log2Tweet Scheduler Starting...")
    print(f"📅 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("⏰ Will run daily summary at 23:50 every day")
    print("💡 Press Ctrl+C to stop the scheduler")
    print("-" * 50)
    
    # Schedule the daily summary to run at 23:50
    schedule.every().day.at("23:50").do(run_daily_summary)
    
    # Also run once immediately if it's after 23:50 (for testing)
    current_hour = datetime.now().hour
    current_minute = datetime.now().minute
    if current_hour == 23 and current_minute >= 50:
        print("🕐 It's after 23:50, running summary now...")
        run_daily_summary()
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
            
    except KeyboardInterrupt:
        print("\n🛑 Scheduler stopped by user")
        print("👋 Goodbye!")

if __name__ == "__main__":
    main()
