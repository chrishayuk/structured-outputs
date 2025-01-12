# src/scripts/model_json.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# our imports
from models import SudokuGrid, SudokuVerificationDetails, SudokuVerificationPlan

# create an empty verification plan
verification_plan = SudokuVerificationPlan(
    sudoku_puzzle=SudokuGrid(grid=[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]),
    verification_details=SudokuVerificationDetails(
        lines_verification=[["valid"]],
        columns_verification=[["valid"]],
        subgrids_verification=[["valid"]],
    ),
    overall_result="Invalid puzzle. Some duplicates found.",
    final_note="Remove duplicates from row 2 and subgrid 8."
)

# show the schema
json = verification_plan.model_dump()

print("\n=== JSON ===")
print(json)