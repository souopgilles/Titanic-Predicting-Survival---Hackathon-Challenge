#!/usr/bin/env python3
import sys
import os
import csv

# --- Configuration ---
FILENAME = "submission.csv"
EXPECTED_ROWS = 418
EXPECTED_COLUMNS = ["PassengerId", "Survived"]
# ---------------------

def main():
    """Runs all checks on the submission file."""
    print(f"--- Checking {FILENAME} ---")

    # 1. Check if the file exists
    if not os.path.exists(FILENAME):
        print(f"❌ Error: Submission file '{FILENAME}' not found.")
        sys.exit(1)

    try:
        with open(FILENAME, 'r', newline='') as f:
            reader = csv.reader(f)

            # 2. Check the header
            header = next(reader)
            if header != EXPECTED_COLUMNS:
                print(f"❌ Error: Invalid header. Expected {EXPECTED_COLUMNS}, but got {header}.")
                sys.exit(1)
            print("✅ Header is correct.")

            # 3. Check rows for format and values
            row_count = 0
            for i, row in enumerate(reader, 1):
                row_count += 1
                if len(row) != 2:
                    print(f"❌ Error: Row {i} has {len(row)} columns, expected 2.")
                    sys.exit(1)
                
                try:
                    survived_val = int(row[1])
                    if survived_val not in [0, 1]:
                        print(f"❌ Error: Row {i} has an invalid value '{row[1]}' in 'Survived' column. Must be 0 or 1.")
                        sys.exit(1)
                except ValueError:
                    print(f"❌ Error: Row {i} has a non-integer value '{row[1]}' in 'Survived' column.")
                    sys.exit(1)
            
            print("✅ All rows have the correct format and values.")

            # 4. Check the total number of data rows
            if row_count != EXPECTED_ROWS:
                print(f"❌ Error: Incorrect number of rows. Expected {EXPECTED_ROWS} data rows, but found {row_count}.")
                sys.exit(1)
            print(f"✅ Correct number of rows ({row_count}).")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)

    print("\n🎉 Success! Your submission file passed all sanity checks.")
    sys.exit(0)

if __name__ == "__main__":
    main()