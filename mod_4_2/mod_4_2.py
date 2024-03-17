import re
from pathlib import Path

def get_cats_info(path):
    with open(path) as reader:
        result = []
        cat_info_dict = {}
        while True:
            line = reader.readline()
            if not line:
                break
            cat_info_list = line.split(",")
            cat_info_dict["id"] = cat_info_list[0]
            cat_info_dict["name"] = cat_info_list[1]
            cat_info_dict["age"] = cat_info_list[2]
            result.append(cat_info_dict)
    return result

cats_info = get_cats_info("mod_4_2\cats_file.txt")
print(cats_info)