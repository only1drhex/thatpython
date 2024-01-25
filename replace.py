def replaceString(word, search, replaceWith):
    result =  word.replace(search,replaceWith)
    return result

replacedWord = replaceString("Abdulqudus", "u", "v")

print(replacedWord)


def changeCase(sentence, case):
    if case == "upper":
        return sentence.upper()
    elif case == "lower":
        return sentence.lower()
    
changedCase = changeCase("Abdulqudus", "lower") 
print(changedCase)
