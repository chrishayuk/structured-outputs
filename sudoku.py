# sudoku.py
from models import SudokuVerificationPlan
from llm_clients.openai_client import verify
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

# -----------------------------
# 4. Use the structured data (hardened)
# -----------------------------
print("\nSudoku Verification Plan:")

# Safely check if `plan` is actually a SudokuVerificationPlan
# (not just a string or something else).
if isinstance(plan, SudokuVerificationPlan):
    if getattr(plan, "overall_result", None) is not None:
        print("Overall Result:", plan.overall_result)

    if getattr(plan, "final_note", None) is not None:
        print("Final Note:", plan.final_note)

    # Safe check for `verification_details`
    if getattr(plan, "verification_details", None) is not None:
        verification = plan.verification_details

        if getattr(verification, "lines_verification", None) is not None:
            print("\nLines Verification:")
            for i, line_checks in enumerate(verification.lines_verification, start=1):
                print(f"  Line {i}:")
                if line_checks:  # ensure it's not None or empty
                    for check in line_checks:
                        print(f"    {check}")

        if getattr(verification, "columns_verification", None) is not None:
            print("\nColumns Verification:")
            for j, col_checks in enumerate(verification.columns_verification, start=1):
                print(f"  Column {j}:")
                if col_checks:
                    for check in col_checks:
                        print(f"    {check}")

        if getattr(verification, "subgrids_verification", None) is not None:
            print("\nSubgrids Verification:")
            for k, sg_checks in enumerate(verification.subgrids_verification, start=1):
                print(f"  Subgrid {k}:")
                if sg_checks:
                    for check in sg_checks:
                        print(f"    {check}")

    else:
        print("No verification details available.")

else:
    # If we're here, `plan` is not an instance of SudokuVerificationPlan.
    # Possibly it's a string if the model returned raw text or there's a parsing issue.
    print("The returned `plan` is not a SudokuVerificationPlan object.")
    print("Plan content:", plan)

