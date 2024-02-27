import os 

try:
   
   file_path = os.path.join(".","fold","ji.txt")
   file = open(file_path, "r")
   print(file.read())

except Exception as e:
    #do something else
    print(e)
