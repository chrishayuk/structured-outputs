# sudoku_second_pass.py
from models import SudokuVerificationPlan
from verification_output import print_verification_plan
from llm_clients.ollama_client import verify

system_message = {
    "role": "system",
    "content": (
        "You are an expert at verifying Sudoku solutions. "
        "Given a 9x9 Sudoku grid, return a JSON object matching the SudokuVerificationPlan schema:\n\n"
        "1) sudoku_puzzle: the 9x9 array of integers.\n\n"
        "2) verification_details: an object with:\n"
        "   - lines_verification: a list of 9 arrays, each array describing that row's checks in a detailed, paragraph-like format. "
        "     For example, you might include a heading like 'A. Verify Each Row', a short explanation, and then for each row:\n"
        "       'Row 1: 5, 3, 4, 6, 7, 8, 9, 1, 2 -> SUCCESS', "
        "       'Row 2: 6, 7, 2, 1, 9, 5, 3, 4, 8 -> SUCCESS', etc.\n\n"
        "   - columns_verification: a list of 9 arrays, similarly detailed. For instance:\n"
        "       'B. Verify Each Column', 'Column 1: digits... -> SUCCESS', etc.\n\n"
        "   - subgrids_verification: a list of 9 arrays, also detailed. For instance:\n"
        "       'C. Verify Each Subgrid', 'Subgrid 1: digits... -> SUCCESS', etc.\n\n"
        "3) overall_result: 'VALID' or 'INVALID'.\n"
        "4) final_note: a short concluding remark.\n\n"
        "IMPORTANT:\n"
        " - Each of the arrays (lines_verification, columns_verification, subgrids_verification) must have exactly 9 elements.\n"
        " - Each element can contain a multi-sentence explanation if needed, but store it as a single string.\n"
        " - Clearly state if there's a duplicate, e.g., 'Row 2 -> ERROR: digit 3 appears twice'.\n"
        " - The final output must be valid JSON that exactly matches the SudokuVerificationPlan schema.\n"
    )
}


def main():
    user_message_first_pass = {
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
    # Hardcoded model name
    model_name = "phi4"

    # --- First Pass ---
    plan_first_pass = verify(
        system_message=system_message,
        user_message=user_message_first_pass,
        response_format=SudokuVerificationPlan,
        model_name=model_name
    )

    print("=== First Pass ===")
    print_verification_plan(plan_first_pass)

    # --- Second Pass ---
    # Use the JSON output from the first pass as part of the new user_message
    second_pass_input_json = plan_first_pass.model_dump_json()

    user_message_second_pass = {
        "role": "user",
        "content": (
            f"Here is the first-pass verification result:\n{second_pass_input_json}\n"
            "Please verify again or correct any mistakes if needed."
        )
    }

    plan_second_pass = verify(
        system_message=system_message,
        user_message=user_message_second_pass,
        response_format=SudokuVerificationPlan,
        model_name=model_name
    )

    print("=== Second Pass ===")
    print_verification_plan(plan_second_pass)


if __name__ == "__main__":
    main()
