from json import load
data = []
tags = []

with open("data.json", "r") as json_file:
    loaded_data:dict = load(json_file)

# temporary blok for testing
END_SUFFIX = loaded_data.get("end_separator")
START_PREFIX = loaded_data.get("start_separator")
INLINE_SPE = loaded_data.get("in_separator")
SETTER_SPE = loaded_data.get("setter")
# temporary blocks ends

with open(r"D:\Vaults\Hobby Projects\Hobby Project\data.txt", "r") as file:

    for i in file.readlines():
        data.append(i.strip())
        

def striping_func(data:list):
    temp = {}
    for i in data:
        if START_PREFIX in i and END_SUFFIX in i:
            te = (i.removeprefix(START_PREFIX)).split(SETTER_SPE)
            temp[te[0]] = te[1]
    for i in temp:
        print(f"Value: {temp.get(i)}, extension: {type(temp.get(i))}")
        



for i in range(len(data)):
    if data[i] == "~Status~":
        striping_func(data)
    else:
        pass


