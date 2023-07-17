import random

def generateRandomCamelCase():
    variableCount = random.randint(5, 10)
    camelCaseCode = ""
    for i in range(variableCount):
        variableName = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(random.randint(3, 8)))
        camelCaseCode += variableName[0].lower() + variableName[1:]
        if i < variableCount - 1:
            camelCaseCode += random.choice(("_", ""))
    return camelCaseCode

for i in range(10):
    generatedVariable = generateRandomCamelCase()
    print(f"{generatedVariable} = {random.randint(1, 100)}")
