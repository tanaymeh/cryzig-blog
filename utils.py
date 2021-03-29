import random
import string
import json
import os 
import schemas

class Utils:
    def createUser(blogData: dict):
        """
        Saves a dictionary as a json file with randomized name and returns the file name.
        After creating a new user data file, add the user 
        """
        # If the user data is a model, convert to a dictionary
        if isinstance(blogData, schemas.BlogModel):
            blogData = Utils.convertModeltoJSON(blogData)
        
        # Create the file and add the data into it.
        fileName = Utils.generateANString()
        fileName = f"{fileName}.json"
        with open(f"data/{fileName}", 'w') as f:
            json.dump(blogData, f)

        # Add the entry into the registry
        registryData = {blogData['authid']: fileName}
        Utils.addBlogToRegistry(registryData)
        
        return fileName
    
    def addBlogToRegistry(data: dict):
        """
        Adds an authid and it's corresponding filename in the registry
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
    
    def checkRegistry(authid: str):
        """
        Checks if a 'userid: filename' pair exists in the registry.
        """
        try:
            with open('data/registry.json', 'r+') as fl:
                file = json.load(fl)
                if authid in file:
                    return True
        except FileNotFoundError:
            return False
        
        return False
    
    def getAllBlogs(registryPath: str):
        """Return a list of tuple, Every tuple having a single users details

        Args:
            registryPath (str): Path where the registry is located
        """
        # First check if registry exists or not
        if not os.path.exists(registryPath):
            return -1
        
        allUsers = []
        with open(registryPath, 'r') as registry:
            registry = json.load(registry)
        
        for user in registry.items():
            with open(os.path.join("data", user[1]), 'r') as userfile:
                userfile = json.load(userfile)
            currentUserData = list(userfile.values())
            allUsers.append(currentUserData)
        return allUsers
    
    def hashTitle(title: str):
        """Cleans a title string and returns it's hashed version to be used as an id

        Args:
            title (str): Title of a blog
        """
        title = title.lower()
        # hash()
        
    
    def convertModeltoJSON(modelObject: schemas.BlogModel):
        """Takes a BlogModel type object and return a dictionary of the data

        Args:
            modelObject (schemas.BlogModel): BlogModel Object passed by request

        Returns:
            dict: Dictionary form of blog model object
        """
        modelCache = {}
        modelCache['authid'] = modelObject.authid
        modelCache['blogTitle'] = modelObject.blogTitle
        modelCache['author'] = modelObject.author
        modelCache['content'] = modelObject.content
        
        return modelCache
    
    def generateANString():
        """
        Generates a 16-digit Alphanumeric string
        """
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        return x