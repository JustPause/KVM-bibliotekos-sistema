# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class Pagrindinis
###########################################################################

class Pagrindinis ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Pagrindinis"), pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE )

        self.SetSizeHints( wx.Size( 1280,720 ), wx.Size( 1280,720 ) )

        MainLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.sidePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 256,-1 ), wx.BORDER_NONE )
        self.sidePanel.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        sideLayout = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        sideLayout.Add( Titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        sideNavigsionLayout = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Barkodai, 0, wx.ALL, 5 )

        BarkodaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.Button( self.sidePanel, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.Size( 180,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Kurti_naujus_barkodus = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.Size( 150,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.Kurti_naujus_barkodus, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( BarkodaiLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        KnyguLayout = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.Size( 168,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Ieškoti_pagal_pavadinima = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.Size( 166,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Ieškoti_pagal_pavadinima, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Iš_CSV = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.Size( 52,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_CSV, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( KnyguLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.Size( 114,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Localioje_lenteje, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Google_sheets_lenteliaja = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Google sheets lenteliaja"), wx.DefaultPosition, wx.Size( 160,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Google_sheets_lenteliaja, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.sidePanel.SetSizer( sideLayout )
        self.sidePanel.Layout()
        MainLayout.Add( self.sidePanel, 0, wx.EXPAND, 0 )

        self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.mainPanel.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        mainLayout = wx.BoxSizer( wx.VERTICAL )

        arrowLayout = wx.GridSizer( 0, 2, 0, 0 )

        self.m_bitmap2 = wx.StaticBitmap( self.mainPanel, wx.ID_ANY, wx.Bitmap( self.img_path( u"img/Vector.png" ), wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        arrowLayout.Add( self.m_bitmap2, 0, wx.TOP, 160 )


        mainLayout.Add( arrowLayout, 0, wx.LEFT, 25 )

        self.arrowText = wx.StaticText( self.mainPanel, wx.ID_ANY, _(u"Pasirinkite kategorija"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.arrowText.Wrap( -1 )

        self.arrowText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        mainLayout.Add( self.arrowText, 0, wx.LEFT, 245 )


        self.mainPanel.SetSizer( mainLayout )
        self.mainPanel.Layout()
        mainLayout.Fit( self.mainPanel )
        MainLayout.Add( self.mainPanel, 1, wx.EXPAND, 0 )


        self.SetSizer( MainLayout )
        self.Layout()

        self.Centre( wx.HORIZONTAL )

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class KurtiNaujusBarkodus
###########################################################################

class KurtiNaujusBarkodus ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.sidePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 256,-1 ), wx.BORDER_NONE )
        self.sidePanel.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        sideLayout = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        sideLayout.Add( Titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        sideNavigsionLayout = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Barkodai, 0, wx.ALL, 5 )

        BarkodaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.Button( self.sidePanel, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.Size( 180,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Kurti_naujus_barkodus = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.Size( 150,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.Kurti_naujus_barkodus, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( BarkodaiLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        KnyguLayout = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.Size( 168,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Ieškoti_pagal_pavadinima = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.Size( 166,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Ieškoti_pagal_pavadinima, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Iš_CSV = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.Size( 52,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_CSV, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( KnyguLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.Size( 114,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Localioje_lenteje, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Google_sheets_lenteliaja = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Google sheets lenteliaja"), wx.DefaultPosition, wx.Size( 160,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Google_sheets_lenteliaja, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.sidePanel.SetSizer( sideLayout )
        self.sidePanel.Layout()
        MainLayout.Add( self.sidePanel, 0, wx.EXPAND, 0 )

        self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.mainPanel.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        self.mainPanel.SetSizer( mainLayout )
        self.mainPanel.Layout()
        mainLayout.Fit( self.mainPanel )
        MainLayout.Add( self.mainPanel, 1, wx.EXPAND, 0 )


        self.SetSizer( MainLayout )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class ISNBkoduAtspauzdinimas
###########################################################################

class ISNBkoduAtspauzdinimas ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.sidePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 256,-1 ), wx.BORDER_NONE )
        self.sidePanel.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        sideLayout = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        sideLayout.Add( Titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        sideNavigsionLayout = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Barkodai, 0, wx.ALL, 5 )

        BarkodaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.Button( self.sidePanel, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.Size( 180,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Kurti_naujus_barkodus = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.Size( 150,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.Kurti_naujus_barkodus, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( BarkodaiLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        KnyguLayout = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.Size( 168,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Ieškoti_pagal_pavadinima = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.Size( 166,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Ieškoti_pagal_pavadinima, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Iš_CSV = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.Size( 52,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_CSV, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( KnyguLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.Size( 114,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Localioje_lenteje, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Google_sheets_lenteliaja = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Google sheets lenteliaja"), wx.DefaultPosition, wx.Size( 160,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Google_sheets_lenteliaja, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.sidePanel.SetSizer( sideLayout )
        self.sidePanel.Layout()
        MainLayout.Add( self.sidePanel, 0, wx.EXPAND, 0 )

        self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.mainPanel.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        self.mainPanel.SetSizer( mainLayout )
        self.mainPanel.Layout()
        mainLayout.Fit( self.mainPanel )
        MainLayout.Add( self.mainPanel, 1, wx.EXPAND, 0 )


        self.SetSizer( MainLayout )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class IsCSV
###########################################################################

class IsCSV ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.sidePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 256,-1 ), wx.BORDER_NONE )
        self.sidePanel.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        sideLayout = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        sideLayout.Add( Titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        sideNavigsionLayout = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Barkodai, 0, wx.ALL, 5 )

        BarkodaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.Button( self.sidePanel, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.Size( 180,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Kurti_naujus_barkodus = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.Size( 150,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.Kurti_naujus_barkodus, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( BarkodaiLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        KnyguLayout = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.Size( 168,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Ieškoti_pagal_pavadinima = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.Size( 166,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Ieškoti_pagal_pavadinima, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Iš_CSV = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.Size( 52,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_CSV, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( KnyguLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.Size( 114,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Localioje_lenteje, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Google_sheets_lenteliaja = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Google sheets lenteliaja"), wx.DefaultPosition, wx.Size( 160,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Google_sheets_lenteliaja, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.sidePanel.SetSizer( sideLayout )
        self.sidePanel.Layout()
        MainLayout.Add( self.sidePanel, 0, wx.EXPAND, 0 )

        self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.mainPanel.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        self.mainPanel.SetSizer( mainLayout )
        self.mainPanel.Layout()
        mainLayout.Fit( self.mainPanel )
        MainLayout.Add( self.mainPanel, 1, wx.EXPAND, 0 )


        self.SetSizer( MainLayout )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class IsKlavetūrosSkaitytuvo
###########################################################################

class IsKlavetūrosSkaitytuvo ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.sidePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 256,-1 ), wx.BORDER_NONE )
        self.sidePanel.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        sideLayout = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        sideLayout.Add( Titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        sideNavigsionLayout = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Barkodai, 0, wx.ALL, 5 )

        BarkodaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.Button( self.sidePanel, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.Size( 180,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Kurti_naujus_barkodus = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.Size( 150,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.Kurti_naujus_barkodus, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( BarkodaiLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        KnyguLayout = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.Size( 168,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Ieškoti_pagal_pavadinima = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.Size( 166,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Ieškoti_pagal_pavadinima, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Iš_CSV = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.Size( 52,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_CSV, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( KnyguLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.Size( 114,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Localioje_lenteje, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Google_sheets_lenteliaja = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Google sheets lenteliaja"), wx.DefaultPosition, wx.Size( 160,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Google_sheets_lenteliaja, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.sidePanel.SetSizer( sideLayout )
        self.sidePanel.Layout()
        MainLayout.Add( self.sidePanel, 0, wx.EXPAND, 0 )

        self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.mainPanel.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        self.mainPanel.SetSizer( mainLayout )
        self.mainPanel.Layout()
        mainLayout.Fit( self.mainPanel )
        MainLayout.Add( self.mainPanel, 1, wx.EXPAND, 0 )


        self.SetSizer( MainLayout )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class IeskotiPagalPavadinima
###########################################################################

class IeskotiPagalPavadinima ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.sidePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 256,-1 ), wx.BORDER_NONE )
        self.sidePanel.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        sideLayout = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        sideLayout.Add( Titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        sideNavigsionLayout = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Barkodai, 0, wx.ALL, 5 )

        BarkodaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.Button( self.sidePanel, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.Size( 180,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Kurti_naujus_barkodus = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.Size( 150,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.Kurti_naujus_barkodus, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( BarkodaiLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        KnyguLayout = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.Size( 168,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Ieškoti_pagal_pavadinima = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.Size( 166,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Ieškoti_pagal_pavadinima, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Iš_CSV = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.Size( 52,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_CSV, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( KnyguLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.Size( 114,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Localioje_lenteje, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Google_sheets_lenteliaja = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Google sheets lenteliaja"), wx.DefaultPosition, wx.Size( 160,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Google_sheets_lenteliaja, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.sidePanel.SetSizer( sideLayout )
        self.sidePanel.Layout()
        MainLayout.Add( self.sidePanel, 0, wx.EXPAND, 0 )

        self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.mainPanel.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        self.mainPanel.SetSizer( mainLayout )
        self.mainPanel.Layout()
        mainLayout.Fit( self.mainPanel )
        MainLayout.Add( self.mainPanel, 1, wx.EXPAND, 0 )


        self.SetSizer( MainLayout )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class KurtiNaujusBarkodus
###########################################################################

class KurtiNaujusBarkodus ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.sidePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 256,-1 ), wx.BORDER_NONE )
        self.sidePanel.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        sideLayout = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        sideLayout.Add( Titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        sideNavigsionLayout = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Barkodai, 0, wx.ALL, 5 )

        BarkodaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.Button( self.sidePanel, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.Size( 180,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Kurti_naujus_barkodus = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.Size( 150,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.Kurti_naujus_barkodus, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( BarkodaiLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        KnyguLayout = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.Size( 168,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Ieškoti_pagal_pavadinima = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.Size( 166,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Ieškoti_pagal_pavadinima, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Iš_CSV = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.Size( 52,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_CSV, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( KnyguLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.Size( 114,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Localioje_lenteje, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Google_sheets_lenteliaja = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Google sheets lenteliaja"), wx.DefaultPosition, wx.Size( 160,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Google_sheets_lenteliaja, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.sidePanel.SetSizer( sideLayout )
        self.sidePanel.Layout()
        MainLayout.Add( self.sidePanel, 0, wx.EXPAND, 0 )

        self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.mainPanel.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        self.mainPanel.SetSizer( mainLayout )
        self.mainPanel.Layout()
        mainLayout.Fit( self.mainPanel )
        MainLayout.Add( self.mainPanel, 1, wx.EXPAND, 0 )


        self.SetSizer( MainLayout )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class ISNBKoduAtspauzdinimas
###########################################################################

class ISNBKoduAtspauzdinimas ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        MainLayout = wx.BoxSizer( wx.HORIZONTAL )

        self.sidePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 256,-1 ), wx.BORDER_NONE )
        self.sidePanel.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        sideLayout = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        sideLayout.Add( Titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        sideNavigsionLayout = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Barkodai, 0, wx.ALL, 5 )

        BarkodaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.Button( self.sidePanel, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.Size( 180,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Kurti_naujus_barkodus = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.Size( 150,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.Kurti_naujus_barkodus, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( BarkodaiLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        KnyguLayout = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.Size( 168,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Ieškoti_pagal_pavadinima = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.Size( 166,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Ieškoti_pagal_pavadinima, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Iš_CSV = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.Size( 52,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_CSV, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( KnyguLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self.sidePanel, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.Size( 114,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Localioje_lenteje, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Google_sheets_lenteliaja = wx.Button( self.sidePanel, wx.ID_ANY, _(u"Google sheets lenteliaja"), wx.DefaultPosition, wx.Size( 160,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Google_sheets_lenteliaja, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.sidePanel.SetSizer( sideLayout )
        self.sidePanel.Layout()
        MainLayout.Add( self.sidePanel, 0, wx.EXPAND, 0 )

        self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.mainPanel.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        self.mainPanel.SetSizer( mainLayout )
        self.mainPanel.Layout()
        mainLayout.Fit( self.mainPanel )
        MainLayout.Add( self.mainPanel, 1, wx.EXPAND, 0 )


        self.SetSizer( MainLayout )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class SideBar
###########################################################################

class SideBar ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 256,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        sideLayout = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        sideLayout.Add( Titulas_BarkodasBoxSizer, 0, wx.EXPAND, 5 )

        sideNavigsionLayout = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Barkodai, 0, wx.ALL, 5 )

        BarkodaiLayout = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.Button( self, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.Size( 180,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Kurti_naujus_barkodus = wx.Button( self, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.Size( 150,-1 ), wx.BORDER_NONE )
        BarkodaiLayout.Add( self.Kurti_naujus_barkodus, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( BarkodaiLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        KnyguLayout = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.Button( self, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.Size( 168,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Ieškoti_pagal_pavadinima = wx.Button( self, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.Size( 166,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Ieškoti_pagal_pavadinima, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Iš_CSV = wx.Button( self, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.Size( 52,-1 ), wx.BORDER_NONE )
        KnyguLayout.Add( self.Iš_CSV, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( KnyguLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.Button( self, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.Size( 114,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Localioje_lenteje, 0, wx.RIGHT|wx.LEFT, 5 )

        self.Google_sheets_lenteliaja = wx.Button( self, wx.ID_ANY, _(u"Google sheets lenteliaja"), wx.DefaultPosition, wx.Size( 160,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Google_sheets_lenteliaja, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.SetSizer( sideLayout )
        self.Layout()

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class MainPanel
###########################################################################

class MainPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )

        arrowLayout = wx.GridSizer( 0, 2, 0, 0 )

        self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( self.img_path( u"img/Vector.png" ), wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        arrowLayout.Add( self.m_bitmap2, 0, wx.TOP, 160 )


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


