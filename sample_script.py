from models import SudokuGrid, SudokuVerificationDetails, SudokuVerificationPlan

# Sample 9×9 sudoku grid (0 represents an empty cell)
sample_grid = [
    [5, 3, 0,  0, 7, 0,  0, 0, 0],
    [6, 0, 0,  1, 9, 5,  0, 0, 0],
    [0, 9, 8,  0, 0, 0,  0, 6, 0],
    
    [8, 0, 0,  0, 6, 0,  0, 0, 3],
    [4, 0, 0,  8, 0, 3,  0, 0, 1],
    [7, 0, 0,  0, 2, 0,  0, 0, 6],
    
    [0, 6, 0,  0, 0, 0,  2, 8, 0],
    [0, 0, 0,  4, 1, 9,  0, 0, 5],
    [0, 0, 0,  0, 8, 0,  0, 7, 9]
]

# Sample verification details using "valid" or "invalid" (with optional messages)
sample_lines_verification = [
    # 9 rows, each row is a list of 9 statuses
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Row 1
    [
        "valid", 
        "valid", 
        "invalid", 
        "Duplicate '1' found in columns 3 and 5",
        "valid", 
        "valid", 
        "valid", 
        "valid", 
        "valid"
    ],  # Row 2
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Row 3
    [
        "valid", 
        "valid", 
        "valid", 
        "valid", 
        "invalid", 
        "Missing '7'", 
        "valid", 
        "valid", 
        "valid"
    ],  # Row 4
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Row 5
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Row 6
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Row 7
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Row 8
    [
        "invalid",
        "Out of range '10'",
        "valid", 
        "valid", 
        "valid", 
        "valid", 
        "valid", 
        "valid", 
        "valid"
    ]   # Row 9
]

sample_columns_verification = [
    # 9 columns, each column is a list of 9 statuses
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Col 1
    [
        "valid", 
        "invalid", 
        "Duplicate '4' found in rows 2 and 6", 
        "valid", 
        "valid", 
        "valid", 
        "valid", 
        "valid", 
        "valid"
    ],  # Col 2 (example)
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Col 3
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Col 4
    [
        "invalid",
        "Missing '2'",
        "valid",
        "valid",
        "valid",
        "valid",
        "valid",
        "valid",
        "valid"
    ],  # Col 5
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Col 6
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Col 7
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Col 8
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"]   # Col 9
]

sample_subgrids_verification = [
    # 9 subgrids, each subgrid is a list of 9 statuses
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Subgrid 1
    [
        "valid", 
        "valid", 
        "invalid", 
        "Incorrect subgrid sum", 
        "valid", 
        "valid", 
        "valid", 
        "valid", 
        "valid"
    ],  # Subgrid 2
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Subgrid 3
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Subgrid 4
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Subgrid 5
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Subgrid 6
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"],  # Subgrid 7
    [
        "valid", 
        "invalid", 
        "Duplicate '7'", 
        "valid", 
        "valid", 
        "valid", 
        "valid", 
        "valid", 
        "valid"
    ],  # Subgrid 8
    ["valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid", "valid"]   # Subgrid 9
]

# Create the SudokuVerificationPlan instance
verification_plan = SudokuVerificationPlan(
    sudoku_puzzle=SudokuGrid(grid=sample_grid),
    verification_details=SudokuVerificationDetails(
        lines_verification=sample_lines_verification,
        columns_verification=sample_columns_verification,
        subgrids_verification=sample_subgrids_verification
    ),
    overall_result="Invalid puzzle. Some duplicates found.",
    final_note="Remove duplicates from row 2 and subgrid 8."
)

# Dump to a Python dict (which can be converted to JSON)
json_data = verification_plan.model_dump()

print("=== JSON Dump (Dictionary) ===")
print(json_data)

# Dump the schema (Pydantic v2)
schema_data = verification_plan.model_json_schema()


print("\n=== Schema ===")
print(schema_data)
