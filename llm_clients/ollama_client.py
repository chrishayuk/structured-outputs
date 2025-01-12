import json
from pydantic import ValidationError
from ollama import chat

# system message
from system_message import system_message

def verify(user_message, response_format, model: str):
    """
    Verifies a user message against the SudokuVerificationPlan using Ollama.
    Takes in a 'model' argument which defaults in sudoku.py to 'phi4' unless overridden.
    """
    # setup the messages
    messages = [system_message, user_message]

    try:
        response = chat(
            model=model,
            messages=messages,
            format=response_format.model_json_schema()
        )

        # return a parsed message
        return response.message.content

    except ValidationError as ve:
        print("Output did not match SudokuVerificationPlan schema:", ve)
    except json.JSONDecodeError:
        print("The model output wasn't valid JSON. Try refining the prompt or adding a check for invalid JSON.")
    except Exception as ex:
        print("An error occurred:", ex)
