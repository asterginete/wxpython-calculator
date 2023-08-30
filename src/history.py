import wx

class HistoryPanel(wx.Panel):
    def __init__(self, parent):
        super(HistoryPanel, self).__init__(parent)

        self.history = []
        self.listbox = wx.ListBox(self, style=wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.on_item_double_click, self.listbox)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.listbox, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def add_entry(self, entry):
        self.history.append(entry)
        self.listbox.Insert(entry, 0)

    def on_item_double_click(self, event):
        selected_entry = self.listbox.GetString(event.GetSelection())
        wx.PostEvent(self.GetParent(), wx.CommandEvent(wx.EVT_TEXT.typeId, self.GetParent().text_display.GetId()))
        self.GetParent().text_display.SetValue(selected_entry.split('=')[0].strip())
