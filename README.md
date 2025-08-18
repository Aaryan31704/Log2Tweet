# Log2Tweet 🚀

A Python side-project that logs your daily work sessions and automatically posts a friendly summary to Twitter every day at 23:50 using Google Gemini AI.

## ✨ Features

- **Simple Task Logging**: Log individual work sessions with timestamps
- **Automatic Daily Summaries**: Runs every day at 23:50 PM
- **AI-Powered Summaries**: Uses Google Gemini to generate engaging tweet-style summaries
- **Twitter Integration**: Automatically posts summaries using Twitter API v2
- **Lightweight Scheduler**: Uses the `schedule` package for automation

## 🏗️ Project Structure

```
log2tweet/
├── log.py                       # Script to log individual work sessions
├── post_daily_summary.py        # Auto-post script (called by scheduler)
├── scheduler.py                 # Runs post_daily_summary.py at 23:50 everyday
├── tasks.json                   # Stores logged sessions
├── twitter_config.json          # For API keys/tokens (create from template)
├── llm_config.json              # For LLM API key / endpoint (create from template)
├── twitter_config_template.json # Template for Twitter config
├── llm_config_template.json     # Template for LLM config
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # This file
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Aaryan31704/Log2Tweet.git
cd Log2Tweet/log2tweet
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# OR Activate it (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

#### Twitter Configuration
1. Go to [Twitter Developer Portal](https://developer.twitter.com/)
2. Create a new app and get your API keys
3. Copy `twitter_config_template.json` to `twitter_config.json`
4. Edit `twitter_config.json` and add your credentials:

```json
{
  "consumer_key": "YOUR_ACTUAL_CONSUMER_KEY",
  "consumer_secret": "YOUR_ACTUAL_CONSUMER_SECRET",
  "access_token": "YOUR_ACTUAL_ACCESS_TOKEN",
  "access_token_secret": "YOUR_ACTUAL_ACCESS_TOKEN_SECRET"
}
```

#### LLM Configuration (Google Gemini)
1. Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Copy `llm_config_template.json` to `llm_config.json`
3. Edit `llm_config.json` and add your API key:

```json
{
  "gemini_api_key": "YOUR_ACTUAL_GEMINI_API_KEY",
  "model": "gemini-pro",
  "max_tokens": 100,
  "temperature": 0.7
}
```

### 5. Start Logging Tasks
```bash
# Log a single task
python log.py "LeetCode – Two Sum"

# Log a task with spaces (use quotes)
python log.py "Completed React component refactoring"

# Log multiple words as one task
python log.py "Bug fix in authentication module"
```

### 6. Test Summary Generation
```bash
# Test the AI summary generation
python post_daily_summary.py
```

### 7. Start the Scheduler (Optional)
```bash
# Start the scheduler (will run daily at 23:50)
python scheduler.py
```

## 📖 Usage Examples

### Logging Tasks
```bash
# Log coding tasks
python log.py "Implemented user authentication system"
python log.py "Fixed CSS layout issues"
python log.py "Added unit tests for API endpoints"

# Log learning tasks
python log.py "Studied React hooks and context"
python log.py "Completed AWS certification module"
python log.py "Read Clean Code chapter 3"
```

### Manual Summary Generation
If you want to generate and post a summary manually (without waiting for 23:50):
```bash
python post_daily_summary.py
```

## ⚙️ How It Works

1. **Task Logging**: `log.py` appends task descriptions with timestamps to `tasks.json`
2. **Daily Summary**: At 23:50, `scheduler.py` triggers `post_daily_summary.py`
3. **AI Processing**: The script reads today's tasks and sends them to Google Gemini
4. **Tweet Generation**: Gemini creates a friendly, motivational summary tweet
5. **Twitter Posting**: The summary is posted to Twitter using Twitter API v2
6. **Cleanup**: `tasks.json` is cleared for the next day

## 🔧 Configuration Options

### LLM Prompt Customization
The LLM prompt is defined in `post_daily_summary.py` as `DAILY_SUMMARY_PROMPT`. You can modify this to change the style and tone of your summaries.

### Scheduling Time
To change the daily posting time, edit `scheduler.py` and modify this line:
```python
schedule.every().day.at("23:50").do(run_daily_summary)
```

### Fallback Summary
If the Gemini API fails, the system generates a simple fallback summary. You can customize this in the `generate_fallback_summary()` function.

## 🚨 Troubleshooting

### Common Issues
1. **Twitter API Errors**: Check your API keys and ensure your Twitter app has write permissions
2. **Gemini API Errors**: Verify your API key and check your usage limits
3. **Scheduler Not Running**: Make sure you're running `scheduler.py` and it's not being interrupted

### Testing
- Test task logging: `python log.py "Test task"`
- Test summary generation: `python post_daily_summary.py`
- Test Twitter posting: Ensure your API keys are correct

## 📝 Notes

- The system automatically truncates summaries that exceed Twitter's 280 character limit
- Tasks are stored with ISO format timestamps for precise tracking
- The scheduler runs continuously and should be kept running for daily automation
- All configuration is stored in JSON files for easy editing
- **Important**: Never commit your actual API keys to Git!

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve Log2Tweet!

## 📄 License

This project is open source and available under the MIT License.
