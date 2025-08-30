# 🚀 Log2Tweet Dashboard

A modern web interface to monitor and control your Log2Tweet system.

## ✨ Features

- **🏠 Dashboard**: System overview and status
- **📊 Tasks**: View recent logged tasks
- **⚙️ Settings**: Control scheduler and check configurations
- **📝 Manual Control**: Run daily summaries manually

## �� Quick Start

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Start Dashboard
```bash
python -m streamlit run dashboard.py
```

Or use the provided scripts:
- **Windows**: Double-click `start_dashboard.bat`
- **PowerShell**: Run `start_dashboard.ps1`

### 3. Access Dashboard
- Opens automatically in your browser
- Usually at `http://localhost:8501`

## 🎯 How to Use

### Dashboard Page
- View system status at a glance
- Check configuration file status
- Quick actions for common tasks

### Tasks Page
- View tasks from the last 7 days (adjustable)
- Tasks grouped by date
- Expandable task details

### Settings Page
- Start/stop the scheduler
- Check configuration file status
- System information

### Manual Control Page
- Run daily summary manually
- View execution results
- Check current system status

## 🔧 Troubleshooting

### Dashboard won't start
- Make sure Python is installed
- Install requirements: `pip install -r requirements.txt`
- Check if port 8501 is available

### Configuration errors
- Ensure all config files exist
- Check file permissions
- Verify JSON format is correct

## 📱 Access from Other Devices

The dashboard runs on your local network. To access from other devices:
1. Find your computer's IP address
2. Access: `http://YOUR_IP:8501`
3. Make sure firewall allows connections

## 🛑 Stopping the Dashboard

- **In browser**: Close the tab
- **In terminal**: Press `Ctrl+C`
- **Background**: Close the terminal window

## 🔄 Auto-Start (Optional)

To make the dashboard start automatically:
1. Use Windows Task Scheduler
2. Set to run at startup
3. Point to `start_dashboard.bat`

## 📊 Requirements

- Python 3.7+
- Streamlit 1.29.0+
- All existing Log2Tweet dependencies