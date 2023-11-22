
import os
import pandas as pd

input_file_path = "data/752937_Fault.xlsx"
output_file_path = input_file_path.replace('.xlsx', '.out')
output_file_path = output_file_path.replace('data/', 'out/')

os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

with open(output_file_path, 'w') as file:
	for key, value in code_out.items():
		file.write(f"FaultNo.:{key} corresponds to: {value}\n")
