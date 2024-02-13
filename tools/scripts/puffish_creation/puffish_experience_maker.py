"""Create a puffish skills sources and make the experience field, auxiliating the modder to make more custom items.

Ver 1.0 KuroiAme4536 on mojang
Jason21Todd on github

"""


import os
import json


MAIN_PATH = "./tools/scripts/puffish_creation/main/"
# Defines then post path to especify if has one ( default is "")
POST_PATH = "/capabilities/weapons"
# Defines then pre path to especify if has one ( default is "")
PRE_PATH = ""
# Define what words should be included on sources
INCLUDED_WORDS = ["sword", "claymore"]


def read_all_mods():
    """Read and list all the mods inside of main"""
    mods_list = os.listdir(MAIN_PATH)
    print(f"found {len(mods_list)}  mods ")
    return mods_list
    

class ModReader:
    """Class that read all the items inside of a mod folder.
    
    that folders must be inside of the folder has the name "main"
    """

    @classmethod
    def read_all_the_items(cls):
        print("Reading items...")
        mods = read_all_mods()
        mods_with_items = {}
        for mod in mods:
            current_path = MAIN_PATH + PRE_PATH + mod + POST_PATH
            mods_with_items[mod] = os.listdir(current_path)
            mods_with_items[mod] = cls.sanatize_item_name(mods_with_items[mod])
        return mods_with_items

    @classmethod
    def sanatize_item_name(cls, item_list: list[str]):
        print("cleaning itens json ends")
        sanatized_item_list = []
        for item in item_list:
            sanatized_item_list.append(item.replace(".json", ""))
        return sanatized_item_list


class ItemsFilter:
    @classmethod
    def filter_by_word(cls, items):
        filtered_items = []
        for item_name in items:
            for word in INCLUDED_WORDS:
                if word in item_name:
                    filtered_items.append(item_name)
        return filtered_items


class StrctureMaker:
    conditions = []

    @classmethod
    def make_conditions(cls):
        """Create the source data strcuture for puffish"""
        condition_str = ""
        for condition in cls.conditions:
            condition_str = condition_str +" | "+condition
        return condition_str
            

    @classmethod
    def iterate_all_items(cls):
        mods = read_all_mods()
        sources = []
        items_dict = ModReader.read_all_the_items()
        for mod in mods:
            items_list = ItemsFilter.filter_by_word(items_dict[mod])
            for item in items_list:
                cls.conditions.append(f"{mod}_{item}")
                sources.append(cls.make_source_base(mod, item))
        return sources

    @classmethod
    def make_it_json(cls, dict_structure: dict):
        with open(f"./tools/scripts/puffish_creation/current.json", "w+", encoding="UTF-8") as arq:
            conditions = {"conditons": cls.make_conditions()}
            dump = json.dumps(obj=[dict_structure, conditions] , indent=3)
            arq.write(dump)
        
    @classmethod
    def make_source_base(cls, mod_id, item):
        """Make puffish experience source base"""
        base = {f"{mod_id}_{item}": {
                        "type": "weapon",
                        "data": {
                            "item": f"{mod_id}:{item}"
                            }
                    }}
        return base
    

if __name__ == "__main__":
    print(ModReader.read_all_the_items())
    print(StrctureMaker.iterate_all_items())
    structure = StrctureMaker.iterate_all_items()
    StrctureMaker.make_it_json(structure)
    print(StrctureMaker.make_conditions())