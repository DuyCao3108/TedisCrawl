import requests
import base64
import json
from subprocess_func.constant import AUTHORIZATION, WORDPRESS_URL
import pickle

class WordPressMiddleMan():
    def __init__(self, input_path: str, status: str) -> None:
        self.input_path = input_path
        self.status = status
        self.header = {
            "Content-Type": "application/json",
            "User-Agent": "insomnia/8.6.1",
            "Authorization": AUTHORIZATION
        }
        self.url = WORDPRESS_URL

    def create_draft(self) -> None:
        try:
            with open(self.input_path, "rb") as file:
                input_dict = pickle.load(file)
                payload = {
                    "title": input_dict['title'],
                    "content": input_dict['content'],
                    "status": "draft"
                } 
                requests.request("POST", self.url, json = payload, headers = self.header)
                return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False

    def upload(self):
        pass