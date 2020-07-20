from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class CalcGridlayout(GridLayout):

    def Calculate(self,Calculation):

        if Calculation:
            try:
                self.display.text =str(eval(Calculation))
            except Exception:
                self.display.text ="Error"

class CalculatorApp(App):
    def build(self):
        return CalcGridlayout()

if __name__ == "__main__":
    CalculatorApp().run()