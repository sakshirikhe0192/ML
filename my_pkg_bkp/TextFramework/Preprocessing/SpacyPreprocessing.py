from my_pkg.TextFramework.Interface.PreprocessingInterface import PreprocessingInterface 
import spacy
from my_pkg.TextFramework.Preprocessing.Dict_contra import *
import re
#from spacy.lang.en import English
#nlp = English()


sp=spacy.load("en_core_web_sm")
#from Interface import PreprocInterface

class SpacyPreprocessing(PreprocessingInterface):
    
    def __init__(self, text_input): 
        self.__text_input = text_input
        self.__result=None
        
#expanding contraction
      
    def expandContractions(self, parameter_dictionary):
        c_re = re.compile('|'.join(cList.keys()))
        def replace(match):
            
            return cList[match.group()]#match.group() returns part of string where there is a match
        
        return c_re.sub(replace, self.__text_input)
        
    
#replacing special character,numbers,email,unicode

    def replace_func(self,parameter_dictionary): 
        text=self.expandContractions({})
        
        reg_ex=[r'\\u[0-9a-fA-Z]{4}','[0-9]+','[a-z,0-9,A-Z]+@[a-z]+.com','[^a-zA-z0-9]','^\s*|\s\s*']
        for i in reg_ex:
            text=re.sub(i, " ",text)
            self.__text_input=text
        self.__result=text
        return self.__result
    
        """We can perform remve tage by beautifulsoup also
        import re
        
        cleanr = re.compile('<.*?>')#.means character and this regex means between <> multiple character
        print(cleanr)
        cleantext = re.sub(cleanr, 'tag ', text_raw)
        print(cleantext)""" 
        
        
#assigning tokens to words

    def tokenization(self,parameter_dictionary): 
        words=self.replace_func({})       
        doc=sp(words)#nlp" Object is used to create documents with linguistic annotations.
        list1=[]
        for i in doc:#we can split by sentence using new_text.sents
            list1.append(i.text)
            
        self.__result=list1
        return  self.__result
    
#removing stop words

    def removeStopwords(self,parameter_dictionary):
        words=self.tokenization({})
        str=" "
        parameter_dictionary=str.join(words)
        doc=sp(parameter_dictionary)
        filtered_text=[]
        filtered_text=[i.text for i in doc if not i.is_stop]
        """lexeme=nlp.vocab[i]
            if lexeme.is_stop==False:
                filtered_text.append(i)"""    
        self.__result=filtered_text
        return self.__result
    
  #performing Lemminization
  
    def lemmenization(self,parameter_dictionary):
        #words=word_tokenize(self.__text_input)
        words=self.removeStopwords({})
        str=" "
        parameter_dictionary=str.join(words)
        doc=sp(parameter_dictionary)
        res=[]
        for w in doc:
            res.append(w.lemma_)
        self.__result=res
        return self.__result
    
#assigning part of sppech to tokenzed words   
        
    def partOfSpeech(self,parameter_dictionary):
        words=self.lemmenization({})
        str=" "
        parameter_dictionary=str.join(words)
        doc=sp(parameter_dictionary)
        tagged_words=[]
        for i in doc:
            tagged_words.append((i.text,i.pos_,i.tag_,spacy.explain(i.tag_)))
        self.__result=tagged_words
        return self.__result

#assigning named entity to part of speech
       
    def namedEntity(self,parameter_dictionary):
        words=self.removeStopwords({})
        str=" "
        parameter_dictionary=str.join(words)
        doc=sp(parameter_dictionary)
        
        named_entities=[(entity.text + ' - ' + entity.label_ + ' - ' + spacy.explain(entity.label_)) for entity in doc.ents]
        self.__result=named_entities
        return self.__result
    
    """def dict_Preprocessing(self,method_name):
            sp_method_dict={'1':(self.expandContractions({}),'expandContractions'),
                            '2':(self.replace_func({}),'replace_func'),
                            '3':(self.tokenization({"token type":"word"}),'tokenization'),
                            '4':(self.removeStopwords({}),'removeStopwords'),
                            '5':(self.lemmenization({}),'lemmenization'),
                            '6':(self.partOfSpeech({}),'partOfSpeech'),
                            '7':(self.namedEntity({}),'namedEntity')}
            for j in method_name:
                print("Running for SpaCy:",sp_method_dict[j][1])
                res=sp_method_dict[j][0]
                print(res)
                
                print("****************************")"""
                