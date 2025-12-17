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

        fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 256,700 ), wx.BORDER_NONE )
        self.m_panel1.SetBackgroundColour( wx.Colour( 201, 201, 201 ) )

        fgSizer2.Add( self.m_panel1, 0, wx.EXPAND, 0 )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,700 ), wx.BORDER_NONE )
        self.m_panel2.SetBackgroundColour( wx.Colour( 217, 217, 217 ) )

        fgSizer2.Add( self.m_panel2, 1, wx.EXPAND, 0 )


        self.SetSizer( fgSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


