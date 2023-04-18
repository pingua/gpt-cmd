import os
import sys
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
if openai.api_key is None:
    # Ask the user if they have the key or not
    print("The OPENAI_API_KEY environment variable is not set.")
    answer = input("Do you have an OpenAI API key? (y/n) ")
    if answer.lower() == "y":
        # Ask the user to paste the key manually
        openai.api_key = input("Please paste your OpenAI API key: ")
        # Try to test the key by making a simple API call
        try:
            openai.Engine.list()
        except openai.error.AuthenticationError:
            # Handle the case when the key is invalid
            print("The OpenAI API key you entered is invalid.")
            print("Please check your key and try again.")
            sys.exit()
    else:
        # Handle the case when the user does not have the key
        print("You need an OpenAI API key to use this script.")
        print("You can get one from https://openai.com/docs/api-reference/authentication.")
        sys.exit()

if len(sys.argv) < 2:
    print("Usage: python chatcompletion.py <prompt> or python chatcompletion.py -f <filename>")
    sys.exit()

if sys.argv[1] == "-f":
    # Read the prompt from a file
    filename = sys.argv[2]
    with open(filename) as f:
        prompt = f.read()
else:
    # Read the prompt from the command line
    prompt = sys.argv[1]

# Count the number of tokens in the prompt
tokens = len(prompt.split())*4/3

# Check if the tokens exceed 1000
if tokens > 1000:
    # Ask for confirmation
    answer = input(f"The prompt has {tokens} tokens, which may incur a high cost. Do you want to continue? (y/n) ")
    # If the answer is not yes, exit the program
    if answer.lower() != "y":
        print("Aborting chat completion.")
        sys.exit()

# Proceed with chat completion using gpt 3.5 model
completion = openai.ChatCompletion.create (
    model="gpt-3.5-turbo",
    messages= [
        {"role": "user", "content": prompt}
    ]
)

message = completion.choices [0].message.content

print(message)
