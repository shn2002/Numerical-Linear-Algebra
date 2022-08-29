################################################################################
# Composite design pattern
#
# Purpose: A composite design pattern example in Python for calculating the
# size in a file and folder system.  In this example, the files are the leaf
# nodes in the pattern, and the folders are the composite nodes.  Composite
# design pattern: https://en.wikipedia.org/wiki/Composite_pattern
#
# Author: Kevin Browne
# Contact: brownek@mcmaster.ca
#
################################################################################

from abc import ABC, abstractmethod


# Components must have a size operation
class Component(ABC):

    @abstractmethod
    def size(self, components):
        pass

    def number(self, components):
        pass


# File components simply return their size for the size operation
class File(Component):

    def __init__(self, name, size):
        self.__name = name
        self.__size = size
        self.__number = 1

    def size(self):
        return self.__size

    def number(self):
        return self.__number


# Folder components return the sum of all the components (files, folder) they
# contain for the size operation
class Folder(Component):

    def __init__(self, name, components):
        self.__name = name
        self.__components = components

    def size(self):
        total = 0
        for component in self.__components:
            total = total + component.size()
        return total

    def number(self):
        total = 0
        for component in self.__components:
            total = total + component.number()
        return total


# Create objects to represent a file system with the following tree:
#
#            ___________________________________System (folder)______
#           /                                   /                     \
#     Documents (folder)        Downloads (folder)              Desktop (folder)
#    /          |       \           /         \                /             \
# resume.doc cover.doc  ref.pdf  imgA.png  GoT (folder)  meeting.txt    todo.txt
#                                             |
#                                          S07E05.mp4
#
documents = Folder("Documents", [File("resume.doc", 1024), \
                                 File("cover.doc", 2048), \
                                 File("ref.pdf", 4096)])
desktop = Folder("Desktop", [File("todo.txt", 1024), File("meeting.txt", 2048)])
downloads_subfolder = Folder("GoT", [File("S07E05.mp4", 16384)])
downloads = Folder("Downloads", [File("img.png", 8192), \
                                 downloads_subfolder])
system = Folder("System", [documents, desktop, downloads])

# Output some of the size values of the different folders and entire system
print(documents.size())
print(desktop.size())
print(downloads_subfolder.size())
print(downloads.size())
print(system.size())


print(documents.number())
print(desktop.number())
print(downloads_subfolder.number())
print(downloads.number())
print(system.number())