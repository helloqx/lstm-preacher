from numpy import array
from keras.utils import to_categorical

def get_sequences(seq_file, args):
    sequences = []
    for doc in seq_file:
        if not args.no_pad:
            doc = ([0] * args.seq_len) + doc
        for i in range(args.seq_len, len(doc)):
            seq = doc[i - args.seq_len:i + 1]
            sequences.append(seq)
    sequences = array(sequences)
    x, y = sequences[:,:-1], sequences[:,-1]
    y = to_categorical(y, num_classes=args.vocab_sz)
    print("{} sequences of len {}".format(len(sequences), args.seq_len))
    return x, y