from json import load
import calculation
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
            te = ((i.removeprefix(START_PREFIX)).removesuffix(END_SUFFIX)).split(SETTER_SPE)
            
            temp[te[0]] = te[1]
    return temp
        


dat = {}
for i in range(len(data)):
    if data[i] == "~Status~":
        dat = striping_func(data)
        print(dat)
    else:
        pass

# this block belongs for the calculation
# calculation.calc(dat)
