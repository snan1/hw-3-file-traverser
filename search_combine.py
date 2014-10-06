import searcher
import indexer
import data_load
dict_words = indexer.process_data("raw_data.txt","shelve_file")
searcher.search("shelve_file")
