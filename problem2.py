import re
from itertools import chain, permutations

class RackValidator:
    """Rack Validator takes the input from the user and outputs a valid rack, all lower case and no commas """
    def build_rack(self):
        while True:
            scrabble_rack = input("scrabble rack: ")
            scrabble_rack = scrabble_rack.replace(',','')
            scrabble_rack = scrabble_rack.replace(' ','')
            if len(scrabble_rack) < 8:
                if scrabble_rack.isalpha():
                    break
                else:
                    print("Please enter characters a-z only")
            else:
                print("Please only enter seven tiles")
        return(scrabble_rack)
    pass

    
class MatchValidator:
    """This Class returns match and the characteristics for the Word class """
    def list_of_outcomes(self,rack):
        """takes input of scrabble rack and creates all possible permutations """    
        temp_list_of_strings = []
        list_of_permutations = []
        lo, hi = 2, 7

        for perm in chain.from_iterable(permutations(rack, i) for i in range(lo, hi + 1)):
            temp_list_of_strings = (''.join(perm))
            list_of_permutations.append(temp_list_of_strings)
        return(list_of_permutations)

    def import_scrabble_list(self):
        """ takes scrabble words from list of scrabble words and inputs to list """
        scrable_file = open("scrabble_list.txt", "r")

        list_of_possible_scrabble_words = []
        for line in scrable_file:
            word_stripped_line = line.strip()
            word_stripped_line = word_stripped_line.lower()
            list_of_possible_scrabble_words.append(word_stripped_line)

        return(list_of_possible_scrabble_words)
    
    def matching_words(self,list_of_permutations,list_of_possible_scrabble_words):
        """takes both the list of permutations and compares to the list of words and creates a list of words found in both lists"""
        list_of_matching_words=[]
        for i in range(0,len(list_of_possible_scrabble_words)):
            if list_of_possible_scrabble_words[i]  in list_of_permutations:
                list_of_matching_words.append(list_of_possible_scrabble_words[i])    
        return(list_of_matching_words)
    
    def names(self, list_of_matching_words):
        name = []
        for word in list_of_matching_words :
            name.append(word)
        return(name)

    def scores(self, list_of_matching_words):
        """ this will score the list """

        scrabble_dict = {}
        score = {"a": 1 , "b": 3 , "c": 3 , "d": 2 ,
         "e": 1 , "f": 4 , "g": 2 , "h": 4 ,
         "i": 1 , "j": 8 , "k": 5 , "l": 1 ,
         "m": 3 , "n": 1 , "o": 1 , "p": 3 ,
         "q": 10, "r": 1 , "s": 1 , "t": 1 ,
         "u": 1 , "v": 4 , "w": 4 , "x": 8 ,
         "y": 4 , "z": 10}

        score_list = []
#   Initial score is 0 
        total=0
#   Looks at every word in the list_of_matching_words    
        for word in list_of_matching_words:
            total=0
            for letter in word:
                total = total + score[letter]
            scrabble_dict[word] = total
        score_list = list(scrabble_dict.values()) 
        return(scrabble_dict,score_list)

    def lengths (self, list_of_matching_words):
        length=[]
        list_of_matching_words = str(list_of_matching_words)
        for word in list_of_matching_words:
            length.append(len(word))
        return(length)


    pass

class Word:
    """A class that contains the attributes of aplicable words
    name:including the word itself
    score: the score of the word
    length: the length of the word"""
    def __init__(self,name,score,length):
        self.name = name
        self.score = score
        self.length = length

    def __str__(self):
        return "%s %s %s" %(self.name, self.score, self.length)
    pass

class Organize:   
    def dictionary_sort(self,scrabble_dict):
        """This will take a dictionary and return a sorted list"""  
 # The function works by sorting in reverse order of score
 # Since a dictionary cannot be ordered the result of this action is an ordered list       
        sorted_items = sorted(scrabble_dict.items(), key = lambda t:t[1], reverse=True)
        return(sorted_items)

    def organize_words_by_length (self,scrabble_options):
        """this functions takes the overall list of matching words
        and creates an individual sublist of each length of word from
        2 to 7. It returns these seven lists to main so they can be printed with specific requirments"""
        #This part of the code uses regular expression to match terms to each word length sublist    
        scrabble_options = str(scrabble_options)
        #print(scrabble_options)
        two_lwords =  re.findall(r"'\w{2}'\S\s\d+",scrabble_options)
        three_lwords =  re.findall(r"'\w{3}'\S\s\d+",scrabble_options)
        four_lwords =  re.findall(r"'\w{4}'\S\s\d+",scrabble_options)
        five_lwords =  re.findall(r"'\w{5}'\S\s\d+",scrabble_options)
        six_lwords =  re.findall(r"'\w{6}'\S\s\d+",scrabble_options)
        seven_lwords =  re.findall(r"'\w{7}'\S\s\d+",scrabble_options)
        if not two_lwords:
            two_lwords = "no words"
        if not three_lwords:
            three_lwords = "no words"
        if not four_lwords:
            four_lwords = "no words"
        if not five_lwords:
            five_lwords = "no words"
        if not six_lwords:
            six_lwords = "no words"
        if not seven_lwords:
            seven_lwords = "no words"
        return(two_lwords,three_lwords,four_lwords,five_lwords,six_lwords,seven_lwords)
    pass

def main():
    """this part of the problem brings the problem together"""
    player = RackValidator()
    a_rack = player.build_rack()
    mwords = MatchValidator()
    list_p = mwords.list_of_outcomes(a_rack)
    list_s = mwords.import_scrabble_list()
    list_m = mwords.matching_words(list_p,list_s)
    name = mwords.names(list_m)
    s_dict, score = mwords.scores(list_m)
    length = mwords.lengths(list_m)
    words = Word(name,score,length)
    print(words)
    order = Organize()
    sorted_items = order.dictionary_sort(s_dict)
    two_lwords,three_lwords,four_lwords,five_lwords,six_lwords,seven_lwords = order.organize_words_by_length(sorted_items)
    #This final print statement prints all of the sublists with the 10 highest scoring terms
    #Includes spacing and character sperators so that the user does not become confused
    print(r'2 Letter words','\n','-'*60,'\n', *two_lwords[:10],'\n'*5,
    '3 letter_words','\n','-'*60,'\n', *three_lwords[:10],'\n'*5, 
    '4 letter words','\n','-'*60,'\n',*four_lwords[:10],'\n'*5,
    '5 letter words','\n','-'*60,'\n',*five_lwords[:10],'\n'*5,
    '6 letter words','\n','-'*60,'\n',*six_lwords[:10],'\n'*5,
    '7 letter words','\n','-'*60,'\n', *seven_lwords[:10])    
    print(words)

if __name__ == "__main__":
    main()
