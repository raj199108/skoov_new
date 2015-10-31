"""
*******************************************************************************************************************************
FILE NAME:              Subwords.py
PURPOSE:                This module derives all possible subwords from the given list of words
CREATED BY:             Rajkumar T
MODIFICATION HISTORY :  Created on 31/10/2015
********************************************************************************************************************************
"""
try:
    from itertools import chain, combinations
    import enchant
#    from nltk.corpus import words
    import traceback
except:       
    print "Could not import required modules!!"
    print traceback.format_exc()

"""
********************************************************************************************************************************************************
CLASS NAME:            Subwords
PURPOSE:               This class serves the purpose of deriving the possible subwords form the given list of words ans writes them to a .txt file
********************************************************************************************************************************************************
"""    

class Subwords:

    """
*********************************************************************************************************************************
FUNCTION NAME:          __init__
PURPOSE:                To open the input file 'words.txt' to read and to create and open the output file 'output.txt' to write to
********************************************************************************************************************************
    """    
    def __init__(self):
        self.output_file = open("output.txt","w")
        self.input_file = open("words.txt", 'r')
        
    """
*********************************************************************************************************************************
FUNCTION NAME:          readfile
PURPOSE:                To read each word form the input file 'words.txt' and pass each word to the function possible_words
********************************************************************************************************************************
    """       
    def readfile(self):
        try:
            for line in self.input_file:
                self.possible_words(line.strip("\n")) #removing all the newlines while reading the words form the file
             #  possible_words("amicable")
        except:
            print("Error while reading file!!")
            print traceback.format_exc() 
    """
*********************************************************************************************************************************
FUNCTION NAME:          powerset
PURPOSE:                To find all the combinations of subwords possible from each of the word passed by readfile
********************************************************************************************************************************
    """                            
    def powerset(self,iterable):       
        "powerset([a,b,c]) --> () (a,) (b,) (c,) (a,b) (a,c) (b,c) (a,b,c)"
        try:
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s)+1)) #returning all possible word combinations from the letters in the given word
        except:
            print("Error while generating combinations!!")
            print traceback.format_exc()    
    """
*********************************************************************************************************************************
FUNCTION NAME:          possible_words
PURPOSE:                To filter all the meaningful words from the list of combinations provided by the powerset function 
********************************************************************************************************************************
    """    
    def possible_words(self,main_word):
        try:
            po_words = (list(map(''.join, self.powerset(main_word)))) #calling the powerset function to get all possbile combinations for the given word
            d = enchant.Dict("en_US") #using the english-US dictionary in the PyEnchant module
            for i in range(1,len(po_words)): # looping through all the word combinations and comparing it with the dictionary to find the meaningful words
                word = po_words[i]
                if (d.check (word) and len(word)>1): # checking if the combinations generated are in the dictionary; d.check("string") returns true if the word exists in the dictionary and elimiating all the single letters
                    self.write_word(main_word,word)           
        except:
            print("Error while deriving words!!")
            print traceback.format_exc()
    """
*********************************************************************************************************************************
FUNCTION NAME:          write_word
PURPOSE:                To wirte the meaningful words from possible_words function to the output file 'output.txt' 
********************************************************************************************************************************
    """                        
    def write_word(self,main_word,word):
        try:
            li_word= list(word)
            actual_word = main_word
            if(word != actual_word):# eliminating the main_word which will be a part of the combinations generated
                for i in li_word:
                    actual_word= actual_word.replace(i,"",1) # replacing the letters in the main word with "" for the common letters in the meaningful word derived and the main_word
                print ('%s => %s (minus "%s") \n' %(main_word,word,actual_word))
                self.output_file.write('%s => %s (minus "%s") \n' %(main_word,word,actual_word)) # writing to the outputfile 'output.txt'
        except:
            print("Error while writing word!!")
            print traceback.format_exc()
    """
*********************************************************************************************************************************
FUNCTION NAME:          close
PURPOSE:                To close the input and the output files
********************************************************************************************************************************
    """                                         
    def close(self):
        try:
            self.output_file.close()
            self.input_file.close()
        except:
            print("Unable to close files!!")
            print traceback.format_exc()    
        
"""
*********************************************************************************************************************************
FUNCTION NAME:          main
PURPOSE:                To instantiate the class subwords and to call the driving function readfile
********************************************************************************************************************************
"""           
def main():
    try:
        obj1 = Subwords()
        obj1.readfile()
        obj1.close()
    except:
        print("File Creation Failed!!")
        print traceback.format_exc()


if __name__ == "__main__":
    main()        
        




                
            