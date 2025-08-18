# Log2Tweet Scheduler Starter Script
Write-Host "🚀 Starting Log2Tweet Scheduler..." -ForegroundColor Green
Write-Host ""
Write-Host "This will run the daily summary posting at 23:50 every day." -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the scheduler." -ForegroundColor Yellow
Write-Host ""

try {
    python scheduler.py
}
catch {
    Write-Host "❌ Error starting scheduler: $_" -ForegroundColor Red
}

Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
