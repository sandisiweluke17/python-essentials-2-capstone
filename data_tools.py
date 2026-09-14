from datetime import datetime


def generate_sample_data_file(filepath="data/students.txt"):
    """Creates a raw, slightly messy data file — this simulates 'real' input data."""
    raw_lines = [
        "  Lisa , S1 , 72 ",
        "tom,S2,45",
        " NOMVULA,S3,91",
        "Sipho , S4,  38 ",
        "  amahle,S5,67 ",
        "Kabelo,S6,55",
    ]
    with open(filepath, "w") as f:
        for line in raw_lines:
            f.write(line + "\n")
    return filepath


def load_and_clean_records(filepath="data/students.txt"):
    """Reads the raw file and returns a clean list of (name, student_id, score) tuples."""
    cleaned_records = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3:
                continue
            name = parts[0].strip().title()
            student_id = parts[1].strip().upper()
            try:
                score = int(parts[2].strip())
            except ValueError:
                continue
            cleaned_records.append((name, student_id, score))
    return cleaned_records


def export_results(content, filepath="data/report.txt"):
    """Writes a text report (e.g. analysis results) to a file."""
    with open(filepath, "w") as f:
        f.write(content)
    return filepath


def append_log(message, filepath="data/activity.log"):
    """Appends a timestamped line to a log file — never overwrites previous entries."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] {message}\n")