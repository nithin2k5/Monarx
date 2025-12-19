import psutil
import time
import os
from config import CPU_LIMIT, MEM_LIMIT, SWAP_LIMIT, CHECK_EVERY, COOLDOWN

last_alert = {}

def notify(title, msg):
    os.system(
        f"osascript -e 'display notification \"{msg}\" with title \"{title}\"'"
    )

def can_alert(key):
    now = time.time()
    if key not in last_alert or now - last_alert[key] > COOLDOWN:
        last_alert[key] = now
        return True
    return False

while True:
    try:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        swap = psutil.swap_memory().percent

        if cpu > CPU_LIMIT and can_alert("cpu"):
            notify("⚠️ High CPU Usage", f"CPU at {cpu:.1f}%")

        if mem > MEM_LIMIT and can_alert("mem"):
            notify("⚠️ High Memory Usage", f"RAM at {mem:.1f}%")

        if swap > SWAP_LIMIT and can_alert("swap"):
            notify("⚠️ Swap Usage", f"Swap at {swap:.1f}%")

    except Exception:
        pass

    time.sleep(CHECK_EVERY)

