from my_pkg.TextFramework.Main.constant_enum import *
import tkinter as tk
from tkinter import filedialog as fd 

class MainFunc():
    def __init__(self):
        #self.__my_text=my_text
        pass
    
    def preprocessing_text(self,my_text,lib_name,function_name,param_dict):
        classname=LibraryBase.get(lib_name,"nltk")
        class_ref=classname(my_text)
        result=getattr(class_ref,function_name)(param_dict)
        return result
    
    def main_start(self,input_text,class_name,method_name):
#if __name__=='__main__':
    
        #main=MainFunc()
        #class_name = str(input("Enter the library input 1:nltk 2:spacy 3:Both   "))
        #input_text=input("Enter the text to pre-process :   ")
        
        '''method_name=str(input("Enter the method want to perform for preprocessing:\n 1:expandContractions \
                                \n 2:replace_func\n 3:tokenization\n 4:removeStopwords \
                                \n 5:lemmenization\n 6:partOfSpeech\n 7:namedEntity\n"))'''
        
        
        param_dict={"token type":"word"}
        
        print(self.preprocessing_text(input_text,class_name,method_name,param_dict))
        
    
        