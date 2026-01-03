# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
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


        sideNavigsionLayout.Add( ( 0, 25), 0, wx.EXPAND, 5 )

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


        sideNavigsionLayout.Add( ( 0, 25), 0, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,32 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        sideNavigsionLayout.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        PatikrinimasLayout = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.Button( self, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.Size( 114,-1 ), wx.BORDER_NONE )
        PatikrinimasLayout.Add( self.Localioje_lenteje, 0, wx.RIGHT|wx.LEFT, 5 )


        sideNavigsionLayout.Add( PatikrinimasLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        sideNavigsionLayout.Add( ( 0, 280), 1, wx.EXPAND, 5 )

        self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, _(u"Version 0.1 build 2026-01-01"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )

        self.m_staticText29.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        sideNavigsionLayout.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        sideLayout.Add( sideNavigsionLayout, 0, wx.EXPAND|wx.LEFT, 10 )


        self.SetSizer( sideLayout )
        self.Layout()

        # Connect Events
        self.ISNB_kodu_atspauzdinimas.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Kurti_naujus_barkodus.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Iš_Klavetūros_Skaitytuvo.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Ieškoti_pagal_pavadinima.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Iš_CSV.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.Localioje_lenteje.Bind( wx.EVT_LEFT_DOWN, self.Click )
        self.m_staticText29.Bind( wx.EVT_LEFT_UP, self.version )

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


###########################################################################
## Class KurtiNaujusBarkodus
###########################################################################

class KurtiNaujusBarkodus ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.m_panel49 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizer135 = wx.BoxSizer( wx.VERTICAL )

        bSizer128 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText16 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        self.m_staticText16.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer128.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( bSizer128, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer129 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText63 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Kur isaugoti norimus failus"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText63.Wrap( -1 )

        bSizer129.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer129.Add( ( 20, 0), 0, 0, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self.m_panel49, wx.ID_ANY, _(u"/"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.m_textCtrl3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_textCtrl3.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer129.Add( self.m_textCtrl3, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer135.Add( bSizer129, 0, 0, 5 )


        bSizer135.Add( ( 0, 16), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer130 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText66 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Kiek sukurti barkodu"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText66.Wrap( -1 )

        bSizer130.Add( self.m_staticText66, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer130.Add( ( 55, 0), 0, 0, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self.m_panel49, wx.ID_ANY, _(u"50"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_textCtrl2.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer130.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer135.Add( bSizer130, 0, 0, 5 )


        bSizer135.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.m_button8 = wx.Button( self.m_panel49, wx.ID_ANY, _(u"Testi"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer135.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        self.m_panel49.SetSizer( bSizer135 )
        self.m_panel49.Layout()
        bSizer135.Fit( self.m_panel49 )
        mainLayout.Add( self.m_panel49, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.m_button8.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
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

        self.m_panel49 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizer135 = wx.BoxSizer( wx.VERTICAL )

        bSizer128 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText16 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        self.m_staticText16.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer128.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( bSizer128, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer130 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText66 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Iš kur norimus failua apimti"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText66.Wrap( -1 )

        bSizer130.Add( self.m_staticText66, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer130.Add( ( 16, 0), 0, 0, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self.m_panel49, wx.ID_ANY, _(u"/home/justpause/Programming/pyhton/KVM-bibliotekos-sistema/"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.m_textCtrl2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_textCtrl2.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer130.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer135.Add( bSizer130, 0, 0, 5 )


        bSizer135.Add( ( 0, 16), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer129 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText63 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Kur isaugoti norimus faila"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText63.Wrap( -1 )

        bSizer129.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer129.Add( ( 27, 0), 1, wx.EXPAND, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self.m_panel49, wx.ID_ANY, _(u"/home/justpause/Programming/pyhton/KVM-bibliotekos-sistema/"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.m_textCtrl3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_textCtrl3.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer129.Add( self.m_textCtrl3, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer135.Add( bSizer129, 0, 0, 5 )


        bSizer135.Add( ( 0, 16), 1, wx.EXPAND, 5 )

        self.m_button8 = wx.Button( self.m_panel49, wx.ID_ANY, _(u"Testi"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer135.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        self.m_panel49.SetSizer( bSizer135 )
        self.m_panel49.Layout()
        bSizer135.Fit( self.m_panel49 )
        mainLayout.Add( self.m_panel49, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.m_button8.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
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

        self.m_panel49 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizer135 = wx.BoxSizer( wx.VERTICAL )

        bSizer128 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText16 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        self.m_staticText16.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer128.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( bSizer128, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer130 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText66 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Iš kur norimus failua apimti"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText66.Wrap( -1 )

        bSizer130.Add( self.m_staticText66, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer130.Add( ( 16, 0), 0, 0, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self.m_panel49, wx.ID_ANY, _(u"/home/justpause/Programming/pyhton/KVM-bibliotekos-sistema"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.m_textCtrl2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_textCtrl2.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer130.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer135.Add( bSizer130, 0, 0, 5 )


        bSizer135.Add( ( 0, 16), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer129 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText63 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Kur isaugoti norimus faila"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText63.Wrap( -1 )

        bSizer129.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer129.Add( ( 27, 0), 1, wx.EXPAND, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self.m_panel49, wx.ID_ANY, _(u"/home/justpause/Programming/pyhton/KVM-bibliotekos-sistema"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.m_textCtrl3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_textCtrl3.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer129.Add( self.m_textCtrl3, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer135.Add( bSizer129, 0, 0, 5 )


        self.m_panel49.SetSizer( bSizer135 )
        self.m_panel49.Layout()
        bSizer135.Fit( self.m_panel49 )
        mainLayout.Add( self.m_panel49, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class IsKlavetūrosSkaitytuvo
###########################################################################

class IsKlavetūrosSkaitytuvo ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.m_panel49 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizer135 = wx.BoxSizer( wx.VERTICAL )

        bSizer128 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText16 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        self.m_staticText16.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer128.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( bSizer128, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer130 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText66 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Kur išaugoti norimus faila"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText66.Wrap( -1 )

        bSizer130.Add( self.m_staticText66, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer130.Add( ( 20, 0), 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self.m_panel49, wx.ID_ANY, _(u"/home/justpause/Programming/pyhton/KVM-bibliotekos-sistema"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.m_textCtrl2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_textCtrl2.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer130.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer135.Add( bSizer130, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( ( 0, 16), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer51 = wx.BoxSizer( wx.VERTICAL )


        bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer135.Add( bSizer51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer1301 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button81 = wx.Button( self.m_panel49, wx.ID_ANY, _(u"Skanuoti be išvedimo"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1301.Add( self.m_button81, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer1301.Add( ( 0, 0), 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button8 = wx.Button( self.m_panel49, wx.ID_ANY, _(u"Testi"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1301.Add( self.m_button8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer135.Add( bSizer1301, 0, wx.EXPAND, 5 )


        self.m_panel49.SetSizer( bSizer135 )
        self.m_panel49.Layout()
        bSizer135.Fit( self.m_panel49 )
        mainLayout.Add( self.m_panel49, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.m_button81.Bind( wx.EVT_LEFT_DOWN, self.file_free_scan )
        self.m_button8.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def file_free_scan( self, event ):
        event.Skip()

    def next( self, event ):
        event.Skip()

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class IsKlavetūrosSkaitytuvoEkranas
###########################################################################

class IsKlavetūrosSkaitytuvoEkranas ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.m_panel49 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        bSizer135 = wx.BoxSizer( wx.VERTICAL )

        bSizer128 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText16 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        self.m_staticText16.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer128.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( bSizer128, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer130 = wx.BoxSizer( wx.VERTICAL )

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.m_panel49, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,400 ), wx.dataview.DV_ROW_LINES )
        bSizer130.Add( self.m_dataViewListCtrl1, 0, wx.ALL, 5 )


        bSizer130.Add( ( 0, 64), 0, 0, 5 )

        self.m_panel27 = wx.Panel( self.m_panel49, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,100 ), wx.TAB_TRAVERSAL )
        self.m_panel27.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer130.Add( self.m_panel27, 1, wx.EXPAND, 5 )


        bSizer135.Add( bSizer130, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.m_panel49.SetSizer( bSizer135 )
        self.m_panel49.Layout()
        bSizer135.Fit( self.m_panel49 )
        mainLayout.Add( self.m_panel49, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class IeskotiPagalPavadinima
###########################################################################

class IeskotiPagalPavadinima ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        mainLayout = wx.BoxSizer( wx.VERTICAL )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        self.m_panel49 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel49.SetMaxSize( wx.Size( 800,-1 ) )

        bSizer135 = wx.BoxSizer( wx.VERTICAL )

        bSizer128 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText16 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        self.m_staticText16.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer128.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( bSizer128, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer135.Add( ( 0, 40), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer130 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText66 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"Kur isaugoti norimus faila"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText66.Wrap( -1 )

        bSizer130.Add( self.m_staticText66, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer130.Add( ( 20, 0), 0, 0, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self.m_panel49, wx.ID_ANY, _(u"/home/justpause/Programming/pyhton/KVM-bibliotekos-sistema"), wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        self.m_textCtrl2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_textCtrl2.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        bSizer130.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer135.Add( bSizer130, 0, 0, 5 )


        bSizer135.Add( ( 0, 16), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button8 = wx.Button( self.m_panel49, wx.ID_ANY, _(u"Testi"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer135.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        self.m_panel49.SetSizer( bSizer135 )
        self.m_panel49.Layout()
        bSizer135.Fit( self.m_panel49 )
        mainLayout.Add( self.m_panel49, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


        self.SetSizer( mainLayout )
        self.Layout()

        # Connect Events
        self.m_button8.Bind( wx.EVT_LEFT_DOWN, self.next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def next( self, event ):
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

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, _(u"Didzioji lentele"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        self.m_staticText16.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        mainLayout.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        mainLayout.Add( ( 0, 40), 0, 0, 5 )

        bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer30 = wx.BoxSizer( wx.VERTICAL )

        bSizer32 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText17 = wx.StaticText( self.m_panel15, wx.ID_ANY, _(u"Autorius"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        bSizer33.Add( self.m_staticText17, 0, wx.ALL, 5 )


        bSizer33.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText18 = wx.StaticText( self.m_panel15, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        bSizer33.Add( self.m_staticText18, 0, wx.ALL, 5 )


        self.m_panel15.SetSizer( bSizer33 )
        self.m_panel15.Layout()
        bSizer33.Fit( self.m_panel15 )
        bSizer32.Add( self.m_panel15, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_panel151 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer331 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText171 = wx.StaticText( self.m_panel151, wx.ID_ANY, _(u"Pavadinimas"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText171.Wrap( -1 )

        bSizer331.Add( self.m_staticText171, 0, wx.ALL, 5 )


        bSizer331.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText181 = wx.StaticText( self.m_panel151, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText181.Wrap( -1 )

        bSizer331.Add( self.m_staticText181, 0, wx.ALL, 5 )


        self.m_panel151.SetSizer( bSizer331 )
        self.m_panel151.Layout()
        bSizer331.Fit( self.m_panel151 )
        bSizer32.Add( self.m_panel151, 0, wx.EXPAND|wx.ALL, 5 )

        self.m_panel152 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer332 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText172 = wx.StaticText( self.m_panel152, wx.ID_ANY, _(u"Metai"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText172.Wrap( -1 )

        bSizer332.Add( self.m_staticText172, 0, wx.ALL, 5 )


        bSizer332.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText182 = wx.StaticText( self.m_panel152, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText182.Wrap( -1 )

        bSizer332.Add( self.m_staticText182, 0, wx.ALL, 5 )


        self.m_panel152.SetSizer( bSizer332 )
        self.m_panel152.Layout()
        bSizer332.Fit( self.m_panel152 )
        bSizer32.Add( self.m_panel152, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_panel153 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer333 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText173 = wx.StaticText( self.m_panel153, wx.ID_ANY, _(u"ISNB"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText173.Wrap( -1 )

        bSizer333.Add( self.m_staticText173, 0, wx.ALL, 5 )


        bSizer333.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText183 = wx.StaticText( self.m_panel153, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText183.Wrap( -1 )

        bSizer333.Add( self.m_staticText183, 0, wx.ALL, 5 )


        self.m_panel153.SetSizer( bSizer333 )
        self.m_panel153.Layout()
        bSizer333.Fit( self.m_panel153 )
        bSizer32.Add( self.m_panel153, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer30.Add( bSizer32, 1, wx.EXPAND, 5 )


        bSizer29.Add( bSizer30, 1, wx.EXPAND, 5 )

        bSizer31 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel14.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        bSizer54 = wx.BoxSizer( wx.VERTICAL )

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_ROW_LINES )
        bSizer54.Add( self.m_dataViewListCtrl1, 1, wx.EXPAND|wx.ALL, 5 )


        self.m_panel14.SetSizer( bSizer54 )
        self.m_panel14.Layout()
        bSizer54.Fit( self.m_panel14 )
        bSizer31.Add( self.m_panel14, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 25 )


        bSizer29.Add( bSizer31, 1, wx.EXPAND, 5 )


        mainLayout.Add( bSizer29, 1, wx.EXPAND, 5 )


        self.SetSizer( mainLayout )
        self.Layout()

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


###########################################################################
## Class PopUp
###########################################################################

class PopUp ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 480,320 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        bSizer102 = wx.BoxSizer( wx.VERTICAL )

        Titulas_BarkodasBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        Titulas_BarkodasBoxSizer.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        bSizer102.Add( Titulas_BarkodasBoxSizer, 1, wx.EXPAND, 5 )

        bSizer108 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel23.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        bSizer108.Add( self.m_panel23, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        bSizer110 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel28 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel28.SetBackgroundColour( wx.Colour( 233, 12, 0 ) )

        bSizer110.Add( self.m_panel28, 1, wx.ALL, 5 )

        self.m_panel29 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel29.SetBackgroundColour( wx.Colour( 65, 139, 36 ) )

        bSizer110.Add( self.m_panel29, 1, wx.ALL, 5 )


        bSizer108.Add( bSizer110, 0, wx.EXPAND, 5 )


        bSizer102.Add( bSizer108, 1, wx.EXPAND, 5 )

        bSizer1081 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel231 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel231.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        bSizer1081.Add( self.m_panel231, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        bSizer1101 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel281 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel281.SetBackgroundColour( wx.Colour( 233, 12, 0 ) )

        bSizer1101.Add( self.m_panel281, 1, wx.ALL, 5 )

        self.m_panel291 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel291.SetBackgroundColour( wx.Colour( 65, 139, 36 ) )

        bSizer1101.Add( self.m_panel291, 1, wx.ALL, 5 )


        bSizer1081.Add( bSizer1101, 0, wx.EXPAND, 5 )


        bSizer102.Add( bSizer1081, 1, wx.EXPAND, 5 )

        bSizer1082 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel232 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel232.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        bSizer1082.Add( self.m_panel232, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        bSizer1102 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel282 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel282.SetBackgroundColour( wx.Colour( 233, 12, 0 ) )

        bSizer1102.Add( self.m_panel282, 1, wx.ALL, 5 )

        self.m_panel292 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel292.SetBackgroundColour( wx.Colour( 65, 139, 36 ) )

        bSizer1102.Add( self.m_panel292, 1, wx.ALL, 5 )


        bSizer1082.Add( bSizer1102, 0, wx.EXPAND, 5 )


        bSizer102.Add( bSizer1082, 1, wx.EXPAND, 5 )

        bSizer1083 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel233 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel233.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        bSizer1083.Add( self.m_panel233, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        bSizer1103 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel283 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel283.SetBackgroundColour( wx.Colour( 233, 12, 0 ) )

        bSizer1103.Add( self.m_panel283, 1, wx.ALL, 5 )

        self.m_panel293 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel293.SetBackgroundColour( wx.Colour( 65, 139, 36 ) )

        bSizer1103.Add( self.m_panel293, 1, wx.ALL, 5 )


        bSizer1083.Add( bSizer1103, 0, wx.EXPAND, 5 )


        bSizer102.Add( bSizer1083, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer102 )
        self.Layout()

    def __del__( self ):
        pass

    # Virtual image path resolution method. Override this in your derived class.
    def img_path( self, bitmap_path ):
        return bitmap_path


