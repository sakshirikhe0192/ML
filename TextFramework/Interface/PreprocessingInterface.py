from abc import ABC, abstractmethod

class PreprocessingInterface(ABC):
    
    @abstractmethod
    def expandContractions(self,parameter_dictionary): 
        pass
    
    @abstractmethod
    def replace_func(self,parameter_dictionary): 
        pass
    
    @abstractmethod
    def tokenization(self,parameter_dictionary): 
        pass
    
    """@abstractmethod
    def stemming(self,parameter_dictionary):
        pass"""
    
    @abstractmethod
    def removeStopwords(self,parameter_dictionary):
        pass
    
    @abstractmethod
    def lemmenization(self,parameter_dictionary):
        pass
    
    @abstractmethod
    def partOfSpeech(self,parameter_dictionary):
        pass
    
    @abstractmethod
    def namedEntity(self,parameter_dictionary):
        pass
    
    
    
    
    
    
    
    
    
    
    
    