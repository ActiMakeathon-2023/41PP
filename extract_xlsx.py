# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    extract_xlsx.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: julian <julian@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/22 09:43:08 by julian            #+#    #+#              #
#    Updated: 2023/11/22 11:43:42 by julian           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

file_path = "data/752937_Fault.xlsx"
flt_file = file_path.replace('.xlsx', '.faults')

df = pd.read_excel(file_path, engine='openpyxl')
Machine = {}
l = len (df['Machine type:'])

for i in range(3, l):
	Machine[df['Machine type:'][i]] = df['Unnamed: 1'][i]
#print[df['Machine number:'][3])
for key, value in Machine.items():
	print(f"{key}: {value}\n")

with open(flt_file, 'w') as file:
	for key, value in Machine.items():
		file.write(f"{key}: {value}\n")

print(f"Entries have been written to {flt_file}")

print(Machine)
