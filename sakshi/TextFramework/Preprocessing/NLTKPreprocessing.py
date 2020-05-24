from Interface.PreprocessingInterface import PreprocessingInterface 
#from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import re
from Preprocessing.Dict_contra import *
#from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
import nltk
#nltk.download('punkt')#an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences
#nltk.download('wordnet')# is a database of English containing noun, verbs, adjective,advrbs, freely avaliable
#nltk.download('stopwords')

class NLTKPreprocessing(PreprocessingInterface):
    
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
        new_text=self.replace_func({})
        token_type=parameter_dictionary.get("token type","sent")
        
        if token_type=="word":
            #tokenizer.train(self.__text_input)
            res=word_tokenize(new_text)
        else:
            res=sent_tokenize(new_text)
            
        self.__result=res
        return self.__result
    
#removing stop words

    def removeStopwords(self,parameter_dictionary):
        stop_words=set(stopwords.words('english'))
        words=self.tokenization({"token type":"word"})
        
        filtered_words= [w for w in words if not w in stop_words]
        self.__result=filtered_words
        return self.__result
    
 #performing stemming
 
    def stemming(self,parameter_dictionary):
        ps = PorterStemmer()
        #words=word_tokenize(self.__text_input)
        words=self.removeStopwords({})
        res=[]
        for w in words:
            res.append(ps.stem(w)) 
        self.__result=res
        return self.__result
    
  #performing Lemminization
  
    def lemmenization(self,parameter_dictionary):
        #words=word_tokenize(self.__text_input)
        words=self.removeStopwords({})
        ls = WordNetLemmatizer()
        res=[]
        for w in words:
            res.append(ls.lemmatize(w)) 
        self.__result=res
        return self.__result
    
#assigning part of sppech to tokenzed words   
        
    def partOfSpeech(self,parameter_dictionary):
        words=self.lemmenization({})
        tagged_words = nltk.pos_tag(words)#will give part of speech tag to words, will give list of tuple
        self.__result=tagged_words
        return self.__result

#assigning named entity to part of speech
       
    def namedEntity(self,parameter_dictionary):
        tagged_words=self.partOfSpeech({})
        ne_chunked_sents = nltk.ne_chunk(tagged_words)#it will chunk data with named entitiy
        named_entities = []
        for tagged_tree in ne_chunked_sents:
                if hasattr(tagged_tree, 'label'):#label will be named entity and leaves will be POS
                    
                    entity_name = ' '.join(c[0] for c in tagged_tree.leaves())#('computer', 'NN') 
                    entity_type = tagged_tree.label() # get NE category
                    named_entities.append((entity_name, entity_type))
        self.__result=named_entities
        return self.__result
    
    """def dict_Preprocessing(self,method_name):
            nk_method_dict={'1':(self.expandContractions({}),'expandContractions'),
                            '2':(self.replace_func({}),'replace_func'),
                            '3':(self.tokenization({"token type":'word'}),'tokenization'),
                            '4':(self.removeStopwords({}),'removeStopwords'),
                            '5':(self.lemmenization({}),'lemmenization'),
                            '6':(self.partOfSpeech({}),'partOfSpeech'),
                            '7':(self.namedEntity({}),'namedEntity')}
            for j in method_name:
                print("Running for NLTK:",nk_method_dict[j][1])
                res=nk_method_dict[j][0]
                print(res)
                
                print("****************************")"""
               
        
    