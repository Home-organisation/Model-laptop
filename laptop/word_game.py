"""
Created on Wed Jul  1 20:12:41 2020

@author: sudersan
"""

from word_list import word_list



class word_game:
    if __name__=="__main__":
        import random
        
        w = word_list()
        word_list = w.words_list()
        
        words=list(word_list.keys())  
        hints=list(word_list.values())
        
                
        flag=0
        while(True):
            if(flag==0):
                k=random.randint(0,len(word_list)-1)
                chosen_word=words[k]
                for i in range(0,2):
                    r=random.randint(1,len(chosen_word)-1)
                    chosen_word=chosen_word.replace(chosen_word[r],"_")
            print("Find the word:",chosen_word)
            print("Hint:",hints[k])
            ans=input()
            if(ans==words[k]):
                print("Great....")
                flag=0
            else:
                print("Try again...")
                flag=1
            h=input("Do you want to continue playing:(Y/N):")
            if(h=='N'):
                break
