# src/llm_clients/openai_client.py
import json
from typing import List
from pydantic import ValidationError
from dotenv import load_dotenv
from openai import OpenAI

# system message
from system_message import system_message

# load environment variables if needed
load_dotenv()

def verify(user_message, response_format):
    # get the client
    client = OpenAI()

    # setup the messages
    messages = [system_message, user_message]

    try:
        # perform the completion
        response = client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=messages,
            response_format=response_format
        )

        # return a parsed message
        return response.choices[0].message.parsed

    except ValidationError as ve:
        print("Output did not match SudokuVerificationPlan schema:", ve)
    except json.JSONDecodeError:
        print("The model output wasn't valid JSON. Try refining the prompt or adding a check for invalid JSON.")
    except Exception as ex:
        print("An error occurred:", ex)

