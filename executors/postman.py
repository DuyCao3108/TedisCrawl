import requests
import base64
import json
from executors.constant import AUTHORIZATION, WORDPRESS_URL, UPLOAD_FILE_FORMATS
import pickle
import glob


class WordPressMiddleMan():
    def __init__(self, dir_path: str, status: str) -> None:
        self.dir_path = dir_path
        self.status = status
        self.header = {
            "Content-Type": "application/json",
            "User-Agent": "insomnia/8.6.1",
            "Authorization": AUTHORIZATION
        }
        self.url = WORDPRESS_URL

    def start_uploading(self) -> None:
        file_list = self.loading_dir()
        file_list_length = len(file_list)

        print(file_list)
        print(file_list_length)
        
        if file_list_length == 0: return False
        elif file_list_length >= 1: 
            status = self.create_drafts(file_list)
            return status

    def loading_dir(self):
        # Define the directory path
        directory_path = self.dir_path
        # Define the file format you're interested in (e.g., txt, csv, jpg)
        file_formats = UPLOAD_FILE_FORMATS  # Change this to the desired format, e.g., '*.csv' for CSV files
        # Create a file pattern using the directory path and file format
        file_list = []
        for file_format in file_formats:
            file_pattern = directory_path + file_format
            file_list += glob.glob(file_pattern)
        return file_list
    
    def create_drafts(self, file_list):
        for file in file_list:
            print(f"processing {file}")

            file_content = open(file, "r").read()
            payload = {
                    "title": f"Title for {file}",
                    "content": file_content,
                    "status": "draft"
            }
            requests.request("POST", self.url, json = payload, headers = self.header)

            print(f"done {file}")
        return True

