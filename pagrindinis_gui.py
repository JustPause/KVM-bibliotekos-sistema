import sys
from pagrindinis import MainClass


class MainClassGUI(MainClass):
    def main(self):
        argv = sys.argv[1:]
        argv_count= len(argv)

        if '--console' in argv:
            self.prompting()
        else:
            self.run()