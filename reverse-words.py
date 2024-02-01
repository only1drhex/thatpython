# print("hey budd".split(" ").reverse())

# v = [3,4,5,"5"]
# r = v
# print(r)

class wordUtil:

    def __init__(self, sentence):
        self.sentence = sentence
    def reverse_word(self):
          c = reversed(self.sentence.split())
          return " ".join(c)
    

obj = wordUtil("Hello World")
formaatWrd = print(obj.reverse_word())
    
    