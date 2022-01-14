import os, asyncio
def fixPath(s: str)->str:
    return ".".join(s.replace(".", "").replace("\\", "/").split("/"))[1:]
async def HotLoad(bot, path: str = "./cogs"):
    modules: dict[str,int] = {}

    for filename in getListOfFiles(path):
        if not filename.endswith(".py"): continue
        path = filename
        filename = fixPath(filename[:-3])
        try: 
            bot.load_extension(f'{filename}')
            print("\033[92m"+f"loaded {filename}"+"\033[0m")
            modules[filename] = int(os.path.getmtime(path))
        except Exception as e:
            print("\033[91m"+f"ERROR: cannot load {filename}, raised error: {e}"+"\033[0m")
    while True:
        for filename in modules:
            try:
                split = filename.split(".")
                path = "./" + "/".join(split)+ ".py"
                last_time_edited = int(os.path.getmtime(path))
                if last_time_edited != modules[filename]:
                    modules[filename] = last_time_edited
                    bot.reload_extension(f'{filename}')
                    print("\033[94m"+f"hot-reloaded {filename}"+"\033[0m")
            except Exception as e:
                print("\033[91m"+f"ERROR: cannot hot-reload {filename}, raised error: {e}"+"\033[0m")
        await asyncio.sleep(0)

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles