import tkinter as tk
from tkinter import StringVar
import subprocess
import re
import pandas as pd
import json
from subprocess_func.scraper import Scraper
from subprocess_func.generator import Generator
from subprocess_func.postman import WordPressMiddleMan
from subprocess_func.constant import *

# Global variables:
input_csv_path = "storage/data.csv"
store_GenContent_path = "storage/generated/gen1.pkl"
post_status = "draft"
color_code = {
    "warning": "#F6FDC3",
    "success": "#d1e7dd",
    "fail": "#F28585",
    "default": "#F0EBE3"
}


def execute_scraping():
    keyword = keyword_entry.get()
    # keyword = re.sub(r'[^A-Za-z\s]', '', keyword_entry.get())
    max_article = max_article_entry.get()    # Get the max_article entered by the user
    # Run the say_hello.py script with user input as arguments
    execution_status = Scraper(keyword, max_article)
    # Update messages
    message = "Success!" if execution_status else "Fail!"
    color = color_code['success'] if execution_status else color_code['fail']
    message_label.config(text="SCRAPING STATUS: " + message, bg = color)


def execute_generating():
    generator = Generator(input_csv_path = input_csv_path)
    execution_status = generator.start_generate(store_path = store_GenContent_path)
    message = "Success!" if execution_status else "Fail!"
    color = color_code['success'] if execution_status else color_code['fail']
    message_label.config(text="GENERATION STATUS: " + message, bg = color)

def execute_upload():
    WPMiddleman = WordPressMiddleMan(input_path = store_GenContent_path, status = post_status)
    execution_status = WPMiddleman.create_draft()
    
    message = "Success!" if execution_status else "Fail!"
    color = color_code['success'] if execution_status else color_code['fail']
    message_label.config(text= "UPLOADING STATUS: " + message, bg = color)




# Load font from file
window = tk.Tk()
window.title("Test gui")
window.geometry("800x300")

custom_font = ("Roboto", 9, "bold")

window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)

window.rowconfigure(1,weight=4)
window.rowconfigure(2,weight=2)
window.rowconfigure(3,weight=2)





# frame
frame = tk.Frame(window)
frame.grid(row=1, column=1, columnspan=3, sticky="ns")
frame.columnconfigure(1, weight = 4)
frame.columnconfigure(2, weight = 6)
frame.rowconfigure(1,weight=1)
frame.rowconfigure(2,weight=1)

# input label
keyword_label = tk.Label(frame, text = "Search Keywords:", font=("Roboto", 14))
max_article_label = tk.Label(frame, text = "Max articles:", font=("Roboto", 14))
keyword_label.grid(row=1, column=1, sticky="sw",pady=5)
max_article_label.grid(row=2, column=1, sticky="nw",pady=5)
# input entry
keyword_entry = tk.Entry(frame, textvariable = StringVar(window, value = None),font=("Roboto", 14), width=32)
max_article_entry =  tk.Entry(frame,font=("Roboto", 14), width=32)
keyword_entry.grid(row=1, column=2, sticky="sw", pady=5 )
max_article_entry.grid(row=2, column=2, sticky="nw",pady=5)




# message 

message_label = tk.Label(window, text = "Ready to receive command", font=("Roboto", 12), bg = "#F0EBE3")
message_label.grid(row =2, column=2, sticky="swne")







# button
button1 = tk.Button(window, background = '#378CE7', width = 12, height=2, text = "Scrape", font = custom_font, fg="white", command= execute_scraping)
button2 = tk.Button(window, background = '#378CE7', width = 12, height=2, text = "Generate", font = custom_font, fg="white", command= execute_generating)
button3 = tk.Button(window, background = '#378CE7', width = 12, height=2, text = "Upload", font = custom_font, fg="white", command= execute_upload)

button1.grid(row=3, column=1)
button2.grid(row=3, column=2)
button3.grid(row=3, column=3)










window.mainloop()

