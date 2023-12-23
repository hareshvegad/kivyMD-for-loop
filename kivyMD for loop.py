from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from datetime import datetime

class ProductDataEntry(GridLayout):
    def __init__(self, **kwargs):
        super(ProductDataEntry, self).__init__(**kwargs)
        self.cols = 3

        self.product_names = ["p1", "p2", "p3", "p4", "p5"]

        self.product_data = {}
        
        self.title = "card 1"

        self.quantity_inputs = []
        self.weight_inputs = []

        for product_name in self.product_names:
            self.add_widget(Label(text=product_name))

            quantity_input = TextInput(hint_text=f'Quantity for {product_name}')
            weight_input = TextInput(hint_text=f'Weight for {product_name}')

            self.quantity_inputs.append(quantity_input)
            self.weight_inputs.append(weight_input)

            self.add_widget(quantity_input)
            self.add_widget(weight_input)

        submit_button = Button(text="Submit")
        submit_button.bind(on_release=self.show_data)
        self.add_widget(submit_button)

    def show_data(self, instance):
        self.product_data = {}
        self.product_data["Title"] = self.title
        self.product_data["Date"] = datetime.now().strftime('%d-%m-%Y')

        for i in range(len(self.product_names)):
            product_name = self.product_names[i]
            quantity = self.quantity_inputs[i].text
            weight = self.weight_inputs[i].text

            if quantity or weight: 
                    self.product_data[product_name] = {
                        "Quantity": quantity,
                        "Weight": weight
                    }

        if self.product_data:
            print(self.product_data)

class ProductDataApp(App):
    def build(self):
        return ProductDataEntry()

if __name__ == '__main__':
    ProductDataApp().run()
