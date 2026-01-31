import os


class Ensure():
    @staticmethod
    def _ensure_extension( path: str, ext: str) -> str:
        return path if path.endswith("." + ext) else f"{path}." + ext
    @staticmethod
    def ensure_csv( path: str) -> str:
        return Ensure._ensure_extension(path, "csv")
    @staticmethod
    def ensure_pdf( path: str) -> str:
        return Ensure._ensure_extension(path, "pdf")
    @staticmethod
    def ensure_not_dir(path: str) -> bool:
        return not os.path.isdir(path)