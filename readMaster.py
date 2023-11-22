import docx

master = {}
doc = docx.Document('Machine/100XXX_QD_AFT-CAR_Durch_de_Master.2.docx')
j = 0
for i in doc.paragraphs:
    j+=1
    if j > 23 and i.text and i.text[0] != '\n' and i.text[0:2].isupper():
        if '\n' in i.text:
            endl = i.text.find('\n')
            str = i.text[0:endl]
            #print(str)
            p = str.find(":");
            master[str[0:p]]=str[p + 2:]
            str = i.text[endl+1:]
            #print(str)
            master[str[0:p]]=str[p + 2:]
        else:
            #print(i.text)
            p = i.text.find(":")
            master[i.text[0:p]]=i.text[p + 2:]