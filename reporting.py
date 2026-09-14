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
        f"Current Working Directory: {os.getcwd()}",
    ]
    data_file = "data/students.txt"
    if os.path.exists(data_file):
        size = os.path.getsize(data_file)
        lines.append(f"data/students.txt exists: Yes ({size} bytes)")
    else:
        lines.append("data/students.txt exists: No")
    return "\n".join(lines)


def date_report(target_date_str=None):
    """Returns a string with the date, a timestamp, leap year/month facts, and a calendar."""
    now = datetime.now()
    day_name = calendar.day_name[now.weekday()]
    is_leap = calendar.isleap(now.year)
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    lines = [
        "=== DATE REPORT ===",
        f"Today's Date: {now.strftime('%Y-%m-%d')}",
        f"Day of the Week: {day_name}",
        f"Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Leap Year: {'Yes' if is_leap else 'No'}",
        f"Days in Current Month: {days_in_month}",
    ]

    if target_date_str:
        try:
            target = datetime.strptime(target_date_str, "%Y-%m-%d").date()
            days_until = (target - now.date()).days
            lines.append(f"Days Until {target_date_str}: {days_until}")
        except ValueError:
            lines.append("Invalid target date format (expected YYYY-MM-DD).")

    lines.append("")
    lines.append(calendar.month(now.year, now.month))
    return "\n".join(lines)