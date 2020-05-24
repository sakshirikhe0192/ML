from Preprocessing.NLTKPreprocessing import *
from Preprocessing.SpacyPreprocessing import *
from ProcessingFactory import *
import tkinter as tk
from tkinter import filedialog as fd 


def preprocessing_text(parameter_dictionary):
            #print(parameter_dictionary)
            text=parameter_dictionary.get('text')
            key=parameter_dictionary.get('className')
            class_name_dict={'1':[NLTKPreprocessing(text)],
                             '2':[SpaCyPreprocessing(text)],
                             '3':[SpaCyPreprocessing(text),
                                  NLTKPreprocessing(text)]}
            module_name=class_name_dict[key]
            return module_name
        
if __name__=="__main__":
    
    try:
        class_name = input("Enter the library input 1:NLTK 2:SpaCy 3:Both   ")
        print("Choose file")
        name= fd.askopenfilename() 
        with open(name,"r") as f:
            input_text = f.read()
                  
        tk.Button(text='File Open').pack(fill=tk.X)
        tk.mainloop()
          
        method_name=str(input("Enter the method want to perform for preprocessing:\n 1:expandContractions \
                                \n 2:replace_func\n 3:tokenization\n 4:removeStopwords \
                                \n 5:lemmenization\n 6:partOfSpeech\n 7:namedEntity\n")).split()
        input_dict={'className':class_name,'text':input_text}
        pt=preprocessing_text(input_dict)
        module_name=pt
        #print(module_name,type(module_name))
    
        for j in module_name:
            for i in method_name:
                result = getattr(j, i)({})
                print("Running for {0} :{1}".format(j.__class__.__name__,i)+"\n"+result)     
    except FileNotFoundError :
        print("Please select correct file")
      #except NameError:
        #print("Name is not correct")        

       
        
