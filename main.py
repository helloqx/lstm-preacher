import argparse
import pickle as pk
from generator.util import WordDict

parser = argparse.ArgumentParser()

paths = parser.add_argument_group(title='File Paths')
paths.add_argument("--doc_file", help='.pkl file of documents (list of list of ints)')
paths.add_argument("--vocab_file", required=True, help='.pkl vocab file')
paths.add_argument("--model_file", help='Pre-trained model file')

train = parser.add_argument_group(title='Training Details')
train.add_argument("--train", action="store_true", help="Train model")
train.add_argument("--seq_len", type=int, default=15, help='Length of input_seq')
train.add_argument("--no_pad", action="store_false", help='Do not pad beginning of documents')
train.add_argument("--embed_dim", type=int, default=200, help='Dimensions for embeddings')
train.add_argument("--lstm_dim", type=int, default=200, help='Dimensions for LSTM')
train.add_argument("--num_epochs", type=int, default=50, help='Num epochs')
train.add_argument("--model_out", type=str, default="model", help='Name of output trained model file')

gen = parser.add_argument_group(title='Generation Details')
gen.add_argument("--gen", action="store_true", help="Use model to generate text")
gen.add_argument("--gen_len", type=int, default=300, help='Length to generate')
gen.add_argument("--text_out", default="text", help='Name of output text file')
    
args = parser.parse_args()

################################################################################
## Validate arguments
assert (args.train or args.gen), "Choose either train or gen."
if args.gen and not args.train:
    assert (args.model_file is not None), "Need pre-trained model file."
if args.train:
	assert (args.doc_file is not None), "Need document file"

################################################################################
## Load and Prep Data
with open(args.vocab_file, 'rb') as read_file:
    vocab = pk.load(read_file)

args.vocab_sz = vocab.vocab_sz

if args.train:
    from generator import data_prep
    with open(args.doc_file, 'rb') as read_file:
        doc_file = pk.load(read_file)
    x, y = data_prep.get_sequences(doc_file, args)

################################################################################
## Train Model
if args.train:
    from generator import models
    from keras.callbacks import EarlyStopping
    callbacks = [
        EarlyStopping(monitor='loss', patience=3, verbose=0)]
    model = models.get_model(args)
    model.fit(x, y, 
                epochs=args.num_epochs,
                verbose = 2,
                callbacks=callbacks)
    model.save(args.model_out + '.h5')

################################################################################
## Generate Text

if args.gen:
    import numpy as np
    from generator.util import get_starter_phrase

    if not args.train:
        from keras.models import load_model
        model = load_model(args.model_file)

    starter = get_starter_phrase(vocab)
    in_text = ([0] * (args.seq_len - len(starter))) + starter
    in_text = np.array(in_text)

    for _ in range(args.gen_len):
        encoded = np.expand_dims(in_text[-args.seq_len:], axis=0)
        pred = model.predict(encoded)
        pred = pred.argmax(axis=-1)
        in_text = np.append(in_text, pred)

    with open(args.text_out + ".txt", 'w') as out_file:
        for i in in_text:
            out_file.write(vocab.get_word_from_idx(i))
