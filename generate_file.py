import pandas as pd
from openai import OpenAI, chat
import docx
import csv

client = OpenAI(api_key="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")
def cmp_de_en(de, en):
    msg = "Here are two strings, one in German one in English, can you tell me if they have the same meaning, German:"
    msg = msg + de
    msg = msg + ", English:"
    msg = msg + en
    msg = msg + ". Give simple answer Yes, No"
    completion = client.chat.completions.create(model="gpt-4",messages=[{"role": "user", "content": msg}])
    #print(completion.choices[0].message.content)
    return (completion.choices[0].message.content)


Master = {}
doc = docx.Document('Machine/100XXX_QD_AFT-CAR_Durch_de_Master.2.docx')
j = 0
for i in doc.paragraphs:
    j+=1
    if j > 23 and i.text and i.text[0] != '\n' and i.text[0:2].isupper():
        if '\n' in i.text:
            endl = i.text.find('\n')
            strr = i.text[0:endl]
            p = strr.find(":")
            key = strr[0:p]
            if key in Master.keys():
                Master[key + "-"]=strr[p + 2:]
            else:
                Master[strr[0:p]]=strr[p + 2:]
            strr = i.text[endl+1:]
            p = strr.find(":")
            key = strr[0:p]
            if key in Master.keys():
                Master[key + "-"]=strr[p + 2:]
            else:
                Master[strr[0:p]]=strr[p + 2:]
        else:
            p = i.text.find(":")
            key = i.text[0:p]
            if key in Master.keys():
                Master[key + "-"]=i.text[p + 2:]
            else:
                Master[i.text[0:p]]=i.text[p + 2:]

#generating dict
machine_number = input("Machine Number:")

if machine_number == "100223" or machine_number == "100261" or machine_number == 752937:

    file_path = "Machine/m"+machine_number+"/"+machine_number+"_f.xlsx"

    df = pd.read_excel(file_path, engine='openpyxl')
    Machine = {}
    l = len (df['Machine type:'])

    for i in range(3, l):
        Machine[df['Machine type:'][i]] = df['Unnamed: 1'][i]


    code_in = {}
    code_out = {}

    print("Generating file ...")
    for mach_key in Machine.keys():
        for mst_key in Master.keys():
            #print(str(mach_key)+" "+mst_key)
            if " "+str(mach_key)+"-" in mst_key+"-":
                if cmp_de_en(Master[mst_key],Machine[mach_key])== "Yes":
                    code_in[mst_key] = Machine[mach_key]
                    break
        code_out[mach_key] = Machine[mach_key].replace("\n", " ")
        
        
    #save file
    while True:
        file_type = input("Enter file type:")
        if file_type == "csv" or file_type == "txt":
            break
        print("please enter 'txt' or 'csv'")

    if file_type == "csv":
        with open("report_"+machine_number+".csv", 'w') as csv_file:  
            writer = csv.writer(csv_file)
            for key, value in code_out.items():
               writer.writerow([key, value])
        print("Saved to csv file")
    elif file_type == "txt":
        with open("report_"+machine_number+".txt", 'w') as file:
            for key, value in code_out.items():
                file.write(f"FaultNo.:{key} corresponds to: {value}\n")
        print("Saved to txt file")
        

else:
    print("Machine not found")
