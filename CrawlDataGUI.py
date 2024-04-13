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

def execute_scraping():
    keyword = keyword_entry.get()
    # keyword = re.sub(r'[^A-Za-z\s]', '', keyword_entry.get())
    max_article = max_article_entry.get()    # Get the max_article entered by the user
    # Run the say_hello.py script with user input as arguments
    config_text = Scraper(keyword, max_article)
    # Update messages
    scrape_label.config(text = config_text)
    
def execute_generating():
    generator = Generator(input_csv_path = input_csv_path)
    execution_status = generator.start_generate(store_path = store_GenContent_path)
    message = "Success!" if execution_status else "Fail!"
    scrape_label.config(text="GENERATION STATUS: " + message)

def execute_upload():
    WPMiddleman = WordPressMiddleMan(input_path = store_GenContent_path, status = post_status)
    upload_status = WPMiddleman.create_draft()
    message = "Success!" if upload_status else "Fail!"
    scrape_label.config(text="UPLOAD STATUS: " + message)


root = tk.Tk()
root.title("WordPress's SEO OpenaiAPI Wrapper")

# Create input field for the user's name
keyword_label = tk.Label(root, text="Enter keyword:")
keyword_label.grid(row=0, column=0)
keyword_variable = StringVar(root, value = None)

keyword_entry = tk.Entry(root, textvariable = keyword_variable)
keyword_entry.grid(row=0, column=1)

# Create input field for the user's max_article
max_article_label = tk.Label(root, text="What is the max number of articles:")
max_article_label.grid(row=1, column=0)

max_article_entry = tk.Entry(root)
max_article_entry.grid(row=1, column=1)


# Create a label to display the greeting messmax_article
scrape_label = tk.Label(root, text="")
scrape_label.grid(row=3, column=0)

# Create a button to trigger the greeting
scrape_button = tk.Button(root, text="Scrape", command = execute_scraping)
scrape_button.grid(row=2, column=1)

# Trigger chatgpt
gpt_button = tk.Button(root, text = "Generate Post", command = execute_generating)
gpt_button.grid(row=3, column=1)

# Trigger chatgpt
upload_button = tk.Button(root, text = "Upload", command = execute_upload)
upload_button.grid(row=4, column=1)

root.mainloop()
