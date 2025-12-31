import sys
import pagrindinis


class MainClassGUI(pagrindinis.MainClass):
    def main(self):
        argv = sys.argv[1:]
        if '--console' in argv:
            self.prompting()  # console mode
        else:
            self.local_run()  
            
if __name__ == "__main__":
    app = MainClassGUI()
    app.main()