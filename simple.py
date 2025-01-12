# simple.py
from pydantic import BaseModel
from llm_clients.ollama_client import verify

class YesNoVerificationPlan(BaseModel):
    question: str
    user_answer: str
    correct_answer: bool
    is_correct: bool
    explanation: str

system_message = {
    "role": "system",
    "content": (
        "You are an expert at verifying yes/no questions.\n"
        "Output valid JSON only"
    )
}

def main():
    user_message = {
        "role": "user",
        "content": "Question: Is the sky green? The user answered 'yes'."
    }

    # model name
    model_name = "phi4"

    # plan
    plan = verify(
        system_message=system_message,
        user_message=user_message,
        response_format=YesNoVerificationPlan,
        model_name=model_name
    )

    print("schema")
    print("------------")
    print(plan.model_json_schema())
    print("------------")
    print("json")
    print("------------")
    print(plan.model_dump())

if __name__ == "__main__":
    main()
