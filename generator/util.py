import pickle as pk

class WordDict:
    '''
        Stores dict of word:index and index:word
    '''
    def __init__(self):
        self.word_dict = {'UNK': 0}
        self.vocab_sz = 1
        self.inv_dict = {}

    def __len__(self):
        return self.vocab_sz

    def add_word(self, word):
        if word not in self.word_dict:
            self.word_dict[word] = self.vocab_sz
            self.vocab_sz += 1
        return self.word_dict[word]

    def get_reverse_dict(self):
        for k, v in self.word_dict.items():
            self.inv_dict[v] = k

    def get_word_from_idx(self, idx):
        if len(self.inv_dict) != self.vocab_sz:
            self.get_reverse_dict()
        return self.inv_dict[idx]


def get_starter_phrase(vocab_file, phrase=None):
    if phrase is None:
        phrase = "主内弟兄姐妹平安。"
    with open(vocab_file, 'rb') as vcb_file:
        vocab = pk.load(vcb_file)
    starter = []
    for char in phrase:
        starter.append(vocab.add_word(i))
    return starter
