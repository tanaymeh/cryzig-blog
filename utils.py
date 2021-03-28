import random
import string
import json
import os 
import schemas

class Utils:
    def createUser(userData: dict):
        """
        Saves a dictionary as a json file with randomized name and returns the file name.
        After creating a new user data file, add the user 
        """
        # If the user data is a model, convert to a dictionary
        if isinstance(userData, schemas.UserModel):
            userData = Utils.convertModeltoJSON(userData)
        
        # Create the file and add the data into it.
        fileName = Utils.generateANString()
        fileName = f"{fileName}.json"
        with open(f"data/{fileName}", 'w') as f:
            json.dump(userData, f)

        # Add the entry into the registry
        registryData = {userData['userid']: fileName}
        Utils.addUserToRegistry(registryData)
        
        return fileName
    
    def addUserToRegistry(data: dict):
        """
        Adds a userid and it's corresponding data filename in the registry
        """
        if not os.path.exists('data/registry.json'):
            f = open('data/registry.json', 'w+')
            json.dump(data, f)                         
        else:
            with open('data/registry.json', 'r+') as fl:
                newData = json.load(fl)
                newData.update(data)
                fl.seek(0)
                json.dump(newData, fl)
    
    def checkRegistry(userid: str):
        """
        Checks if a 'userid: filename' pair exists in the registry.
        """
        try:
            with open('data/registry.json', 'r+') as fl:
                file = json.load(fl)
                # print(file)
                if userid in file:
                    print(f"User id: {userid} exists")
                    return True
        except FileNotFoundError:
            return False
        
        return False
    
    def convertModeltoJSON(userModelObject: schemas.UserModel):
        """Takes a UserModel type object and return a dictionary of the data

        Args:
            userModelObject (schemas.UserModel): UserModel Object passed by request

        Returns:
            dict: Dictionary form of user model object
        """
        modelCache = {}
        modelCache['userid'] = userModelObject.userid
        modelCache['name'] = userModelObject.name
        modelCache['age'] = int(userModelObject.age)
        modelCache['gender'] = userModelObject.gender
        
        return modelCache
    
    def generateANString():
        """
        Generates a 16-digit Alphanumeric string
        """
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        return x