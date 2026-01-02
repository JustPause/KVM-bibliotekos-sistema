import os

def is_it_directory(output_pdf):
    if not os.path.exists(output_pdf):
        folder = os.path.dirname(output_pdf)
        os.makedirs(folder, exist_ok = True)

def is_file_empty(output_csv):
    file_exists = os.path.exists(output_csv)
    file_empty = True if (not file_exists) or os.path.getsize(output_csv) == 0 else False
    return file_empty

def git_build_number():
    import subprocess
    try:
        return subprocess.check_output(
            ["git", "rev-list", "--count", "HEAD"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        return "0"