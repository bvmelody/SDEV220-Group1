
"""
Project Name: Group2Project.py
Author: Brenden Melody, Wyatt Berry, Kevin Ramirez, Darrell Cassidy
Date last updated: 5/10/2025
Description: Program is designed to be a metric/imperial notation converter
"""

from logging import root
import tkinter as tk

"""
This module actually initializes the main menu with the 3 main buttons to start the program
"""

def main():
    mainMenu = tk.Tk()
    mainMenu.title("Math Converter")
    mainMenu.geometry("500x500")
    mainMenu['background'] = "WHITE"
    
    # creating welcome label and buttons
    welcomeMessage = tk.Label(mainMenu, text="Welcome to our Metric/Imperial Converter!")
    imperialToMetric = tk.Button(mainMenu, text="Imperial to Metric")
    metricToImperial = tk.Button(mainMenu, text="Metric to Imperial")
    settingsButton = tk.Button(mainMenu, text ="Settings")
    exitButton = tk.Button(mainMenu, text="Exit", command=mainMenu.quit)

    
    welcomeMessage.pack()
    imperialToMetric.pack()
    metricToImperial.pack()
    settingsButton.pack()
    exitButton.pack()
    mainMenu.mainloop()


if __name__ == '__main__':
    main()
