import wx

app = wx.App()
# 框架，窗口
win = wx.Frame(None, title='Simple Editor')

# 按钮
loadButton = wx.Button(win, label='Open', pos=(225, 5), size=(80, 25))
saveButton = wx.Button(win, label='Save', pos=(315, 5), size=(80, 25))

# 文本框
filename = wx.TextCtrl(win, pos=(5, 5), size=(210, 25))
contents = wx.TextCtrl(win, pos=(5, 35), size=(390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)

# 显示窗口
win.Show()

# 执行图形界面事件循环
app.MainLoop()

