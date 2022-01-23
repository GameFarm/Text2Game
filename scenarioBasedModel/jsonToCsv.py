import json

with open('./dataset/modu_emotion.json', 'rb') as f:
    json_data = json.load(f)

f = open("modu_emotion.csv", "w", encoding="utf-8-sig")
f.write('text,y\n')


documents = json_data['document']

for doc in documents:
    senti_exps = doc['sentiment_expression']
    for senti_exp in senti_exps:
        text = senti_exp['expression'][0]['expression_form']
        y = senti_exp['expression_score']
        f.write(f'"{text}",{y}\n')
print("IS DONE...")
