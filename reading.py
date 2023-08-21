from json import load
data = []
tags = []

with open("data.json", "r") as json_file:
    loaded_data = load(json_file)

print(loaded_data)

print()
with open(r"D:\Vaults\Hobby Projects\Hobby Project\data.txt", "r") as file:

    for i in file.readlines():
        data.append(i.strip())
        

def striping_func(data:list):
    temp = {}
    separator = "["
    e_separator = "]"
    for i in data:
        if separator in i and e_separator in i:
            te = (i.removeprefix("[")).split(":")
            temp[te[0]] = te[1]
    for i in temp:
        print(i)
        



# for i in range(len(data)):
#     if data[i] == "~Status~":
#         striping_func(data)
#     else:
#         pass


print("test")
print("test")
