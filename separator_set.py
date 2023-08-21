from json import load, dump



def text_doc(path:str):
    with open("data.json", "r") as json_file:
        data = load(json_file)
    temp = []
    with open(rf"{path}", "r") as file:
        for i in file.readlines():
            temp = (i.split("$"))
            data[temp[0].strip()] = temp[1].strip()
    json_readLoad(data=data)


def json_readLoad(file_path:str = "", data:dict = {}):
    if len(file_path) != 0:
        with open(rf"{file_path}", "r") as json_file:
            p_data:dict = load(json_file)
        with open("data.json", "r") as json_file:
            data = load(json_file)
        temp = ["end_separator", "start_separator", "in_separator", "setter"]
        for i in range(4):
            data[temp[i]] = p_data.get(temp[i].strip())
        with open("data.json", "w") as json_file:
            dump(data, json_file, indent=4)
    elif len(data) != 0:
        with open("data.json", "w") as json_file:
            dump(data, json_file, indent=4)
    else:
        'Custom error messgae here later'


    




text_doc("D:\Vaults\Hobby Projects\Hobby Project\dummy.txt")

# json_readLoad(file_path="temp.json")



