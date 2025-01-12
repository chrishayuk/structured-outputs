# models.py
from typing import List
from pydantic import BaseModel

class SudokuGrid(BaseModel):
    grid: List[List[int]]

class SudokuVerificationDetails(BaseModel):
    # Each element represents an entire line (row),
    # which itself is a list of cell-check strings
    lines_verification: List[List[str]]

    # Each element represents a column,
    # which itself is a list of cell-check strings
    columns_verification: List[List[str]]

    # Each element represents a subgrid,
    # which itself is a list of cell-check strings
    subgrids_verification: List[List[str]]

class SudokuVerificationPlan(BaseModel):
    sudoku_puzzle: SudokuGrid
    verification_details: SudokuVerificationDetails
    overall_result: str
    final_note: str
