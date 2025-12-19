# Mac Monitor
A lightweight macOS system resource monitor that sends native notifications when CPU, memory, or swap usage exceeds configurable thresholds.

## Features
- **Real-time Monitoring** — Continuously monitors CPU, memory, and swap usage
- **Native Notifications** — Uses macOS notification center for alerts
- **Configurable Thresholds** — Easily customize alert limits
- **Cooldown System** — Prevents notification spam with configurable cooldown periods
- **Lightweight** — Minimal resource footprint using `psutil`

## Requirements

- macOS
- Python 3.x
- `psutil` library

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/username/mac-monitor.git
cd mac-monitor
```

Or create the directory manually:

```bash
mkdir -p ~/tools/mac-monitor
cd ~/tools/mac-monitor
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Edit `config.py` to customize the monitoring thresholds:

| Setting       | Default | Description                                      |
|---------------|---------|--------------------------------------------------|
| `CPU_LIMIT`   | 85%     | Alert when CPU usage exceeds this percentage     |
| `MEM_LIMIT`   | 70%     | Alert when memory usage exceeds this percentage  |
| `SWAP_LIMIT`  | 20%     | Alert when swap usage exceeds this percentage    |
| `CHECK_EVERY` | 10s     | Interval between checks (in seconds)             |
| `COOLDOWN`    | 120s    | Minimum time between repeated alerts (in seconds)|

**Example `config.py`:**

```python
CPU_LIMIT = 85        # %
MEM_LIMIT = 70        # %
SWAP_LIMIT = 20       # %

CHECK_EVERY = 10      # seconds
COOLDOWN = 120        # seconds
```

---

## Usage

### Run Manually (Foreground)

```bash
source .venv/bin/activate
python mac_monitor.py
```

### Run as Background Process

```bash
source .venv/bin/activate
nohup python mac_monitor.py > monitor.log 2> monitor.err &
```

### Run as a Launch Agent (Auto-start on Login)

1. Create a plist file at `~/Library/LaunchAgents/com.username.macmonitor.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.username.macmonitor</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/username/tools/mac-monitor/.venv/bin/python</string>
        <string>/Users/username/tools/mac-monitor/mac_monitor.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/username/tools/mac-monitor/monitor.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/username/tools/mac-monitor/monitor.err</string>
</dict>
</plist>
```

2. Load the launch agent:

```bash
launchctl load ~/Library/LaunchAgents/com.username.macmonitor.plist
```

---

## Stop / Disable

### Stop the Launch Agent

```bash
launchctl unload ~/Library/LaunchAgents/com.username.macmonitor.plist
```

### Remove Permanently

```bash
rm ~/Library/LaunchAgents/com.username.macmonitor.plist
```

### Stop Background Process

```bash
pkill -f mac_monitor.py
```

---

## Project Structure

```
mac-monitor/
├── mac_monitor.py      # Main monitoring script
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── monitor.log         # Standard output logs
├── monitor.err         # Error logs
└── README.md           # This file
```

---

## Notification Examples

When thresholds are exceeded, you'll receive native macOS notifications:

- **High CPU Usage** — "CPU at 92.5%"
- **High Memory Usage** — "RAM at 85.3%"
- **Swap Usage** — "Swap at 45.0%"


## License

This project is open source and available under the [MIT License](LICENSE).

---
