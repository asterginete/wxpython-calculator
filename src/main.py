import wx
from src.gui.calculator import CalculatorApp

def main():
    app = wx.App(False)
    CalculatorApp(None, title='Advanced Calculator')
    app.MainLoop()

if __name__ == "__main__":
    main()
