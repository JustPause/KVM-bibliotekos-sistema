import sys
import pagrindinis


class MainClassGUI(pagrindinis.MainClass):
    def main(self):
        self.local_run()  
            
if __name__ == "__main__":
    app = MainClassGUI()
    app.main()