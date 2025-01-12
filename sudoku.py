# sudoku.py
import argparse
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

def parse_args():
    # setup argument parser
    parser = argparse.ArgumentParser(description="Check Sudoku puzzle validity using LLMs")
    
    # add arguments
    parser.add_argument(
        "--model-provider",
        type=str,
        default="ollama",
        choices=["ollama", "openai"],
        help="Which LLM provider to use (default: ollama)."
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Which model to use for the chosen provider. Defaults to 'phi4' (ollama) or 'gpt-4o-mini' (openai)."
    )

    # parse arguments
    return parser.parse_args()

def main():
    # parse areguments
    args = parse_args()

    # Determine default model if not provided
    if not args.model:
        if args.model_provider == "ollama":
            args.model = "phi4"
        else:
            args.model = "gpt-4o-mini"

    # Dynamically import the correct verification client based on provider
    if args.model_provider == "ollama":
        from llm_clients.ollama_client import verify
    else:
        from llm_clients.openai_client import verify

    # Call verify with the chosen model
    plan = verify(user_message, SudokuVerificationPlan, args.model)

    # Print out the plan
    print_verification_plan(plan)

if __name__ == "__main__":
    # run
    main()