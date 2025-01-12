# sudoku.py
from models import SudokuVerificationPlan
from llm_clients.openai_client import verify
from verification_output import print_verification_plan
#from ollama_client import verify

# user message
# user_message = {
#     "role": "user",
#     "content": (
#         "Please verify this completed Sudoku puzzle:\n\n"
#         "5 3 4 | 6 7 8 | 9 1 2\n"
#         "6 7 2 | 1 9 5 | 3 4 8\n"
#         "1 9 8 | 3 4 2 | 5 6 7\n"
#         "------+-------+------\n"
#         "8 5 9 | 7 6 1 | 4 2 3\n"
#         "4 2 6 | 8 1 3 | 7 9 1\n"
#         "7 1 3 | 9 2 4 | 8 5 6\n"s
#         "------+-------+------\n"
#         "9 6 1 | 5 3 7 | 2 8 4\n"
#         "2 8 7 | 4 1 9 | 6 3 5\n"
#         "3 4 5 | 2 8 6 | 1 7 9"
#     )
# }
user_message = {
    "role": "user",
    "content": """
Is this a valid sudoku grid:

+-------+-------+-------+
| 7 8 9 | 6 1 2 | 3 4 5 |
| 4 2 3 | 8 7 5 | 6 9 1 |
| 1 5 6 | 4 3 9 | 2 8 7 |
+-------+-------+-------+
| 8 7 2 | 5 4 3 | 9 1 6 |
| 5 3 4 | 1 6 7 | 8 2 9 |
| 6 9 1 | 2 8 4 | 5 7 3 |
+-------+-------+-------+
| 3 4 5 | 7 9 8 | 1 6 2 |
| 9 6 8 | 3 2 1 | 7 5 4 |
| 2 1 7 | 9 5 6 | 4 3 8 |
+-------+-------+-------+
"""
}


# get the response
plan = verify(user_message, SudokuVerificationPlan)

# Pass the plan to the separate output function
print_verification_plan(plan)