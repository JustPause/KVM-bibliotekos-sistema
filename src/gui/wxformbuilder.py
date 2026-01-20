# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.dataview

import gettext
_ = gettext.gettext

###########################################################################
## Class SideBar
###########################################################################

class SideBar ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 256,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        sideLayout = wx.BoxSizer( wx.VERTICAL )

        titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )
        self.Titulas_Barkodas.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        sideLayout.Add( titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        sideNavigsionLayout = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )
        self.Barkodai.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        sideNavigsionLayout.Add( self.Barkodai, 0, wx.ALL, 5 )

        BarkodaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.Button( self, wx.ID_ANY, _(u"ISBN kodu atspauždinimas"), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE|wx.BU_EXACTFIT )
        self.ISNB_kodu_atspauzdinimas.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        BarkodaiLayout.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.BOTTOM, 5 )

        self.Kurti_naujus_barkodus = wx.Button( self, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE|wx.BU_EXACTFIT )
        self.Kurti_naujus_barkodus.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        BarkodaiLayout.Add( self.Kurti_naujus_barkodus, 0, wx.BOTTOM, 5 )


        sideNavigsionLayout.Add( BarkodaiLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 25), 0, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )
        self.Knygu_surašimas.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        sideNavigsionLayout.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        KnyguLayout = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.Button( self, wx.ID_ANY, _(u"Klaviatūros / Skaitytuvo"), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE|wx.BU_EXACTFIT )
        self.Iš_Klavetūros_Skaitytuvo.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        KnyguLayout.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.BOTTOM, 5 )

        self.CSV_Sukurimas = wx.Button( self, wx.ID_ANY, _(u"CSV lenteles sukurimas"), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE|wx.BU_EXACTFIT|wx.BORDER_NONE )
        self.CSV_Sukurimas.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        KnyguLayout.Add( self.CSV_Sukurimas, 0, wx.BOTTOM, 5 )

        self.Iš_CSV = wx.Button( self, wx.ID_ANY, _(u"CSV duomenu perkelimas"), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE|wx.BU_EXACTFIT|wx.BORDER_NONE )
        self.Iš_CSV.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        KnyguLayout.Add( self.Iš_CSV, 0, wx.BOTTOM, 5 )


        sideNavigsionLayout.Add( KnyguLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 25), 0, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )
        self.Patikrinimas.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Patikralentėja = wx.Button( self, wx.ID_ANY, _(u"Google sheets lentėje"), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE|wx.BU_EXACTFIT )
        self.Patikralentėja.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        PatikrinimasLayout.Add( self.Patikralentėja, 0, wx.BOTTOM, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 25), 0, wx.EXPAND, 5 )

        self.Uzrasimas = wx.StaticText( self, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Uzrasimas.Wrap( -1 )

        self.Uzrasimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )
        self.Uzrasimas.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        sideNavigsionLayout.Add( self.Uzrasimas, 0, wx.ALL, 5 )

        UzrasimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Išdavimas = wx.Button( self, wx.ID_ANY, _(u"Išdavimas"), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE|wx.BU_EXACTFIT )
        self.Išdavimas.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        UzrasimasLayout.Add( self.Išdavimas, 0, wx.BOTTOM, 5 )

        self.Grąžinimas = wx.Button( self, wx.ID_ANY, _(u"Grąžinimas"), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE|wx.BU_EXACTFIT )
        self.Grąžinimas.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        UzrasimasLayout.Add( self.Grąžinimas, 0, wx.BOTTOM, 5 )


        sideNavigsionLayout.Add( UzrasimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 200), 1, wx.EXPAND, 5 )

        self.versija = wx.StaticText( self, wx.ID_ANY, _(u"Version 0.1 build 2026-01-01"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.versija.Wrap( -1 )

        self.versija.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.versija.SetForegroundColour( wx.Colour( 16, 16, 16 ) )

        sideNavigsionLayout.Add( self.versija, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.SetSizer( sideLayout )
        self.Layout()

        # Connect Events
        self.ISNB_kodu_atspauzdinimas.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Kurti_naujus_barkodus.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Iš_Klavetūros_Skaitytuvo.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.CSV_Sukurimas.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Iš_CSV.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Patikralentėja.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Išdavimas.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Grąžinimas.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.versija.Bind( wx.EVT_LEFT_UP, self.version )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def Click( self, event ):
        event.Skip()








    def version( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class Pagrindinis
###########################################################################

class Pagrindinis ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )

        arrowLayout = wx.GridSizer( 0, 2, 0, 0 )

        self.Arrow = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( self.img_path( u"img/Vector.png" ), wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Arrow.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        arrowLayout.Add( self.Arrow, 0, wx.TOP, 160 )


        mainLayout.Add( arrowLayout, 0, wx.LEFT, 25 )

        self.arrowText = wx.StaticText( self, wx.ID_ANY, _(u"Pasirinkite kategorija"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.arrowText.Wrap( -1 )

        self.arrowText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        mainLayout.Add( self.arrowText, 0, wx.LEFT, 245 )


        self.SetSizer( mainLayout )
        self.Layout()

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class KurtiNaujusBarkodus
###########################################################################

class KurtiNaujusBarkodus ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.mainWindowPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        layout = wx.BoxSizer( wx.VERTICAL )

        title_layout = wx.BoxSizer( wx.VERTICAL )

        self.title = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.title.Wrap( -1 )

        self.title.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        title_layout.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( title_layout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        input1_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.staticText1 = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Kur isaugoti norimus failus (PDF)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText1.Wrap( -1 )

        input1_layout.Add( self.staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        input1_layout.Add( ( 16, 0), 0, 0, 5 )

        self.inputText1 = wx.TextCtrl( self.mainWindowPanel, wx.ID_ANY, _(u"/"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.inputText1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.inputText1.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        input1_layout.Add( self.inputText1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        layout.Add( input1_layout, 0, 0, 5 )


        layout.Add( ( 0, 16), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        input2_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.staticText2 = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Kiek sukurti barkodu"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText2.Wrap( -1 )

        input2_layout.Add( self.staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        input2_layout.Add( ( 16, 0), 0, 0, 5 )

        self.inputText2 = wx.TextCtrl( self.mainWindowPanel, wx.ID_ANY, _(u"50"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputText2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.inputText2.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        input2_layout.Add( self.inputText2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        layout.Add( input2_layout, 0, 0, 5 )


        layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.testi = wx.Button( self.mainWindowPanel, wx.ID_ANY, _(u"Testi"), wx.DefaultPosition, wx.DefaultSize, 0 )
        layout.Add( self.testi, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.description = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Naujas barkodu kurimas, tai langas kuremia galima sukurti lapa kuriama butu pagal pasirenkta skaiciu tam tikras kiekis barkodu, juos galima atsispauzdinti, prilipinti ir sudeti i lentelia"), wx.DefaultPosition, wx.Size( 500,150 ), 0 )
        self.description.Wrap( -1 )

        layout.Add( self.description, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        self.mainWindowPanel.SetSizer( layout )
        self.mainWindowPanel.Layout()
        layout.Fit( self.mainWindowPanel )
        mainLayout.Add( self.mainWindowPanel, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.inputText1.Bind( wx.EVT_LEFT_DOWN, self.SelectingPath )
        self.testi.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def SelectingPath( self, event ):
        event.Skip()

    def next( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class ISNBkoduAtspauzdinimas
###########################################################################

class ISNBkoduAtspauzdinimas ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.mainWindowPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        layout = wx.BoxSizer( wx.VERTICAL )

        title_layout = wx.BoxSizer( wx.VERTICAL )

        self.title = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"ISNB kodu atspauždinimas"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.title.Wrap( -1 )

        self.title.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        title_layout.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( title_layout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.table = wx.grid.Grid( self.mainWindowPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,300 ), 0 )

        # Grid
        self.table.CreateGrid( 50, 1 )
        self.table.EnableEditing( True )
        self.table.EnableGridLines( True )
        self.table.EnableDragGridSize( False )
        self.table.SetMargins( 0, 0 )

        # Columns
        self.table.SetColSize( 0, 640 )
        self.table.EnableDragColMove( False )
        self.table.EnableDragColSize( True )
        self.table.SetColLabelValue( 0, _(u"ISBN") )
        self.table.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.table.AutoSizeRows()
        self.table.EnableDragRowSize( True )
        self.table.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.table.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        layout.Add( self.table, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 16), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        input_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.staticText1 = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Kur isaugoti norimus faila (PDF)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText1.Wrap( -1 )

        input_layout.Add( self.staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        input_layout.Add( ( 16, 0), 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.textCtrl1 = wx.TextCtrl( self.mainWindowPanel, wx.ID_ANY, _(u"/home/justpause/Programming/pyhton/KVM-bibliotekos-sistema/"), wx.DefaultPosition, wx.Size( 500,-1 ), wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
        self.textCtrl1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.textCtrl1.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        input_layout.Add( self.textCtrl1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        layout.Add( input_layout, 0, 0, 5 )


        layout.Add( ( 0, 16), 0, 0, 5 )

        self.testi = wx.Button( self.mainWindowPanel, wx.ID_ANY, _(u"Testi"), wx.DefaultPosition, wx.DefaultSize, 0 )
        layout.Add( self.testi, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.description = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Turint knyga su ISBN kodu, bet be barkodo. Galima nuskanuoti cia. Parasius norima kieki, reiketu issaugoti ir atsispauzdinti. Kad uzklijuoti\n"), wx.DefaultPosition, wx.Size( 500,150 ), 0 )
        self.description.Wrap( -1 )

        layout.Add( self.description, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.mainWindowPanel.SetSizer( layout )
        self.mainWindowPanel.Layout()
        layout.Fit( self.mainWindowPanel )
        mainLayout.Add( self.mainWindowPanel, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.textCtrl1.Bind( wx.EVT_LEFT_DOWN, self.SelectingPath )
        self.textCtrl1.Bind( wx.EVT_TEXT, self.enterI )
        self.testi.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def SelectingPath( self, event ):
        event.Skip()

    def enterI( self, event ):
        event.Skip()

    def next( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class IsCSV
###########################################################################

class IsCSV ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.mainWindowPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        layout = wx.BoxSizer( wx.VERTICAL )

        title_layout = wx.BoxSizer( wx.VERTICAL )

        self.title = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"CSV duomenu perdavimas i google sheets"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.title.Wrap( -1 )

        self.title.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        title_layout.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( title_layout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        input_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.staticText1 = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Iš kur norimus failua apimti (CSV)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText1.Wrap( -1 )

        input_layout.Add( self.staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        input_layout.Add( ( 16, 0), 0, 0, 5 )

        self.textCtrl1 = wx.TextCtrl( self.mainWindowPanel, wx.ID_ANY, _(u"/home/justpause/Programming/pyhton/KVM-bibliotekos-sistema"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.textCtrl1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.textCtrl1.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        input_layout.Add( self.textCtrl1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        layout.Add( input_layout, 0, 0, 5 )


        layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.testi = wx.Button( self.mainWindowPanel, wx.ID_ANY, _(u"Testi"), wx.DefaultPosition, wx.DefaultSize, 0 )
        layout.Add( self.testi, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.description = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Sis lapas leidzia pasirinkti faila i kuri yra surasyi struktirizuota csv lapa, I google lentelia"), wx.DefaultPosition, wx.Size( 500,150 ), 0 )
        self.description.Wrap( -1 )

        layout.Add( self.description, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.mainWindowPanel.SetSizer( layout )
        self.mainWindowPanel.Layout()
        layout.Fit( self.mainWindowPanel )
        mainLayout.Add( self.mainWindowPanel, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.textCtrl1.Bind( wx.EVT_LEFT_DOWN, self.SelectingPath )
        self.testi.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def SelectingPath( self, event ):
        event.Skip()

    def next( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class SukurtiCSV
###########################################################################

class SukurtiCSV ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.mainWindowPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        layout = wx.BoxSizer( wx.VERTICAL )

        title_layout = wx.BoxSizer( wx.VERTICAL )

        self.title = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Sukurti nauja CSV"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.title.Wrap( -1 )

        self.title.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        title_layout.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( title_layout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        input_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.staticText1 = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Kur isaugoti norimus faila (CSV)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText1.Wrap( -1 )

        input_layout.Add( self.staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        input_layout.Add( ( 16, 0), 1, wx.EXPAND, 5 )

        self.textCtrl1 = wx.TextCtrl( self.mainWindowPanel, wx.ID_ANY, _(u"/home/justpause/Programming/pyhton/KVM-bibliotekos-sistema"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.textCtrl1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.textCtrl1.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        input_layout.Add( self.textCtrl1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        layout.Add( input_layout, 0, 0, 5 )


        layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.testi = wx.Button( self.mainWindowPanel, wx.ID_ANY, _(u"Testi"), wx.DefaultPosition, wx.DefaultSize, 0 )
        layout.Add( self.testi, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.description = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Leidzia sukuri CSV dokumenta i kuri ranka galima surasti duomenis"), wx.DefaultPosition, wx.Size( 500,150 ), 0 )
        self.description.Wrap( -1 )

        layout.Add( self.description, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.mainWindowPanel.SetSizer( layout )
        self.mainWindowPanel.Layout()
        layout.Fit( self.mainWindowPanel )
        mainLayout.Add( self.mainWindowPanel, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.textCtrl1.Bind( wx.EVT_LEFT_DOWN, self.SelectingPath )
        self.testi.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def SelectingPath( self, event ):
        event.Skip()

    def next( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class IsKlaveturosSkaitytuvo
###########################################################################

class IsKlaveturosSkaitytuvo ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.mainWindowPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        layout = wx.BoxSizer( wx.VERTICAL )

        title_layout = wx.BoxSizer( wx.VERTICAL )

        self.title = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Klaviatūros / Skaitytuvo"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.title.Wrap( -1 )

        self.title.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        title_layout.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( title_layout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        input_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.staticText1 = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Kur išaugoti norimus faila (CSV)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText1.Wrap( -1 )

        input_layout.Add( self.staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        input_layout.Add( ( 16, 0), 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.textCtrl1 = wx.TextCtrl( self.mainWindowPanel, wx.ID_ANY, _(u"/home/justpause/Programming/pyhton/KVM-bibliotekos-sistema"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.textCtrl1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.textCtrl1.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        input_layout.Add( self.textCtrl1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        layout.Add( input_layout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 16), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        input_katalogas_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.staticText2 = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Kuris katalogos bus"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticText2.Wrap( -1 )

        input_katalogas_layout.Add( self.staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        input_katalogas_layout.Add( ( 16, 0), 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.textCtrl2 = wx.TextCtrl( self.mainWindowPanel, wx.ID_ANY, _(u"Už spintos"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.textCtrl2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.textCtrl2.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        input_katalogas_layout.Add( self.textCtrl2, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


        layout.Add( input_katalogas_layout, 0, wx.EXPAND, 5 )


        layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        button_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.testi_be_failo = wx.Button( self.mainWindowPanel, wx.ID_ANY, _(u"Skanuoti be išvedimo"), wx.DefaultPosition, wx.DefaultSize, 0 )
        button_layout.Add( self.testi_be_failo, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        button_layout.Add( ( 0, 0), 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.testi = wx.Button( self.mainWindowPanel, wx.ID_ANY, _(u"Testi"), wx.DefaultPosition, wx.DefaultSize, 0 )
        button_layout.Add( self.testi, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        layout.Add( button_layout, 0, wx.EXPAND, 5 )


        layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.description = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Leidzia, tiesei is klaveturos apeinant CSV failus surasyti duomenis tiesei i google lentelia, su funcionalumu jei knyga nerasta kad butu surasoma i atskira csv faila kuri galima bus ranka uzpildyti"), wx.DefaultPosition, wx.Size( 500,150 ), 0 )
        self.description.Wrap( -1 )

        layout.Add( self.description, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.mainWindowPanel.SetSizer( layout )
        self.mainWindowPanel.Layout()
        layout.Fit( self.mainWindowPanel )
        mainLayout.Add( self.mainWindowPanel, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.textCtrl1.Bind( wx.EVT_LEFT_DOWN, self.SelectingPath )
        self.testi_be_failo.Bind( wx.EVT_LEFT_DOWN, self.file_free_scan )
        self.testi.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def SelectingPath( self, event ):
        event.Skip()

    def file_free_scan( self, event ):
        event.Skip()

    def next( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class IsKlaveturosSkaitytuvoEkranas
###########################################################################

class IsKlaveturosSkaitytuvoEkranas ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.mainWindowPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        layout = wx.BoxSizer( wx.VERTICAL )

        title_layout = wx.BoxSizer( wx.VERTICAL )

        self.title = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Klaviatūros / Skaitytuvo"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.title.Wrap( -1 )

        self.title.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        title_layout.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( title_layout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        data_layout = wx.BoxSizer( wx.VERTICAL )

        self.dataViewList = wx.dataview.DataViewListCtrl( self.mainWindowPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,350 ), wx.dataview.DV_ROW_LINES )
        data_layout.Add( self.dataViewList, 0, 0, 5 )


        data_layout.Add( ( 0, 32), 0, 0, 5 )

        input_layout = wx.BoxSizer( wx.VERTICAL )

        self.ISBN = wx.TextCtrl( self.mainWindowPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,-1 ), wx.TE_CENTER|wx.TE_PROCESS_ENTER )
        input_layout.Add( self.ISBN, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        data_layout.Add( input_layout, 1, wx.EXPAND, 5 )


        layout.Add( data_layout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.description = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Leidzia, tiesei is klaveturos apeinant CSV failus surasyti duomenis tiesei i google lentelia, su funcionalumu jei knyga nerasta kad butu surasoma i atskira csv faila kuri galima bus ranka uzpildyti"), wx.DefaultPosition, wx.Size( 500,150 ), 0 )
        self.description.Wrap( -1 )

        layout.Add( self.description, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.mainWindowPanel.SetSizer( layout )
        self.mainWindowPanel.Layout()
        layout.Fit( self.mainWindowPanel )
        mainLayout.Add( self.mainWindowPanel, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.ISBN.Bind( wx.EVT_TEXT_ENTER, self.Enter )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def Enter( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class Isdavimas
###########################################################################

class Isdavimas ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.mainWindowPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        layout = wx.BoxSizer( wx.VERTICAL )

        title_layout = wx.BoxSizer( wx.VERTICAL )

        self.title = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Išdavimas"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.title.Wrap( -1 )

        self.title.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        title_layout.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( title_layout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.mainWindowPanel.SetSizer( layout )
        self.mainWindowPanel.Layout()
        layout.Fit( self.mainWindowPanel )
        mainLayout.Add( self.mainWindowPanel, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        data_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.KnygosSide = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        KnygosSideLayout = wx.BoxSizer( wx.VERTICAL )

        KnygosISBNLayout = wx.BoxSizer( wx.VERTICAL )

        self.KngosISBNLable = wx.StaticText( self.KnygosSide, wx.ID_ANY, _(u"Knygos ISBN"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.KngosISBNLable.Wrap( -1 )

        KnygosISBNLayout.Add( self.KngosISBNLable, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.KngosISBNInput = wx.TextCtrl( self.KnygosSide, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        KnygosISBNLayout.Add( self.KngosISBNInput, 0, wx.ALL|wx.EXPAND, 5 )

        self.KngosISBNRezult = wx.StaticText( self.KnygosSide, wx.ID_ANY, _(u"Nerasta"), wx.DefaultPosition, wx.Size( 400,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
        self.KngosISBNRezult.Wrap( -1 )

        self.KngosISBNRezult.Hide()

        KnygosISBNLayout.Add( self.KngosISBNRezult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        KnygosSideLayout.Add( KnygosISBNLayout, 0, wx.EXPAND, 5 )


        KnygosSideLayout.Add( ( 0, 16), 0, wx.EXPAND, 5 )

        AutoriusLayout = wx.BoxSizer( wx.VERTICAL )

        self.AutoriusLable = wx.StaticText( self.KnygosSide, wx.ID_ANY, _(u"Autorius"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AutoriusLable.Wrap( -1 )

        self.AutoriusLable.Hide()

        AutoriusLayout.Add( self.AutoriusLable, 0, wx.ALL, 5 )

        self.AutoriusInput = wx.TextCtrl( self.KnygosSide, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AutoriusInput.Hide()

        AutoriusLayout.Add( self.AutoriusInput, 0, wx.ALL|wx.EXPAND, 5 )


        KnygosSideLayout.Add( AutoriusLayout, 0, wx.EXPAND, 5 )


        KnygosSideLayout.Add( ( 0, 16), 0, wx.EXPAND, 5 )

        PavadinisLayout = wx.BoxSizer( wx.VERTICAL )

        self.PavadinimasLable = wx.StaticText( self.KnygosSide, wx.ID_ANY, _(u"Pavadinimas"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.PavadinimasLable.Wrap( -1 )

        self.PavadinimasLable.Hide()

        PavadinisLayout.Add( self.PavadinimasLable, 0, wx.ALL, 5 )

        self.PavadinimasInput = wx.TextCtrl( self.KnygosSide, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.PavadinimasInput.Hide()

        PavadinisLayout.Add( self.PavadinimasInput, 0, wx.ALL|wx.EXPAND, 5 )


        KnygosSideLayout.Add( PavadinisLayout, 0, wx.EXPAND, 5 )


        KnygosSideLayout.Add( ( 0, 16), 0, wx.EXPAND, 5 )

        MetaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.MetaiLable = wx.StaticText( self.KnygosSide, wx.ID_ANY, _(u"Metai"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.MetaiLable.Wrap( -1 )

        self.MetaiLable.Hide()

        MetaiLayout.Add( self.MetaiLable, 0, wx.ALL, 5 )

        self.MetaiInput = wx.TextCtrl( self.KnygosSide, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.MetaiInput.Hide()

        MetaiLayout.Add( self.MetaiInput, 0, wx.ALL|wx.EXPAND, 5 )


        KnygosSideLayout.Add( MetaiLayout, 0, wx.EXPAND, 5 )


        KnygosSideLayout.Add( ( 0, 16), 0, wx.EXPAND, 5 )

        ISBNLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISBNLable = wx.StaticText( self.KnygosSide, wx.ID_ANY, _(u"ISBN"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ISBNLable.Wrap( -1 )

        self.ISBNLable.Hide()

        ISBNLayout.Add( self.ISBNLable, 0, wx.ALL, 5 )

        self.ISBNInput = wx.TextCtrl( self.KnygosSide, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ISBNInput.Hide()

        ISBNLayout.Add( self.ISBNInput, 0, wx.ALL|wx.EXPAND, 5 )


        KnygosSideLayout.Add( ISBNLayout, 0, wx.EXPAND, 5 )


        self.KnygosSide.SetSizer( KnygosSideLayout )
        self.KnygosSide.Layout()
        KnygosSideLayout.Fit( self.KnygosSide )
        data_layout.Add( self.KnygosSide, 1, wx.EXPAND |wx.ALL, 25 )

        self.Tarpas = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.Tarpas.SetBackgroundColour( wx.Colour( 127, 0, 0 ) )

        data_layout.Add( self.Tarpas, 0, wx.EXPAND, 5 )

        self.NaudotojoSide = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        KortelesSideLayout = wx.BoxSizer( wx.VERTICAL )

        KortelesLayout = wx.BoxSizer( wx.VERTICAL )

        self.KortelesLable = wx.StaticText( self.NaudotojoSide, wx.ID_ANY, _(u"Korteles"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.KortelesLable.Wrap( -1 )

        KortelesLayout.Add( self.KortelesLable, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.KortelesInput = wx.TextCtrl( self.NaudotojoSide, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        KortelesLayout.Add( self.KortelesInput, 0, wx.ALL|wx.EXPAND, 5 )


        KortelesSideLayout.Add( KortelesLayout, 0, wx.EXPAND, 5 )


        KortelesSideLayout.Add( ( 0, 16), 0, wx.EXPAND, 5 )

        PakeistiLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.KortelesRezult = wx.StaticText( self.NaudotojoSide, wx.ID_ANY, _(u"Jei neturi korteles"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.KortelesRezult.Wrap( -1 )

        PakeistiLayout.Add( self.KortelesRezult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.Pakeisti = wx.Button( self.NaudotojoSide, wx.ID_ANY, _(u"Pakeisti"), wx.DefaultPosition, wx.DefaultSize, 0 )
        PakeistiLayout.Add( self.Pakeisti, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        KortelesSideLayout.Add( PakeistiLayout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        VardasLayout = wx.BoxSizer( wx.VERTICAL )

        self.VardasLable = wx.StaticText( self.NaudotojoSide, wx.ID_ANY, _(u"Vardas"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.VardasLable.Wrap( -1 )

        self.VardasLable.Enable( False )

        VardasLayout.Add( self.VardasLable, 0, wx.ALL, 5 )

        self.VardasInput = wx.TextCtrl( self.NaudotojoSide, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.VardasInput.Enable( False )

        VardasLayout.Add( self.VardasInput, 0, wx.ALL|wx.EXPAND, 5 )


        KortelesSideLayout.Add( VardasLayout, 0, wx.EXPAND, 5 )

        KlaseLayout = wx.BoxSizer( wx.VERTICAL )

        self.KlaseLable = wx.StaticText( self.NaudotojoSide, wx.ID_ANY, _(u"Klase"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.KlaseLable.Wrap( -1 )

        self.KlaseLable.Enable( False )

        KlaseLayout.Add( self.KlaseLable, 0, wx.ALL, 5 )

        self.KlaseInput = wx.TextCtrl( self.NaudotojoSide, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.KlaseInput.Enable( False )

        KlaseLayout.Add( self.KlaseInput, 0, wx.ALL|wx.EXPAND, 5 )


        KortelesSideLayout.Add( KlaseLayout, 0, wx.EXPAND, 5 )

        self.Isduoti = wx.Button( self.NaudotojoSide, wx.ID_ANY, _(u"Isduoti"), wx.DefaultPosition, wx.DefaultSize, 0 )
        KortelesSideLayout.Add( self.Isduoti, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        KortelesSideLayout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.description = wx.StaticText( self.NaudotojoSide, wx.ID_ANY, _(u"Duoda galimybe lengvai isduoti knuyga, surasant, Knygos ISBN, Korteles Koda"), wx.DefaultPosition, wx.Size( 400,100 ), 0 )
        self.description.Wrap( -1 )

        KortelesSideLayout.Add( self.description, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.NaudotojoSide.SetSizer( KortelesSideLayout )
        self.NaudotojoSide.Layout()
        KortelesSideLayout.Fit( self.NaudotojoSide )
        data_layout.Add( self.NaudotojoSide, 1, wx.EXPAND |wx.ALL, 25 )


        mainLayout.Add( data_layout, 1, wx.EXPAND, 5 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.KngosISBNInput.Bind( wx.EVT_LEAVE_WINDOW, self.EnterISBN )
        self.KngosISBNInput.Bind( wx.EVT_TEXT_ENTER, self.EnterISBN )
        self.KortelesRezult.Bind( wx.EVT_LEFT_DOWN, self.Isduoti_button )
        self.Pakeisti.Bind( wx.EVT_LEFT_DOWN, self.Pakeisti_button )
        self.VardasInput.Bind( wx.EVT_LEFT_DOWN, self.SlectedName )
        self.KlaseInput.Bind( wx.EVT_LEFT_DOWN, self.SlectedKlase )
        self.Isduoti.Bind( wx.EVT_LEFT_DOWN, self.Isduoti_button )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def EnterISBN( self, event ):
        event.Skip()


    def Isduoti_button( self, event ):
        event.Skip()

    def Pakeisti_button( self, event ):
        event.Skip()

    def SlectedName( self, event ):
        event.Skip()

    def SlectedKlase( self, event ):
        event.Skip()


    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class Patikrinti
###########################################################################

class Patikrinti ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.Title = wx.StaticText( self, wx.ID_ANY, _(u"Didzioji lentele"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Title.Wrap( -1 )

        self.Title.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        mainLayout.Add( self.Title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        layout = wx.BoxSizer( wx.HORIZONTAL )

        data_layout = wx.BoxSizer( wx.VERTICAL )

        self.outputAutorius = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        autoriusLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.autorius_staticText = wx.StaticText( self.outputAutorius, wx.ID_ANY, _(u"Autorius"), wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.autorius_staticText.Wrap( -1 )

        autoriusLayout.Add( self.autorius_staticText, 0, wx.ALL, 5 )

        self.autorius_output = wx.StaticText( self.outputAutorius, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.autorius_output.Wrap( -1 )

        autoriusLayout.Add( self.autorius_output, 1, wx.ALL, 5 )


        self.outputAutorius.SetSizer( autoriusLayout )
        self.outputAutorius.Layout()
        autoriusLayout.Fit( self.outputAutorius )
        data_layout.Add( self.outputAutorius, 0, wx.ALL|wx.EXPAND, 5 )

        self.outputPavadinimas = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        pavadinimasLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.pavadinimas_staticText = wx.StaticText( self.outputPavadinimas, wx.ID_ANY, _(u"Pavadinimas"), wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.pavadinimas_staticText.Wrap( -1 )

        pavadinimasLayout.Add( self.pavadinimas_staticText, 0, wx.ALL, 5 )

        self.pavadinimas_output = wx.StaticText( self.outputPavadinimas, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.pavadinimas_output.Wrap( -1 )

        pavadinimasLayout.Add( self.pavadinimas_output, 1, wx.ALL, 5 )


        self.outputPavadinimas.SetSizer( pavadinimasLayout )
        self.outputPavadinimas.Layout()
        pavadinimasLayout.Fit( self.outputPavadinimas )
        data_layout.Add( self.outputPavadinimas, 0, wx.EXPAND|wx.ALL, 5 )

        self.outputMetai = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        metaiLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.metai_staticText = wx.StaticText( self.outputMetai, wx.ID_ANY, _(u"Metai"), wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.metai_staticText.Wrap( -1 )

        metaiLayout.Add( self.metai_staticText, 0, wx.ALL, 5 )

        self.metai_output = wx.StaticText( self.outputMetai, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.metai_output.Wrap( -1 )

        metaiLayout.Add( self.metai_output, 1, wx.ALL, 5 )


        self.outputMetai.SetSizer( metaiLayout )
        self.outputMetai.Layout()
        metaiLayout.Fit( self.outputMetai )
        data_layout.Add( self.outputMetai, 0, wx.ALL|wx.EXPAND, 5 )

        self.outputISBN = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        outputLayout1 = wx.BoxSizer( wx.HORIZONTAL )

        self.isbn_staticText = wx.StaticText( self.outputISBN, wx.ID_ANY, _(u"ISBN"), wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.isbn_staticText.Wrap( -1 )

        outputLayout1.Add( self.isbn_staticText, 0, wx.ALL, 5 )

        self.isbn_output = wx.StaticText( self.outputISBN, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.isbn_output.Wrap( -1 )

        outputLayout1.Add( self.isbn_output, 1, wx.ALL, 5 )


        self.outputISBN.SetSizer( outputLayout1 )
        self.outputISBN.Layout()
        outputLayout1.Fit( self.outputISBN )
        data_layout.Add( self.outputISBN, 0, wx.ALL|wx.EXPAND, 5 )

        self.outputKatalogas = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        outputLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.katalogas_staticText = wx.StaticText( self.outputKatalogas, wx.ID_ANY, _(u"Katalogas"), wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.katalogas_staticText.Wrap( -1 )

        outputLayout.Add( self.katalogas_staticText, 0, wx.ALL, 5 )

        self.katalogas_output = wx.StaticText( self.outputKatalogas, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.katalogas_output.Wrap( -1 )

        outputLayout.Add( self.katalogas_output, 1, wx.ALL, 5 )


        self.outputKatalogas.SetSizer( outputLayout )
        self.outputKatalogas.Layout()
        outputLayout.Fit( self.outputKatalogas )
        data_layout.Add( self.outputKatalogas, 0, wx.EXPAND |wx.ALL, 5 )


        data_layout.Add( ( 0, 16), 0, 0, 5 )

        self.description = wx.StaticText( self, wx.ID_ANY, _(u"Duoda galimybe patikrinti ar knyga yra lenteleja "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.description.Wrap( -1 )

        data_layout.Add( self.description, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        data_layout.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.ISBN_window_title = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        ISBN_window_layout = wx.BoxSizer( wx.VERTICAL )

        self.ISBN_window_title_text = wx.StaticText( self.ISBN_window_title, wx.ID_ANY, _(u"ISBN"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ISBN_window_title_text.Wrap( -1 )

        ISBN_window_layout.Add( self.ISBN_window_title_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.ISBN_window_input = wx.TextCtrl( self.ISBN_window_title, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        ISBN_window_layout.Add( self.ISBN_window_input, 0, wx.ALL|wx.EXPAND, 5 )


        self.ISBN_window_title.SetSizer( ISBN_window_layout )
        self.ISBN_window_title.Layout()
        ISBN_window_layout.Fit( self.ISBN_window_title )
        data_layout.Add( self.ISBN_window_title, 0, wx.ALL|wx.EXPAND, 5 )


        layout.Add( data_layout, 1, wx.EXPAND|wx.BOTTOM|wx.LEFT, 25 )

        history_layout = wx.BoxSizer( wx.VERTICAL )

        self.history = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.history.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )

        dataViewList_layout = wx.BoxSizer( wx.VERTICAL )

        self.history_table = wx.dataview.DataViewListCtrl( self.history, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_ROW_LINES )
        dataViewList_layout.Add( self.history_table, 1, wx.EXPAND, 5 )


        self.history.SetSizer( dataViewList_layout )
        self.history.Layout()
        dataViewList_layout.Fit( self.history )
        history_layout.Add( self.history, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 25 )


        layout.Add( history_layout, 1, wx.EXPAND, 5 )


        mainLayout.Add( layout, 1, wx.EXPAND, 5 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.ISBN_window_input.Bind( wx.EVT_TEXT_ENTER, self.Enter )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def Enter( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class Gazinimas
###########################################################################

class Gazinimas ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.mainWindowPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        self.mainWindowPanel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        layout = wx.BoxSizer( wx.VERTICAL )

        title_layout = wx.BoxSizer( wx.VERTICAL )

        self.title = wx.StaticText( self.mainWindowPanel, wx.ID_ANY, _(u"Grąžinimas"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.title.Wrap( -1 )

        self.title.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        title_layout.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( title_layout, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        layout.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.mainWindowPanel.SetSizer( layout )
        self.mainWindowPanel.Layout()
        layout.Fit( self.mainWindowPanel )
        mainLayout.Add( self.mainWindowPanel, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        data_layout = wx.BoxSizer( wx.VERTICAL )

        kortelesLayout = wx.BoxSizer( wx.VERTICAL )

        self.KnygosLable = wx.StaticText( self, wx.ID_ANY, _(u"Knygos isbn"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.KnygosLable.Wrap( -1 )

        self.KnygosLable.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        kortelesLayout.Add( self.KnygosLable, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.KnygosInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        kortelesLayout.Add( self.KnygosInput, 0, wx.ALL|wx.EXPAND, 5 )


        kortelesLayout.Add( ( 0, 24), 1, wx.EXPAND, 5 )


        data_layout.Add( kortelesLayout, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 64 )

        Grazintojo_Layout = wx.BoxSizer( wx.HORIZONTAL )

        Inner_grazintojo_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.KnygosLable = wx.StaticText( self, wx.ID_ANY, _(u"Grazinta knyga :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.KnygosLable.Wrap( -1 )

        Inner_grazintojo_layout.Add( self.KnygosLable, 0, 0, 5 )

        self.KnygosStaticText = wx.StaticText( self, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.KnygosStaticText.Wrap( -1 )

        Inner_grazintojo_layout.Add( self.KnygosStaticText, 0, wx.LEFT, 5 )


        Inner_grazintojo_layout.Add( ( 300, 0), 0, 0, 5 )

        self.NaudotojoLable = wx.StaticText( self, wx.ID_ANY, _(u"Kas grazinto knyga :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NaudotojoLable.Wrap( -1 )

        Inner_grazintojo_layout.Add( self.NaudotojoLable, 0, 0, 5 )

        self.NaudotojoStaticText = wx.StaticText( self, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NaudotojoStaticText.Wrap( -1 )

        Inner_grazintojo_layout.Add( self.NaudotojoStaticText, 0, wx.LEFT, 5 )


        Grazintojo_Layout.Add( Inner_grazintojo_layout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        data_layout.Add( Grazintojo_Layout, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.LEFT, 170 )


        data_layout.Add( ( 0, 16), 0, 0, 5 )

        self.testi = wx.Button( self, wx.ID_ANY, _(u"Testi"), wx.DefaultPosition, wx.DefaultSize, 0 )
        data_layout.Add( self.testi, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        mainLayout.Add( data_layout, 1, wx.EXPAND, 5 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.KnygosInput.Bind( wx.EVT_LEAVE_WINDOW, self.Enter )
        self.KnygosInput.Bind( wx.EVT_TEXT_ENTER, self.Enter )
        self.testi.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def Enter( self, event ):
        event.Skip()


    def next( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class PromtForReplacment
###########################################################################

class PromtForReplacment ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,460 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        data_layout = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self, wx.ID_ANY, _(u"Pakeitimas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        data_layout.Add( Titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        Compare_Autroius = wx.BoxSizer( wx.HORIZONTAL )

        self.panel_autorius = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel_autorius.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        main_layout_autorius = wx.BoxSizer( wx.VERTICAL )

        self.old_text_autorius = wx.StaticText( self.panel_autorius, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.old_text_autorius.Wrap( -1 )

        self.old_text_autorius.SetForegroundColour( wx.Colour( 153, 8, 0 ) )

        main_layout_autorius.Add( self.old_text_autorius, 0, wx.ALL|wx.EXPAND, 5 )

        self.new_text_autorius = wx.StaticText( self.panel_autorius, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.new_text_autorius.Wrap( -1 )

        self.new_text_autorius.SetForegroundColour( wx.Colour( 52, 112, 29 ) )

        main_layout_autorius.Add( self.new_text_autorius, 0, wx.ALL|wx.EXPAND, 5 )


        self.panel_autorius.SetSizer( main_layout_autorius )
        self.panel_autorius.Layout()
        main_layout_autorius.Fit( self.panel_autorius )
        Compare_Autroius.Add( self.panel_autorius, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        autorius_layout = wx.BoxSizer( wx.VERTICAL )

        self.red1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.red1.SetBackgroundColour( wx.Colour( 233, 12, 0 ) )

        autorius_layout.Add( self.red1, 1, wx.ALL, 5 )

        self.green1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.green1.SetBackgroundColour( wx.Colour( 65, 139, 36 ) )

        autorius_layout.Add( self.green1, 1, wx.ALL, 5 )


        Compare_Autroius.Add( autorius_layout, 0, wx.EXPAND, 5 )


        data_layout.Add( Compare_Autroius, 0, wx.EXPAND, 5 )

        Compare_Pavadinimas = wx.BoxSizer( wx.HORIZONTAL )

        self.panel_pavadinimas = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel_pavadinimas.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        main_layout_pavadinimas = wx.BoxSizer( wx.VERTICAL )

        self.old_text_pavadinimas = wx.StaticText( self.panel_pavadinimas, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.old_text_pavadinimas.Wrap( -1 )

        self.old_text_pavadinimas.SetForegroundColour( wx.Colour( 153, 8, 0 ) )

        main_layout_pavadinimas.Add( self.old_text_pavadinimas, 0, wx.ALL|wx.EXPAND, 5 )

        self.new_text_pavadinimas = wx.StaticText( self.panel_pavadinimas, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.new_text_pavadinimas.Wrap( -1 )

        self.new_text_pavadinimas.SetForegroundColour( wx.Colour( 52, 112, 29 ) )

        main_layout_pavadinimas.Add( self.new_text_pavadinimas, 0, wx.ALL|wx.EXPAND, 5 )


        self.panel_pavadinimas.SetSizer( main_layout_pavadinimas )
        self.panel_pavadinimas.Layout()
        main_layout_pavadinimas.Fit( self.panel_pavadinimas )
        Compare_Pavadinimas.Add( self.panel_pavadinimas, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        pavadinimas_layout = wx.BoxSizer( wx.VERTICAL )

        self.red2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.red2.SetBackgroundColour( wx.Colour( 233, 12, 0 ) )

        pavadinimas_layout.Add( self.red2, 1, wx.ALL, 5 )

        self.green2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.green2.SetBackgroundColour( wx.Colour( 65, 139, 36 ) )

        pavadinimas_layout.Add( self.green2, 1, wx.ALL, 5 )


        Compare_Pavadinimas.Add( pavadinimas_layout, 0, wx.EXPAND, 5 )


        data_layout.Add( Compare_Pavadinimas, 0, wx.EXPAND, 5 )

        Compare_Metai = wx.BoxSizer( wx.HORIZONTAL )

        self.panel_metai = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel_metai.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        main_layout_metai = wx.BoxSizer( wx.VERTICAL )

        self.old_text_metai = wx.StaticText( self.panel_metai, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.old_text_metai.Wrap( -1 )

        self.old_text_metai.SetForegroundColour( wx.Colour( 153, 8, 0 ) )

        main_layout_metai.Add( self.old_text_metai, 0, wx.ALL|wx.EXPAND, 5 )

        self.new_text_metai = wx.StaticText( self.panel_metai, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.new_text_metai.Wrap( -1 )

        self.new_text_metai.SetForegroundColour( wx.Colour( 52, 112, 29 ) )

        main_layout_metai.Add( self.new_text_metai, 0, wx.ALL|wx.EXPAND, 5 )


        self.panel_metai.SetSizer( main_layout_metai )
        self.panel_metai.Layout()
        main_layout_metai.Fit( self.panel_metai )
        Compare_Metai.Add( self.panel_metai, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        metai_layout = wx.BoxSizer( wx.VERTICAL )

        self.red3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.red3.SetBackgroundColour( wx.Colour( 233, 12, 0 ) )

        metai_layout.Add( self.red3, 1, wx.ALL, 5 )

        self.green3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.green3.SetBackgroundColour( wx.Colour( 65, 139, 36 ) )

        metai_layout.Add( self.green3, 1, wx.ALL, 5 )


        Compare_Metai.Add( metai_layout, 0, wx.EXPAND, 5 )


        data_layout.Add( Compare_Metai, 0, wx.EXPAND, 5 )

        Compare_ISBN = wx.BoxSizer( wx.HORIZONTAL )

        self.panel_isbn = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel_isbn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        main_layout_isbn = wx.BoxSizer( wx.VERTICAL )

        self.old_text_isbn = wx.StaticText( self.panel_isbn, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.old_text_isbn.Wrap( -1 )

        self.old_text_isbn.SetForegroundColour( wx.Colour( 153, 8, 0 ) )

        main_layout_isbn.Add( self.old_text_isbn, 0, wx.ALL|wx.EXPAND, 5 )

        self.new_text_isbn = wx.StaticText( self.panel_isbn, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.new_text_isbn.Wrap( -1 )

        self.new_text_isbn.SetForegroundColour( wx.Colour( 52, 112, 29 ) )

        main_layout_isbn.Add( self.new_text_isbn, 0, wx.ALL|wx.EXPAND, 5 )


        self.panel_isbn.SetSizer( main_layout_isbn )
        self.panel_isbn.Layout()
        main_layout_isbn.Fit( self.panel_isbn )
        Compare_ISBN.Add( self.panel_isbn, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        isbn_layout = wx.BoxSizer( wx.VERTICAL )

        self.red4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.red4.SetBackgroundColour( wx.Colour( 233, 12, 0 ) )

        isbn_layout.Add( self.red4, 1, wx.ALL, 5 )

        self.green4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.green4.SetBackgroundColour( wx.Colour( 65, 139, 36 ) )

        isbn_layout.Add( self.green4, 1, wx.ALL, 5 )


        Compare_ISBN.Add( isbn_layout, 0, wx.EXPAND, 5 )


        data_layout.Add( Compare_ISBN, 0, wx.EXPAND, 5 )


        data_layout.Add( ( 0, 16), 0, 0, 5 )

        button_layout = wx.BoxSizer( wx.HORIZONTAL )

        self.atsisakyti = wx.Button( self, wx.ID_ANY, _(u"atsisakyti"), wx.DefaultPosition, wx.DefaultSize, 0 )
        button_layout.Add( self.atsisakyti, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        button_layout.Add( ( 0, 0), 1, 0, 5 )

        self.sutikti = wx.Button( self, wx.ID_ANY, _(u"sutikti"), wx.DefaultPosition, wx.DefaultSize, 0 )
        button_layout.Add( self.sutikti, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        data_layout.Add( button_layout, 0, wx.EXPAND, 5 )


        self.SetSizer( data_layout )
        self.Layout()

        # Connect Events
        self.atsisakyti.Bind( wx.EVT_LEFT_DOWN, self.cancel )
        self.sutikti.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def cancel( self, event ):
        event.Skip()

    def next( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


