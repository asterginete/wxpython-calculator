import wx
from src.history import HistoryPanel
from src.logic.core import BasicCalculator
from src.utils.helpers import safe_eval

class CalculatorApp(wx.Frame):
    def __init__(self, parent, title):
        super(CalculatorApp, self).__init__(parent, title=title, size=(350, 600))

        self.basic_calculator = BasicCalculator()

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Display for calculations
        self.text_display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.text_display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)

        # Buttons grid
        grid_box = wx.GridSizer(5, 4, 10, 10)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        for label in buttons:
            button = wx.Button(self, label=label)
            self.Bind(wx.EVT_BUTTON, self.OnButtonPress, button)
            grid_box.Add(button, 1, wx.EXPAND)

        vbox.Add(grid_box, proportion=1, flag=wx.EXPAND)

        # History Panel
        self.history_panel = HistoryPanel(self)
        vbox.Add(self.history_panel, 1, wx.EXPAND)

        self.SetSizer(vbox)

    def OnButtonPress(self, event):
        label = event.GetEventObject().GetLabel()

        if label == '=':
            expression = self.text_display.GetValue()
            result = safe_eval(expression)
            self.text_display.SetValue(str(result))
            # Update the history
            self.history_panel.add_entry(f"{expression} = {result}")
        elif label == 'C':
            self.text_display.SetValue('')
        else:
            current_value = self.text_display.GetValue()
            new_value = current_value + label
            self.text_display.SetValue(new_value)
