__author__ = 'djstrong'

import cPickle

class SemanticDictionary():
    def __init__(self):
        f = open('semantic_dictionary.pkl', 'r')
        self.entries = cPickle.load(f)
        f.close()

if __name__ == "__main__":
    pass

