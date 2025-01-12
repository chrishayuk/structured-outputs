import json
from typing import List
from pydantic import ValidationError
from dotenv import load_dotenv
from openai import OpenAI

# system message
from system_message import system_message

# load environment variables if needed
load_dotenv()

def verify(user_message, response_format, model: str):
    """
    Verifies a user message against the SudokuVerificationPlan using OpenAI.
    Takes in a 'model' argument which defaults in sudoku.py to 'gpt-4o-mini' unless overridden.
    """
    # get the client
    client = OpenAI()

    # setup the messages
    messages = [system_message, user_message]

    try:
        response = client.beta.chat.completions.parse(
            model=model,  # use the argument passed from sudoku.py
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
