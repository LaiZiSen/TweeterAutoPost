import os, getpass

folderPath = r"C:\Users\ROGUE\OneDrive\Desktop\Post To Tweeter"
imageFormats = (".tif",".png",".jpeg")

class GetFile ():
    def __init__ (self):
        self.folders = []
        self.pictures = []

        for Files in os.listdir(folderPath):
            self.Filter(Files)

    def Filter(self,filename):
        file = os.path.join(folderPath,filename)
        images = []
        if os.path.isfile(file):
            if file.endswith(imageFormats):
                self.pictures.append(file)
                print(self.pictures)
        else:
            for Files in os.listdir(file):
                if Files.endswith(imageFormats):
                    images.append(Files)
        if images:
            self.pictures.append(images)
GetFile()

def Post (Files):
    #post files with its path
    #may be in group
    pass