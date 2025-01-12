# verification_output.py
from models import SudokuVerificationPlan

def print_verification_plan(plan):
    """
    Receives a 'plan' (ideally a SudokuVerificationPlan) and prints the verification
    details in a structured way.
    """
    print("\nSudoku Verification Plan:")

    # Safely check if `plan` is actually a SudokuVerificationPlan
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
        # Possibly it's a string or some other type if there's a parsing issue.
        print("The returned `plan` is not a SudokuVerificationPlan object.")
        print("Plan content:", plan)
