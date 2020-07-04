"""
Created on Wed Jul  1 20:12:41 2020

@author: sudersan
"""

from word_list import word_list
import random


class word_game:
    def __init__(self):
        
        w = word_list()
        self.word_list = w.words_list()
        
        self.words=list(self.word_list.keys())  
        self.hints=list(self.word_list.values())
        self.k = random.randint(0,len(self.word_list)-1)
        self.chosen_word=self.words[self.k]
        for i in range(0,2):
            self.r=random.randint(1,len(self.chosen_word)-1)
            self.chosen_word=self.chosen_word[:self.r]+"_"+self.chosen_word[self.r+1:]
        
    def quest(self):
        self.k = random.randint(0,len(self.word_list)-1)
        self.chosen_word=self.words[self.k]
        for i in range(0,2):
            self.r=random.randint(1,len(self.chosen_word)-1)
            self.chosen_word=self.chosen_word[:self.r]+"_"+self.chosen_word[self.r+1:]
        return(self.chosen_word,self.hints[self.k])
    def answer(self,ans):
            if(ans==self.words[self.k]):
                return(1)
            else:
                return(0)
