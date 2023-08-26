import wx
from src.calculator import Calculator

def main():
    app = wx.App(False)
    Calculator(None, title='Simple Calculator')
    app.MainLoop()

if __name__ == "__main__":
    main()
