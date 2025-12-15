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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Pagrindinis"), pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_treeCtrl1 = wx.TreeCtrl( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 256,690 ), wx.TR_DEFAULT_STYLE )
        fgSizer2.Add( self.m_treeCtrl1, 0, wx.ALL, 5 )


        self.SetSizer( fgSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


