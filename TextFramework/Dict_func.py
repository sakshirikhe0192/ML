class Dict_func():

    def dict_NLTKPreprocessing(input_text,method_name):
        nk_method_dict={'1':(nk.expandContractions({}),'expandContractions'),
                        '2':(nk.replace_func({}),'replace_func').
                        '3':(nk.tokenization({"token type":"word"}),'tokenization'),
                        '4':(nk.removeStopwords({}),'removeStopwords'),
                        '5':(nk.lemminization({}),'lemminization'),
                        '7':(nk,partOfSpeech({}),'partOfSpeech'),
                        '8':(nk.namedEntity({}),'namedEntity')}
        for j in method_name:
            print("Running for NLTK:",nk_method_dict[j][1])
            res=nk_method_dict[j]
            print(res)
        
    def dict_SpaCyPreprocessing(input_text,method_name):
        sp_method_dict={'1':(sp.expandContractions({}),'expandContractions'),
                        '2':(sp.replace_func({}),'replace_func').
                        '3':(sp.tokenization({"token type":"word"}),'tokenization'),
                        '4':(sp.removeStopwords({}),'removeStopwords'),
                        '5':(sp.lemminization({}),'lemminization'),
                        '7':(sp,partOfSpeech({}),'partOfSpeech'),
                        '8':(sp.namedEntity({}),'namedEntity')}
        for j in method_name:
            print("Running for NLTK:",sp_method_dict[j][1])
            res=nk_method_dict[j]
            print(res)