import json

person_string ='{"name": "Ali", "languages": ["Python","C#"]}'
person_dict ='{"name": "Ali", "languages": ["Python","C#"]}'


# JSON string to dict
# result = json.loads(person_string)
# result = result["name"]
# result = result["languages"]

# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])


# result =json.dumps(person_dict) # dict to json string

# with open("person.json","a") as f:
#     json.dump(person_dict,f)

person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent=4, sort_keys=True)
print(result)

print(person_dict)