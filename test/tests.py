import asyncio
import os
import random
import tellurium as te
import cesiumlookups as lookups
from cesiumlookups.lookups import Model
import msgspec.json

data = lookups.get_metadata("https://github.com/epshteinmatthew/OscillatorDatabase")
dir_path = "result" 

def test_metadata():
    with open("./metadata.json", "r") as f:
        mtdata = msgspec.json.decode(f.read(), type=list[Model])
        assert mtdata == data

def test_length():
    numModels = lookups.get_number_of_models_with_attrib(data)
    assert numModels == len(data) == lookups.get_summary(data)['total amount of models']


def test_ranges():
    ranges = lookups.get_accepted_ranges(data)
    for item in data:
        assert ranges["reactionsRange"][0] <= item.numReactions <= ranges["reactionsRange"][1] and ranges["speciesRange"][0] <= item.numSpecies <= ranges["speciesRange"][1]


def test_attrib_lookup():
    numModels = lookups.get_number_of_models_with_attrib(data, 2, 3)
    count = 0
    for item in data:
        if item.numSpecies == 2 and item.numReactions == 3:
            count+=1
    assert count == numModels

def test_types():
    types = lookups.get_model_type_info(data)
    for item in data:
        assert item.modelType in types['types']


async def lookup(key):
    await lookups.lookup(data, "https://github.com/epshteinmatthew/OscillatorDatabase",
                   resultant_dir=dir_path,
                   num_species=key[0], num_reactions=key[1], model_type=key[2])



def test_lookup(): # relative path for now

    summarydata = lookups.get_summary(data, False)
    pairs = {}
    for key in list(summarydata.keys())[1:]:
        pairs[
            (int(key[key.find("and ") + 4:key.rfind(" species")]),
             int(key[key.find("with ") + 5:key.rfind(" reactions")]),
             key[key.find("of ") + 3:key.rfind(" models")])
        ] = summarydata[key]

    pairs_keys = list(pairs.keys())
    random_key = pairs_keys[random.randint(0, len(pairs_keys))]

    asyncio.run(lookup(random_key))

    for path in os.listdir(dir_path):
        with open(os.path.join(dir_path, path), "r") as file:
            model_string = file.read()
            r = te.loada(model_string)
            numSpecies = r.getNumFloatingSpecies()
            numReactions = r.getNumReactions()

            if "oscillator" in os.listdir(dir_path)[0]:
                modelType = "oscillator"
            elif "random" in os.listdir(dir_path)[0]:
                modelType = "random"
            else:
                modelType = "-"

            assert (numSpecies == random_key[0] and numReactions == random_key[1] and modelType == random_key[2])


