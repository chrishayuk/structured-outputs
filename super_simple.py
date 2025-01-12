import json
from pydantic import BaseModel

system_message = {
    "role": "system",
    "content": (
        "You are an expert at verifying yes/no questions.\n"
        "Output valid JSON only"
    )
}

class YesNoVerficationPlan(BaseModel):
    question: str
    user_answer: str
    correct_answer: bool
    is_correct: bool
    explanation: str


from ollama import chat

def verify(system_message, user_message, response_format, model_name):
    messages = [system_message, user_message]

    response = chat(
        model=model_name,
        messages=messages,
        format=response_format.model_json_schema()
    )

    return response_format.model_validate_json(response.message.content)
        

def main():

    user_message = {
        "role": "user",
        "content": "Question: Is the sky green?  The user answered 'yes'."
    }
    
    plan = verify(system_message=system_message, user_message=user_message, response_format=YesNoVerficationPlan, model_name="qwen2.5-coder")

    print("schema")
    print("------------")
    print(plan.model_json_schema())

    print("json")
    print("------------")
    print(plan.model_dump())

if __name__ == "__main__":
    main()