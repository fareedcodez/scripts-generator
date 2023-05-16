import argparse
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("KEY")  

# Pre-defined script templates
templates = {
    "1": {
        "prompt": "Generate a Django model for a blog post with fields title, content, and pub_date.",
        "template": """
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
"""
    },
    "2": {
        "prompt": "Scrape the titles and URLs of the latest news articles from a website.",
        "template": """
import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com/news'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('article')

for article in articles:
    title = article.find('h2').text.strip()
    url = article.find('a')['href']
    print('Title:', title)
    print('URL:', url)
    print()
"""
    }
}

def generate_script(prompt, file_name):
    try:
        # Configure API request
        headers_data = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }
        request_data = {
            "model": "text-davinci-003",
            "prompt": f"Write a Python script {prompt}",
            "max_tokens": 1500,
            "temperature": 0.5
        }

        # Send API request
        response = requests.post(api_endpoint, headers=headers_data, json=request_data)

        if response.status_code == 200:
            # Extract the generated script from the API response
            response_text = response.json()["choices"][0]["text"]

            # Save the generated script to a file
            with open(file_name, 'w') as file:
                file.write(response_text)

            print("Script generated and saved successfully.")
        else:
            print(f'Response failed with status {str(response.status_code)}')

    except requests.exceptions.RequestException as e:
        print("Network error occurred. Please check your internet connection.")
    except KeyError as e:
        print("Invalid API response received. Please try again later.")
    except FileNotFoundError as e:
        print("The .env file is missing. Make sure to set up the required environment variables.")
    except Exception as e:
        print("An error occurred. Please try again later.")

def delete_script(file_name):
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
            print("Script deleted successfully.")
        else:
            print("Script does not exist.")

    except FileNotFoundError as e:
        print("File not found.")
    except Exception as e:
        print("An error occurred. Please try again later.")

def edit_script(file_name):
    try:
        if os.path.exists(file_name):
            # Open the script file for editing
            os.system(f"start {file_name}")
        else:
            print("Script does not exist.")

    except Exception as e:
        print("An error occurred. Please try again later.")

        


def interactive_mode():
    print("Interactive Mode")
    print("Enter 'q' to quit.")

    while True:
        prompt = input("Enter prompt: ")

        if prompt == "q":
            break
        file_name = input("Enter file name: ")

        if file_name == "q":
            break

        generate_script(prompt, file_name)

        action = input("Do you want to delete or edit any scripts? (y/n): ")

        if action.lower() == "y":
            edit_delete_option = input("Enter 'delete' to delete a script, 'edit' to edit a script: ")

            if edit_delete_option.lower() == "delete":
                delete_file_name = input("Enter the name of the script you want to delete: ")
                delete_script(delete_file_name)
            elif edit_delete_option.lower() == "edit":
                edit_file_name = input("Enter the name of the script you want to edit: ")
                edit_script(edit_file_name)



def single_prompt_mode(prompt, file_name):
    generate_script(prompt, file_name)

    action = input("Do you want to delete or edit the script? (y/n): ")

    if action.lower() == "y":
        edit_delete_option = input("Enter 'delete' to delete the script, 'edit' to edit the script: ")

        if edit_delete_option.lower() == "delete":
            delete_file_name = input("Enter the name of the script you want to delete: ")
            delete_script(delete_file_name)
        elif edit_delete_option.lower() == "edit":
            edit_file_name = input("Enter the name of the script you want to edit: ")
            edit_script(edit_file_name)

def main():
    request_parser = argparse.ArgumentParser(description="Script Generator")
    request_parser.add_argument("-p", "--prompt", help="The prompt to send to the OpenAI API")
    request_parser.add_argument("-f", "--file", help="The file name to save the generated script")
    request_parser.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode")
    user_prompt = request_parser.parse_args()

    if user_prompt.interactive:
        interactive_mode()
    elif user_prompt.prompt and user_prompt.file:
        single_prompt_mode(user_prompt.prompt, user_prompt.file)
    else:
        request_parser.print_help()

if __name__ == "__main__":
    main()

