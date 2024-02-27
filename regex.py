
import re
import random
#  REGULAR EXPRESSIONS
txt = "the rain in spain"

x = re.search("in", txt)

print("Found:", x.end())


z = re.split("in", txt)

# print("Found:", y)
# print( z)

u = re.split("[a-f]+","0a3B9", flags=re.IGNORECASE)
u = re.split(r'(\W+)', 'Weight, feat, word, wish, good, wise')

# print(u)


text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""


# entries = re.split("\n+", text)
# final = list()
# for entry in entries:
#     pass
#     print(re.split(":? ", entry, 4))

# Randomise words, in a sentence
def repl(m):
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)
textt = "Professor Abdolmalek, please report your absences promptly."
print(re.sub(r"(\w)(\w+)(\w)", repl, textt))


# find matches, like adverbs

findText = "He was carefully disguised but captured quickly by police."
result = re.findall(r"\w+ly\b", findText)
print(result)