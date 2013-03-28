__author__ = 'djstrong'

example = {'synonymy': [],
           'similar to': [],
           'is a part of': [],
           'consists of': [],
           'is a': [],
           'is a kind of': [],
           'destination': [],
           'role': [],
           'action': {'positive': [], 'negative': [], 'passive': []},
           'state': {'positive': [], 'negative': []},
           'cause': [],
           'efect': []
}

entries = [
    {'synonymy': [],
     'similar to': [],
     'is a part of': [],
     'consists of': [],
     'is a': [],
     'is a kind of': [],
     'destination': [],
     'role': [],
     'action': {'positive': [], 'negative': [], 'passive': []},
     'state': {'positive': [], 'negative': []},
     'cause': [],
     'efect': []
    },
    {'synonymy': [],
     'similar to': [],
     'is a part of': [],
     'consists of': [],
     'is a': [],
     'is a kind of': [],
     'destination': [],
     'role': [],
     'action': {'positive': [], 'negative': [], 'passive': []},
     'state': {'positive': [], 'negative': []},
     'cause': [],
     'efect': []
    }
]

import cPickle
f = open('semantic_dictionary.pkl', 'w')
cPickle.dump(entries, f, -1)
f.close()