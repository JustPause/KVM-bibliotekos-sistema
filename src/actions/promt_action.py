import sys

from src.etc.logger import logger


def show_prompt(prompt):
    """Specifically for the prompt library, to handle CTRL+C presses"""

    try:
        return prompt.execute()
    except KeyboardInterrupt:
        logger.info("\nIšeinama…")
        sys.exit(0)


def show_src_prompt(prompt):
    pass


def show_dest_prompt(prompt):
    pass
