"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """
    This class will return a random word from a list of words, it doesn't take any parameter.
    """
    
    def __init__(self, txt_address):
        """This will open words.txt, and create a new list based upon that file. 
        It will eliminate "\n" characters at the end of the line"""
        file = open(f"{txt_address}", "r")
        file_list = []
        self.word_counter = 0
        for line in file:
            file_list.append(line.rstrip("\n"))
            self.word_counter += 1
        file.close()
        self.file = file_list
        print(self.word_counter)
    
    def random(self):
        """This will return a random word from the list of words"""
        return self.file[randint(1, len(self.file))]

class SpecialWordFinder(WordFinder):
    """This return random items from every sub list marked down with # symbol"""
        
    def __init__(self):
        super().__init__()

    def random(self):
        output = self.file[randint(1, len(self.file))]
        while output is "" or output[0] == "#":
            output = self.file[randint(1, len(self.file))]
        else:
            return output
            

        








    

    

