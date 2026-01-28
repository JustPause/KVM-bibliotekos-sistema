from typing import override
import pagrindinis


class MainClassGUI(pagrindinis.MainClass):
    @override
    def main(self):
        self.local_run()  
            
if __name__ == "__main__":
    app = MainClassGUI()
    app.main()