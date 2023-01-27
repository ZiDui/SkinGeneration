# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"自动生成皮肤  籽怼", pos = wx.DefaultPosition, size = wx.Size( 300,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar3 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"退出(&X)", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menubar3.Append( self.m_menu1, u"文件(&F)" )

		self.m_menu3 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"帮助(&H)", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"关于(&A)", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem3 )

		self.m_menubar3.Append( self.m_menu3, u"帮助(&H)" )

		self.SetMenuBar( self.m_menubar3 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"性别：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"男", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_radioBtn1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"女", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_radioBtn2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer1, 1, wx.EXPAND, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"细手臂/粗手臂：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer2, 1, wx.EXPAND, 5 )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"头发颜色：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer3.Add( self.m_staticText7, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_colourPicker1 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gbSizer3.Add( self.m_colourPicker1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer3, 1, wx.EXPAND, 5 )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"脸部颜色：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gbSizer4.Add( self.m_staticText8, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_colourPicker2 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gbSizer4.Add( self.m_colourPicker2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer4, 1, wx.EXPAND, 5 )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"身体颜色：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gbSizer5.Add( self.m_staticText9, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_colourPicker3 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gbSizer5.Add( self.m_colourPicker3, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer5, 1, wx.EXPAND, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn1.SetValue( True )
		bSizer2.Add( self.m_toggleBtn1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


