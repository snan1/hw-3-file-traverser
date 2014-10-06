import pickle
import shelve

def process_data(pickle_file,shelve_file):
    global dict_words
    dict_words = {}
    wordList=[]
    i=0
    h=open(pickle_file,"br")
    mylist2=pickle.load(h)
    shelve_file = shelve.open(shelve_file)
    for quote_tuple in (mylist2):        
        quote_list=list(quote_tuple[1:])
        for quote_string in quote_list:
            words = quote_string.split()
            for word in words:
                dict_words.setdefault(word,[]).append(quote_tuple[0:1])

    for key,value in dict_words.items():
        shelve_file[key]=(value)
    h.close
    shelve_file.close()
    
    return dict_words
