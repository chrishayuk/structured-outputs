# llm_clients/ollama_client.py
import json
from pydantic import ValidationError
from ollama import chat

def verify(
    system_message,
    user_message,
    response_format,
    model_name: str
):
    """
    Call the Ollama LLM with the given messages and format, parse the LLM response 
    as JSON, and instantiate 'model_class'. Return None if parsing fails.
    """
    messages = [system_message, user_message]

    try:
        # 1. Call Ollama with your chosen format (e.g., "json" or "").
        response = chat(
            model=model_name,
            messages=messages,
            format=response_format.model_json_schema()
        )

        # return the parsed object
        return response_format.model_validate_json(response.message.content)

    except ValidationError as ve:
        print(f"Output did not match {response_format.__name__} schema:", ve)
        return None
    except json.JSONDecodeError:
        print("The model output wasn't valid JSON. Try refining the prompt or checking the model output.")
        return None
    except Exception as ex:
        print("An error occurred:", ex)
        return None
