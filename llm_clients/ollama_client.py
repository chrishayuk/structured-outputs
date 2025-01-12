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

        # 2. Extract the raw text returned by the LLM.
        content_str = response.message.content

        # 3. Convert JSON string -> Python dict
        content_dict = json.loads(content_str)

        # 4. Construct the Pydantic model
        parsed_model = response_format(**content_dict)

        # return the model
        return parsed_model

    except ValidationError as ve:
        print(f"Output did not match {response_format.__name__} schema:", ve)
        return None
    except json.JSONDecodeError:
        print("The model output wasn't valid JSON. Try refining the prompt or checking the model output.")
        return None
    except Exception as ex:
        print("An error occurred:", ex)
        return None
