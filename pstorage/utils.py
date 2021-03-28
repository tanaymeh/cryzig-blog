import random
import json
import os

class Utils:
    def createFile(argumentsDict: dict):
        """
        Saves a dictionary as a json file with randomized name and returns the file name
        """
        fileName = random.randint(a=1000, b=5000000)
        fileName = f"{fileName}.json"
        with open(f"udata/{fileName}", 'w') as f:
            json.dump(argumentsDict, f)

        return fileName
    
    def addIntoRegistry(data: dict):
        """
        Adds a userid and it's corresponding data filename in the registry
        """
        if not os.path.exists('udata/registry.json'):
            with open('udata/registry.json', 'w') as fl:
                json.dump(data, fl)                            
        else:
            with open('udata/registry.json', 'r+') as fl:
                newData = json.load(fl)
                newData.update(data)
                fl.seek(0)
                json.dump(newData, fl)
    
    def checkRegistry():
        pass