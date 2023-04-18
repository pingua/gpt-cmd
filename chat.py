import os
import sys
import click
import openai


def authenticate_openai():
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


def generate_chat_completion(temperature, max_tokens, model, messages=[]):
    # Proceed with chat completion using the specified model and prompt
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    # Extract the message from the completion response
    response = completion.choices[0].message.content
    return response


@click.command()
@click.option("--model", "-m", default="gpt-3.5-turbo", help="The GPT-3.5 model to use")
@click.option("--temperature", "-t", default=0.5, help="The temperature to use when generating responses")
@click.option("--max-tokens", "-max", default=1000, help="The maximum number of tokens to generate in the response")
@click.option("--system-prompt", "-sp", prompt="Enter the system prompt (optional)", help="The prompt for system messages")
def main(model, temperature, max_tokens, system_prompt):
    authenticate_openai()
    messages = [] # initialize an empty list of messages
    if system_prompt: # add the system prompt if provided
        messages.append({"role": "system", "content": system_prompt})
    while True: # start a loop that keeps asking for user input
        prompt = input("> ") # get the user prompt
        if prompt == "quit":
            break
        messages.append({"role": "user", "content": prompt}) # add it to the messages list
        response = generate_chat_completion(temperature, max_tokens, model, messages) # generate a chat completion using the messages list
        print(response) # print the response
        messages.append({"role": "assistant", "content": response}) # add it to the messages list

if __name__ == "__main__":
    main()
