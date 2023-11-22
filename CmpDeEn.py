from openai import OpenAI, chat
client = OpenAI(api_key="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")
def cmp_de_en(de, en):
    msg = "Here are two strings, one in German one in English, can you tell me if they have the same meaning, German:"
    msg = msg + de
    msg = msg + ", English:"
    msg = msg + en
    msg = msg + ". Give simple answer Yes, No"
    completion = client.chat.completions.create(model="gpt-4",messages=[{"role": "user", "content": msg}])
    print(completion.choices[0].message.content)