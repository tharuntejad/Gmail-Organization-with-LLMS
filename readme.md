
# Automated Gmail organization with llms (langchain , ollama, openai )
## Overview
This project is an intelligent Gmail inbox management tool that leverages language models (LLMs)
to automatically categorize and manage your emails. The application fetches emails from your Gmail
account, categorizes them into predefined categories, and performs specific actions such as marking them as 
read, moving them to folders, or deleting them based on your preferences.

## Features
- **Automated Email Fetching:** Connects to your Gmail account and retrieves emails from specified folders.
- **Intelligent Categorization:** Uses an LLM to categorize emails based on content.
- **Automated Actions:** Performs actions such as sorting, marking as read, or deleting emails based on the assigned category.
- **Customizable:** Easily adjust categories, actions, and settings via the `constants.py` file.

## Prerequisites
- A Gmail account with 2-Factor Authentication enabled.
- An application-specific password for Gmail access.
- Ollama installed locally or an OpenAI API key for using the LLM.
- Python 3.8+ with necessary dependencies (listed in `requirements.txt`).

## Installation & usage
1. Clone the repository:
   ```bash
   git clone https://github.com/tharuntejad/Gmail-Organization-with-LLMS
   cd gmail-email-management
   ```

2. View main.ipynb file for step by step instructions to run the code.

3. The application will fetch emails, categorize them, and perform the specified actions. Logs and metrics will be displayed in the console.

## Customization
- **Categories and Actions:** Modify the categories and actions in `constants.py` to suit your email management needs.
- **Model Selection:** Choose between using Ollama or OpenAI models for categorization.

## License 
This project is provided as-is for personal and educational use. Feel free to use, modify, and share the code as 
you like. However, be aware that some of the dependencies, including the LLMs (such as those from OpenAI or Ollama),
are governed by their own licenses and terms of service. Please ensure you comply with the licensing requirements
of any third-party tools, libraries, or models used in this project.
