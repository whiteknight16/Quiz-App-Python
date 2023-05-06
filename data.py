import requests
import html
data=requests.get("https://opentdb.com/api.php?amount=10&type=boolean").json()["results"]
question_data=[]
for i in data:
    text=i["question"]
    text=html.unescape(text)
    answer=i["correct_answer"]
    question_data.append({
        "text":text,
        "answer":answer
    })

