import tkinter as tk
from tkinter import StringVar
import subprocess
import re


def execute_scraping():
    keyword = keyword_entry.get()
    # keyword = re.sub(r'[^A-Za-z\s]', '', keyword_entry.get())
    max_article = max_article_entry.get()    # Get the max_article entered by the user
    # Run the say_hello.py script with user input as arguments
    result = subprocess.run(["python", "./CrawlMedicalPost/main.py", keyword, max_article])
    if result.returncode == 0:
        scrape_label.config(text='Subprocess ran successfully')
    else:
        scrape_label.config(text='Subprocess failed with error')

root = tk.Tk()
root.title("Greeting App")

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
scrape_label.grid(row=3, column=0, columnspan=2)

# Create a button to trigger the greeting
scrape_button = tk.Button(root, text="Scrape", command = execute_scraping)
scrape_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
