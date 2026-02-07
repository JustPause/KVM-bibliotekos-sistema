from src.etc.logger import logger


class Progress:
    def __init__(self, total):
        self.step = 0
        self.total = total

    def progress(self, messige):
        self.step += 1
        logger.info(messige + " " + str(self.step) + "/" + str(self.total))
