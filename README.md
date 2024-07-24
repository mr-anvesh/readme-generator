
# GitHub README Generator

This project is a Python script that fetches files from a GitHub project repository and generates a `README.md` file using OpenAI's GPT-4o model.

## Features

- Fetches files from a specified GitHub repository.
- Generates a `README.md` file with a description of the project and its files.
- Utilizes the OpenAI GPT-4 Turbo model to generate descriptive content.

## Prerequisites

- Python 3.6 or higher
- The `requests` library
- The `openai` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mr-anvesh/readme-generator.git
    cd readme-generator
    ```

2. Install the required libraries:
    ```bash
    pip install requests openai
    ```

## Usage

1. Run the script:
    ```bash
    python generate_readme.py
    ```

2. Enter the GitHub repository URL when prompted. For example:
    ```
    Enter GitHub repository URL: https://github.com/yourusername/yourrepository
    ```

3. Enter your GitHub Personal Access token.
    ```
    Enter GitHub token: your_github_token
    ```

4. Enter your OpenAI API key. This can be set as an environment variable (`OPENAI_API_KEY`) or entered when prompted:
    ```
    Enter OpenAI API key: your_openai_api_key
    ```

5. The script will generate a `README.md` file with content created by GPT-4o based on the files in the repository.

## Example

Here is an example of how the generated `README.md` file might look:

```
# Project Title
This project is about...

## Files
- file1.py: Description of file1
- file2.py: Description of file2
```

## Notes

- Ensure you have the necessary permissions and tokens to access the GitHub repository and use the OpenAI API.
- The generated README content is basic and can be customized by modifying the prompt provided to the OpenAI API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


