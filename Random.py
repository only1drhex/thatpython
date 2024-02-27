import random 


randomInt  = random.randint(3,44)
print(randomInt)


places = ["place1",
          "place3",
          "place3",

          ]


# print(random.choice(places))


colors = [
    "white",
    "red",
    "green",
    "orange",
]

result = random.choices(colors,k=9, weights= [23,23,23,5])
print(result)


shuffle_num = list(range(1,34))
random.shuffle(shuffle_num)
print(shuffle_num)