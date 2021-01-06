import json

data = json.load(open("data.json"))

def translate(keyword):
    if keyword in data:
        return data[keyword]
    elif keyword.title() in data:
        return data[keyword.title()]
    elif keyword.lower() in data:
        return data[keyword.lower()]
    elif keyword.upper() in data:
        return data[keyword.upper()]
    else:
        print("That word does not exist in the dictionary. Please check the spelling and run this program again.")

keyword = input("Please enter the word you would like to search for \n")
output = translate(keyword)

if type(output) == list:
    for item in output:
            print(item+"\n")
else: 
    print(output)