import json
import openai
from pyscript import Element
from js import document
import os
from dotenv import load_dotenv,dotenv_values

load_dotenv()



Set your OpenAI API key
openai.api_key = = os.getenv("MY_KEY")

def handle_submit(event):
    # Prevent the form from submitting the traditional way
    event.preventDefault()

Get user input from the form
    user_input = document.getElementById("userInput").value

Call OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the engine, e.g., text-davinci-003
        prompt=user_input,
        max_tokens=100
    )

Extract the response text
    response_text = response['choices'][0]['text']

Display the response in the output element
    output_element = Element("output")
    output_element.clear()
    output_element.write(response_text)

Attach the handle_submit function to the form submission event
form = document.getElementById("userForm")
form.addEventListener("submit", handle_submit)