# sudoku_simple.py
from models import SudokuVerificationPlan
from verification_output import print_verification_plan
from system_message import system_message
from llm_clients.ollama_client import verify

user_message = {
    "role": "user",
    "content": """Please verify this completed Sudoku puzzle:

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 1 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
"""
}
 


def main():
    # Hardcoded model name
    model_name = "phi4"
    
    # Call verify with chosen (and now hardcoded) client and model
    plan = verify(system_message, user_message, SudokuVerificationPlan, model_name)

    # Print out the plan
    print_verification_plan(plan)

if __name__ == "__main__":
    main()
