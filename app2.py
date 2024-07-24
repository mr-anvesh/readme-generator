import requests
import openai
import os
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

load_dotenv()

# Function to fetch files from GitHub repository
def fetch_github_files(user, repo, token=None):
    base_url = f"https://api.github.com/repos/{user}/{repo}/contents/"
    headers = {'Authorization': f'token {token}'} if token else {}
    
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Function to generate README content using OpenAI GPT-4 Turbo
def generate_readme_content(file_data):
    file_list = "\n".join([f"- {file_info['name']}" for file_info in file_data])
    prompt = f"""
    I have the following files in my GitHub repository:
    {file_list}
    Could you help me create a README.md file that describes the project, lists the files, and provides a brief description for each?

    Example:
    # Project Title
    This project is about...

    ## Files
    - file1.py: Description of file1
    - file2.py: Description of file2
    """

    response = openai.chat.completions.create(model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are an expert copywriter whose task is to create an extraordinary copy of Readme.md file."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=300)
    return response.choices[0].message.content.strip()

# Function to create README.md file
def create_readme(content, output_path="README.md"):
    with open(output_path, "w") as readme:
        readme.write(content)

# Function to parse GitHub URL to extract username and repository name
def parse_github_url(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')
    if len(path_parts) >= 2:
        user = path_parts[0]
        repo = path_parts[1]
        return user, repo
    else:
        raise ValueError("Invalid GitHub URL format. Expected format: https://github.com/username/repository")

if __name__ == "__main__":
    # Get GitHub URL from user input
    github_url = input("Enter GitHub repository URL: ")
    
    try:
        user, repo = parse_github_url(github_url)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    
    token = os.getenv("GITHUB_ACCESS_TOKEN")
    if not token:
        token = input("Enter Github Personal Access Token: ")
    
    # Fetch OpenAI API key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        openai.api_key = input("Enter OpenAI API key: ")

    try:
        # Fetch file data from GitHub repository
        file_data = fetch_github_files(user, repo, token)
        
        # Generate README content using OpenAI GPT-4 Turbo
        readme_content = generate_readme_content(file_data)
        
        # Create README.md file
        create_readme(readme_content)
        
        print("README.md has been created successfully.")
    except Exception as e:
        print(f"Error: {e}")
