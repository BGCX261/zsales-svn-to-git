#! /usr/bin/python
#-*- coding:utf-8 -*-

import wx
import kinterbasdb as fdb
fdb.init(type_conv=200)

import gui

class zsalse_frame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, -1, title)

class MyApp(wx.App):
	def OnInit(self):
		frame = zsalse_frame(None, u"Z协作营销系统")
		self.SetTopWindow(frame)

		frame.Show(True)
		return True

app = MyApp(redirect=False)
app.MainLoop()
