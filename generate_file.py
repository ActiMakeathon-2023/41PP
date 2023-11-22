import pandas as pd
from openai import OpenAI, chat
import docx

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


machine_number = input("Machine Number:")

file_path = "Machine/m"+machine_number+"/"+machine_number+"_f.xlsx"

df = pd.read_excel(file_path, engine='openpyxl')
Machine = {}
l = len (df['Machine type:'])

for i in range(3, l):
    Machine[df['Machine type:'][i]] = df['Unnamed: 1'][i]


code_in = {}
code_out = {}


for mach_key in Machine.keys():
    for mst_key in Master.keys():
        #print(str(mach_key)+" "+mst_key)
        if " "+str(mach_key)+"-" in mst_key+"-":
            if cmp_de_en(Master[mst_key],Machine[mach_key])== "Yes":
                code_in[mst_key] = Machine[mach_key]
                break
    code_out[mach_key] = Machine[mach_key]

print(len(code_out.keys()))