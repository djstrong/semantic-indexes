# -*- coding: utf-8 -*-

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
           'effect': []
}

entries = [
    {'synonymy': ['więzienie', 'kryminał'],
     'similar to': ['puszka', 'pudło', 'kić', 'pierdel', 'mamer', 'areszt'],
     'is a part of': [],
     'consists of': ['więzień'],
     'is a': [],
     'is a kind of': [],
     'destination': ['więzić'],
     'role': ['kara'],
     'action': {'positive': [], 'negative': [], 'passive': []},
     'state': {'positive': [], 'negative': []},
     'cause': ['przestępstwo', 'wyrok'],
     'effect': []
    },
    {'synonymy': ['bunt'],
     'similar to': [],
     'is a part of': [],
     'consists of': ['buntownik'],
     'is a': [],
     'is a kind of': ['sprzeciw', 'opór', 'protest'],
     'destination': [],
     'role': [],
     'action': {'positive': [], 'negative': [], 'passive': ['stłumić']},
     'state': {'positive': [], 'negative': []},
     'cause': [],
     'effect': ['śmierć']
    },
    {'synonymy': ['śmierć', 'zgon', 'skon', 'odejście', 'skon'],
     'similar to': [],
     'is a part of': ['życie'],
     'consists of': [],
     'is a': ['męczeństwo', 'ukrzyżowanie'],
     'is a kind of': ['kres', 'koniec'],
     'destination': [],
     'role': [],
     'action': {'positive': [], 'negative': [], 'passive': []},
     'state': {'positive': [], 'negative': []},
     'cause': ['agonia', 'konanie', 'umieranie', 'zabójstwo'],
     'effect': ['pogrzebanie']
    },
    {'synonymy': ['więzień', 'osadzony'],
     'similar to': ['pasiak', 'kiciarz'],
     'is a part of': ['więzienie'],
     'consists of': [],
     'is a': ['zakładnik'],
     'is a kind of': ['osoba'],
     'destination': [],
     'role': [],
     'action': {'positive': ['odsiadywać'], 'negative': ['uciekać'], 'passive': ['więzić']},
     'state': {'positive': [], 'negative': []},
     'cause': [],
     'effect': []
    },
    {'synonymy': ['buntownik'],
     'similar to': ['nonkonformista', 'niekonformista'],
     'is a part of': ['bunt'],
     'consists of': [],
     'is a': ['anarchista', 'rewolucjonista'],
     'is a kind of': ['osoba', 'przeciwnik', 'oponent', 'bojownik'],
     'destination': ['bunt'],
     'role': [],
     'action': {'positive': ['buntować'], 'negative': [], 'passive': []},
     'state': {'positive': [], 'negative': []},
     'cause': [],
     'effect': []
    },
    {'synonymy': ['człowiek', 'osoba'],
     'similar to': [],
     'is a part of': [],
     'consists of': [],
     'is a': [],
     'is a kind of': [],
     'destination': [],
     'role': [],
     'action': {'positive': [], 'negative': [], 'passive': []},
     'state': {'positive': [], 'negative': ['więzień']},
     'cause': ['narodziny'],
     'effect': []
    }
]

import cPickle

f = open('semantic_dictionary.pkl', 'w')
cPickle.dump(entries, f, -1)
f.close()