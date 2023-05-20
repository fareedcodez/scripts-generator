# Script Generator

![OpenAI](https://img.shields.io/badge/OpenAI-API-1B1B1B?logo=openai)

This script utilizes the power of the OpenAI API to generate Python scripts based on user prompts. It provides an interactive mode for generating scripts on-the-fly and a single-prompt mode for generating a script with a specific prompt.

## Features

- Generate Python scripts with custom prompts.
- Choose from pre-defined script templates or provide your own prompt.
- Save generated scripts to files for easy access.
- Manage scripts by deleting or editing existing ones.
- Interactive mode for convenient script generation.
- Single-prompt mode for quick script generation.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed
- `requests` library installed (`pip install requests`)
- `dotenv` library installed (`pip install python-dotenv`)
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/script-generator.git

## Setup

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/script-generator.git


2. Install the required dependencies:

      pip install -r requirements.txt

Create a .env file in the project root directory and add the following content:

         KEY=<your_openai_api_key>

Replace <your_openai_api_key> with your OpenAI API key.

## Usage

- Command-line Interface
- 
To generate a script using the command-line interface, use the following command

python script_generator.py -p "<prompt>" -f "<file_name>"

   Replace <prompt> with the prompt for generating the script, and <file_name> with the desired name of the output file.

- Interactive Mode
   
To run the script in interactive mode, use the following command:
   
       python script_generator.py -i
   
In interactive mode, you will be prompted to enter the prompt and file name for generating the script. You can also choose to delete or edit any generated scripts.
   
   ## Examples
   Here are a few examples of prompts you can try:

   Generate a Django model for a blog post with fields title, content, and pub_date.
   Scrape the titles and URLs of the latest news articles from a website.
   Create a Python script that calculates the Fibonacci sequence up to a given number.
   Feel free to experiment with different prompts and explore the possibilities!

## Contributing
   
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.


## Acknowledgments
   
This script was developed using the OpenAI API, which provides powerful language generation capabilities. Special thanks to the OpenAI team for their amazing work!

## Contact
   
For any inquiries or feedback, please contact sittangwesa6@gmail.com

