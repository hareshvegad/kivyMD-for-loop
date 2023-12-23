# kivyMD-for-loop
kivyMD for loop this code get data in for loop working with kivyMD

Product Data Entry App

This Python script utilizes the Kivy framework to create a simple data entry application for product information. Users can input quantities and weights for different products and submit the data. The entered information is then displayed along with the title and date.
Prerequisites

    Python 3.x
    Kivy library (pip install kivy)

Usage

    Install the required dependencies:

    bash

pip install kivy

Run the script:

bash

    python script_name.py

    Enter the quantity and weight for each product in the provided text input fields.

    Click the "Submit" button to display the entered data, including the title and date, in the console.

Code Explanation
ProductDataEntry Class

    Inherits from Kivy's GridLayout.
    Initializes with a grid layout of 3 columns.
    Provides a list of product names and initializes dictionaries to store product data.
    Creates input fields for quantity and weight for each product.
    Implements a show_data method to gather and display entered data.

ProductDataApp Class

    Inherits from Kivy's App class.
    Implements the build method to return an instance of the ProductDataEntry class.

Main Execution

    Checks if the script is executed as the main module.
    Creates an instance of the ProductDataApp class and runs the application.

Note

    Ensure that Kivy is properly installed before running the script.
    Customize the product names, title, and any other aspects of the UI as needed.
    The entered data is currently printed to the console; you can modify the show_data method to save the data to a file or perform other actions based on your requirements.
