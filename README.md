# gpt-cmd

A Python script that uses OpenAI's ChatCompletion API to generate chat responses based on a user prompt and a GPT-3.5 model.

## Installation

To use this script, you need to have Python 3 installed on your system. You also need to have an OpenAI API key that you can get from https://openai.com/docs/api-reference/authentication.

You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

To run the script, use the following command:

```bash
python chat.py [OPTIONS]
```

The available options are:

- `--model` or `-m`: The GPT-3.5 model to use. Default is `gpt-3.5-turbo`.
- `--temperature` or `-t`: The temperature to use when generating responses. Default is `0.5`.
- `--max-tokens` or `-max`: The maximum number of tokens to generate in the response. Default is `1000`.
- `--system-prompt` or `-sp`: The prompt for system messages. Default is empty.

The script will ask you to enter your OpenAI API key if it is not set as an environment variable named `OPENAI_API_KEY`.

The script will then start a loop that keeps asking for user input and generates a response using the chat completion function. To exit the loop, enter `quit`.

## Example

Here is an example of using the script with the default options:

```
python chat.py
Enter your OpenAI API key: sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
> Hi, how are you?
I'm fine, thank you. How are you?
> I'm good too. What do you like to do for fun?
I like to chat with people like you and learn new things.
> That's nice. What have you learned recently?
I have learned about some Python best practices and how to write a README file.
> Really? Can you tell me more about that?
Sure, a README file is a guide that gives users a detailed description of a project and how to use it. It can be written in plain text, reStructuredText, or Markdown formats.
```
