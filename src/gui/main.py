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

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 256,-1 ), wx.BORDER_NONE )
        self.m_panel1.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        self.Titulas_Barkodas = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Barkodas"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.Titulas_Barkodas.Wrap( -1 )

        self.Titulas_Barkodas.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Playfair Display" ) )

        bSizer19.Add( self.Titulas_Barkodas, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 25 )


        bSizer9.Add( bSizer19, 0, wx.EXPAND, 5 )

        bSizer20 = wx.BoxSizer( wx.VERTICAL )

        self.Barkodai = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Barkodai"), wx.DefaultPosition, wx.Size( 256,-1 ), 0 )
        self.Barkodai.Wrap( -1 )

        self.Barkodai.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer20.Add( self.Barkodai, 0, wx.ALL, 5 )

        bSizer21 = wx.BoxSizer( wx.VERTICAL )

        self.ISNB_kodu_atspauzdinimas = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"ISNB kodu atspauzdinimas"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ISNB_kodu_atspauzdinimas.Wrap( -1 )

        self.ISNB_kodu_atspauzdinimas.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer21.Add( self.ISNB_kodu_atspauzdinimas, 0, wx.ALL, 5 )

        self.Kurti_naujus_barkodus = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Kurti naujus barkodus"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Kurti_naujus_barkodus.Wrap( -1 )

        self.Kurti_naujus_barkodus.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer21.Add( self.Kurti_naujus_barkodus, 0, wx.ALL, 5 )


        bSizer20.Add( bSizer21, 0, wx.EXPAND|wx.LEFT, 10 )


        bSizer20.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Knygu_surašimas = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Knygu surašimas"), wx.DefaultPosition, wx.Size( 256,-1 ), 0 )
        self.Knygu_surašimas.Wrap( -1 )

        self.Knygu_surašimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer20.Add( self.Knygu_surašimas, 0, wx.ALL, 5 )

        bSizer22 = wx.BoxSizer( wx.VERTICAL )

        self.Iš_Klavetūros_Skaitytuvo = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Iš Klavetūros / Skaitytuvo"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Iš_Klavetūros_Skaitytuvo.Wrap( -1 )

        self.Iš_Klavetūros_Skaitytuvo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer22.Add( self.Iš_Klavetūros_Skaitytuvo, 0, wx.ALL, 5 )

        self.Ieškoti_pagal_pavadinima = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Ieškoti pagal pavadinima"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Ieškoti_pagal_pavadinima.Wrap( -1 )

        self.Ieškoti_pagal_pavadinima.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer22.Add( self.Ieškoti_pagal_pavadinima, 0, wx.ALL, 5 )

        self.Iš_CSV = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Iš CSV"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Iš_CSV.Wrap( -1 )

        self.Iš_CSV.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer22.Add( self.Iš_CSV, 0, wx.ALL, 5 )


        bSizer20.Add( bSizer22, 0, wx.EXPAND|wx.LEFT, 10 )


        bSizer20.Add( ( 0, 5), 1, wx.EXPAND, 5 )

        self.Patikrinimas = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Patikrinimas"), wx.DefaultPosition, wx.Size( 256,-1 ), 0 )
        self.Patikrinimas.Wrap( -1 )

        self.Patikrinimas.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer20.Add( self.Patikrinimas, 0, wx.ALL, 5 )

        bSizer23 = wx.BoxSizer( wx.VERTICAL )

        self.Localioje_lenteje = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Localioje lenteje"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Localioje_lenteje.Wrap( -1 )

        self.Localioje_lenteje.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer23.Add( self.Localioje_lenteje, 0, wx.ALL, 5 )

        self.Google_sheets_lenteliaja = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Google sheets lenteliaja"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Google_sheets_lenteliaja.Wrap( -1 )

        self.Google_sheets_lenteliaja.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Inter" ) )

        bSizer23.Add( self.Google_sheets_lenteliaja, 0, wx.ALL, 5 )


        bSizer20.Add( bSizer23, 0, wx.EXPAND|wx.LEFT, 10 )


        bSizer9.Add( bSizer20, 0, wx.EXPAND|wx.LEFT, 10 )


        self.m_panel1.SetSizer( bSizer9 )
        self.m_panel1.Layout()
        bSizer2.Add( self.m_panel1, 0, wx.EXPAND, 0 )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_NONE )
        self.m_panel2.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_bitmap1 = wx.StaticBitmap( self.m_panel2, wx.ID_ANY, wx.Bitmap( u"Vector.png", wx.BITMAP_TYPE_ANY ), wx.Point( 10,-1 ), wx.DefaultSize, 0 )
        gSizer2.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.m_panel2.SetSizer( gSizer2 )
        self.m_panel2.Layout()
        gSizer2.Fit( self.m_panel2 )
        bSizer2.Add( self.m_panel2, 1, wx.EXPAND, 0 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.HORIZONTAL )

    def __del__( self ):
        pass


