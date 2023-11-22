# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    output_file.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: julian <julian@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/22 13:49:48 by julian            #+#    #+#              #
#    Updated: 2023/11/22 13:49:50 by julian           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import pandas as pd
import csv

input_file_path = "data/752937_Fault.xlsx"
output_file_path = input_file_path.replace('.xlsx', '.out')
output_file_path = output_file_path.replace('data/', 'out/')

os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

#Output human readable file
with open(output_file_path, 'w') as file:
	for key, value in code_out.items():
		file.write(f"FaultNo.:{key} corresponds to: {value}\n")

#Output as .csv file
output_file_path = input_file_path.replace('.out', '.csv')
with open(output_file_path, 'w') as file:
	for key, value in code_out.items():
		file.write(f"{key}, {value}\n")
