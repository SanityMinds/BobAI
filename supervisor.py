import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


BOT_PATH = Path(__file__).with_name("bot.py")
SUPERVISOR_LOG_PATH = BOT_PATH.with_name("supervisor.log")
RESTART_DELAY_SECONDS = 5

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(message)s",
    handlers=[
        RotatingFileHandler(
            SUPERVISOR_LOG_PATH,
            maxBytes=2 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8",
        ),
        logging.StreamHandler(),
    ],
)

stopping = False
child_process = None


def request_shutdown(signum, frame):
    del signum, frame
    global stopping
    stopping = True
    if child_process is not None and child_process.poll() is None:
        child_process.terminate()


signal.signal(signal.SIGINT, request_shutdown)
signal.signal(signal.SIGTERM, request_shutdown)
if hasattr(signal, "SIGBREAK"):
    signal.signal(signal.SIGBREAK, request_shutdown)


while not stopping:
    logging.info("Starting Discord process.")
    child_env = os.environ.copy()
    child_env["PYTHONUNBUFFERED"] = "1"
    try:
        child_process = subprocess.Popen(
            [sys.executable, str(BOT_PATH)],
            cwd=str(BOT_PATH.parent),
            env=child_env,
        )
    except Exception:
        logging.exception(
            "Failed to start Discord process; retrying in %s seconds.",
            RESTART_DELAY_SECONDS,
        )
        time.sleep(RESTART_DELAY_SECONDS)
        continue

    exit_code = child_process.wait()

    if stopping:
        break

    logging.warning(
        "Discord process exited with code %s; restarting in %s seconds.",
        exit_code,
        RESTART_DELAY_SECONDS,
    )
    time.sleep(RESTART_DELAY_SECONDS)

logging.info("Supervisor stopped.")
