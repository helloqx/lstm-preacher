import os
import pickle as pk
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data_dir", type=str, required=True, help="Path to unprocessed training texts.")
parser.add_argument("--doc_file", type=str, help="Pre-existing doc file")
args = parser.parse_args()
args.data_dir = args.data_dir + "/"

doclist = os.listdir(args.data_dir)

if args.doc_file is not None:
    with open(args.doc_file, 'rb') as pkl_file:
        documents = pk.load(pkl_file)
        print("{} documents found".format(len(documents)))
else:        
    documents = list()
for doc in doclist:
    if doc[-4:] != ".pkl" or doc[:5] == "vocab":
        continue
    with open(args.data_dir + doc, 'rb') as pkl_file:
        int_list = pk.load(pkl_file)
    documents.append(int_list)

with open(args.data_dir + 'documents_{}.pkl'.format(len(documents)), 'wb') as pk_file:
    pk.dump(documents, pk_file)
print("{} documents output".format(len(documents)))
