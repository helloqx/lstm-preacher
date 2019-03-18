import os
import argparse
import pickle as pk

parser = argparse.ArgumentParser()
parser.add_argument("--data_dir", type=str, required=True, help="Path to unprocessed training texts.")
parser.add_argument("--vocab", type=str, help="Vocab file")
args = parser.parse_args()
args.data_dir = args.data_dir + "/"
class WordDict:

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

doclist = os.listdir(args.data_dir)
if args.vocab is not None:
    with open(args.vocab, 'rb') as doc:
        word_dict = pk.load(doc)
        print("Loaded vocab with {}".format(word_dict.vocab_sz))
else:
    word_dict = WordDict()

for file in doclist:
    file_path = args.data_dir + file
    if file[-4:] != ".txt":
        continue
    filename = file_path[:-4] + ".pkl"
    int_lst = []
    with open(file_path, 'r') as doc:
        for line in doc:
            for char in line.lstrip():
                idx = word_dict.add_word(char)
                int_lst.append(idx)
    with open(filename, 'wb') as pk_file:
        pk.dump(int_lst, pk_file)

with open(args.data_dir + 'vocab_{}.pkl'.format(word_dict.vocab_sz), 'wb') as pk_file:
    pk.dump(word_dict, pk_file)

print("Saved vocab with {}".format(word_dict.vocab_sz))