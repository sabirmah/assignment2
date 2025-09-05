import os
import pandas as pd

# Folder containing CSV files
folder_path = "temperatures"

# Output folder for .txt results
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through CSV files
for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        try:
            df = pd.read_csv(file_path)

            # Find first numeric column (instead of forcing "Temperature")
            numeric_cols = df.select_dtypes(include="number").columns
            if len(numeric_cols) == 0:
                print(f"{file}: No numeric columns found, skipping.")
                continue

            col = numeric_cols[0]  # take the first numeric column
            avg_temp = df[col].mean(skipna=True)
            max_temp = df[col].max(skipna=True)
            min_temp = df[col].min(skipna=True)

            result_text = (
                f"File: {file}\n"
                f"Column used: {col}\n"
                f"Average: {avg_temp:.2f}\n"
                f"Max: {max_temp}\n"
                f"Min: {min_temp}\n"
            )

            print(result_text)

            # Save to output folder
            output_file = os.path.join(output_folder, file.replace(".csv", ".txt"))
            with open(output_file, "w") as f:
                f.write(result_text)

        except Exception as e:
            print(f"Error processing {file}: {e}")

