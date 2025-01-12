# import
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
schema = verification_plan.model_json_dump()

print("\n=== Schema ===")
print(schema)