import json

with open("questions.json", "r") as file:
    data = json.load(file)

    for q in data["questions"]:
        q["answer"] = input(q['q'])

with open("questions.json", "w") as file:
    json.dump(data, file, indent=4)