import os


def is_it_directory(output_pdf):
    if not os.path.exists(output_pdf):
        folder = os.path.dirname(output_pdf)
        os.makedirs(folder, exist_ok=True)


def is_file_empty(output_csv):
    file_exists = os.path.exists(output_csv)
    file_empty = (
        True if (not file_exists) or os.path.getsize(output_csv) == 0 else False
    )
    return file_empty


def git_build_number():
    import subprocess

    try:
        return (
            subprocess.check_output(
                ["git", "rev-list", "--count", "HEAD"], stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )
    except Exception:
        return "0"


def get_correct_extension(path, ending):
    path = str(path)

    if not path.endswith(ending):
        if "." in os.path.basename(path):
            path = path.rsplit(".", 1)[0]
        path += ending

    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    return path


def get_correct_extension_ending(path: str, ending: str):
    if not path.endswith(ending):
        if "." in os.path.basename(path):
            path = path.rsplit(".", 1)[0]
        path = path + "." + ending
    return path


def is_it_an_validate_path(path):
    return os.path.isfile(path)
