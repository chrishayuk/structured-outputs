# simple_hardcoded.py
from pydantic import BaseModel

# Define a Pydantic model (no defaults needed here)
class YesNoVerificationPlan(BaseModel):
    question: str
    user_answer: str
    correct_answer: bool
    is_correct: bool
    explanation: str

#Main driver with robust error handling
def main():
    # Instantiate the verification plan model with hardcoded values
    plan = YesNoVerificationPlan(
        question="Is the sky green?",
        user_answer="yes",
        correct_answer=False,
        is_correct=False,
        explanation=(
            "Typically, the sky appears blue to the human eye due to "
            "Rayleigh scattering of sunlight in Earth's atmosphere."
        )
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
