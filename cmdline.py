import os

# print(os.getcwd())


a= os.getcwd()


# for entry in os.listdir(a):
    # print(entry)


x = os.path.abspath("area.py")
print(x)

print(os.path.exists("repwlace.py"))



base_folder = r"C:\Users\user\Desktop\thatpython"
new_dir = base_folder + "\\cart\\"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
else:
    print("the folder exists")

    #  bs4 requests 