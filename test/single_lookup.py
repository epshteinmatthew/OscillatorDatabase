import asyncio
import os
import random

import pytest
import tellurium as te
import oscillatorlookups as lookups

#todo: add pytest

data = lookups.get_metadata("https://github.com/epshteinmatthew/OscillatorDatabase")

#get and print a summary of the database
summarydata = lookups.get_summary(data, False)

pairs = {}

#create a dictionary of lookup parameters to model quantities
for key in list(summarydata.keys())[1:]:
    pairs[
        (int(key[key.find("and ")+4:key.rfind(" species")]),
         int(key[key.find("with ")+5:key.rfind(" reactions")]),
         key[key.find("of ")+3:key.rfind(" models")])
    ] = summarydata[key]

pairs_keys = list(pairs.keys())

random_key = pairs_keys[random.randint(0, len(pairs_keys))]

async def lookup(key):
    await lookups.lookup(data, "https://github.com/epshteinmatthew/OscillatorDatabase",
                   resultant_dir="/home/epshtein/PycharmProjects/cesiumtest/result",
                   num_species=key[0], num_reactions=key[1], model_type=key[2])


asyncio.run(lookup(random_key))

dir_path = "/home/epshtein/PycharmProjects/cesiumtest/result"  # relative path for now

def test_function():
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


