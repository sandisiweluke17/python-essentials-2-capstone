import platform
import os
from datetime import datetime
import calendar


def environment_report():
    """Returns a string describing the system this program is running on."""
    lines = [
        "=== ENVIRONMENT REPORT ===",
        f"Operating System: {platform.system()} {platform.release()}",
        f"Python Version: {platform.python_version()}",
        f"Machine Type: {platform.machine()}",
        f"Current Working Directory: {os.getcwd()}",
    ]
    return "\n".join(lines)


def date_report():
    """Returns a string with the current date, day name, and a small calendar."""
    now = datetime.now()
    day_name = calendar.day_name[now.weekday()]
    month_calendar = calendar.month(now.year, now.month)

    lines = [
        "=== DATE REPORT ===",
        f"Today's Date: {now.strftime('%Y-%m-%d')}",
        f"Day of the Week: {day_name}",
        f"Time: {now.strftime('%H:%M:%S')}",
        "",
        month_calendar,
    ]
    return "\n".join(lines)