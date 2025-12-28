import wxformbuilder

class SideBar(wxformbuilder.SideBar): 
    def Click(self, event):
        print("Button was clicked!")
        # Do your logic here

        # Call this only if you want other handlers to run too
        event.Skip()
        

class Pagrindinis(wxformbuilder.Pagrindinis): 
    pass