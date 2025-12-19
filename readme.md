1. clone the repo 
    mkdir -p ~/tools/mac-monitor
    cd ~/tools/mac-monitor
2. Create virtual environment
    python3 -m venv .venv
    source .venv/bin/activate
3. Install dependencies
    pip install -r requirements.txt

Configuration
Edit config.py


Run Manually (foreground)

source .venv/bin/activate
python mac_monitor.py



Stop / Disable

launchctl unload ~/Library/LaunchAgents/com.dinesh.macmonitor.plist

Remove permanently:

rm ~/Library/LaunchAgents/com.dinesh.macmonitor.plist

