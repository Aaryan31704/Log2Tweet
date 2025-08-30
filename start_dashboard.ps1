Write-Host "Starting Log2Tweet Streamlit Dashboard..." -ForegroundColor Green
Write-Host ""
Write-Host "Dashboard will open in your browser automatically." -ForegroundColor Cyan
Write-Host "Keep this window open to keep the dashboard running." -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the dashboard." -ForegroundColor Red
Write-Host ""

# Check if Python is available
try {
    python --version
} catch {
    Write-Host "Error: Python not found. Please install Python and try again." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Start the dashboard
python -m streamlit run dashboard.py

Read-Host "Press Enter to exit"