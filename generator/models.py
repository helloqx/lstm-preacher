from keras.layers import Input, Embedding, LSTM, Dense, Bidirectional, Dropout
from keras.models import Model

valid_models = ['lstm', 'bilstm']

def get_model(args):
    if args.model_type == "lstm":
        return get_lstm_model(args)
    if args.model_type == 'bilstm':
        return get_bilstm_model(args)

def get_lstm_model(args):
    input_seq = Input(shape=(args.seq_len,),
                        dtype='int32')
    embedding_layer = Embedding(input_dim=args.vocab_sz,
                                output_dim=args.embed_dim,
                                trainable=True)
    lstm_layer = LSTM(args.lstm_dim)
    decode_layer = Dense(units=args.vocab_sz,
                         activation='softmax')

    embed = embedding_layer(input_seq)
    x = lstm_layer(embed)
    pred = decode_layer(x)
    model = Model(inputs=input_seq, 
                    outputs=pred)
    model.compile(loss='categorical_crossentropy', 
                    optimizer='adam', 
                    metrics=['accuracy'])
    print(model.summary())
    return model

def get_bilstm_model(args):
    input_seq = Input(shape=(args.seq_len,),
                        dtype='int32')
    embedding_layer = Embedding(input_dim=args.vocab_sz,
                                output_dim=args.embed_dim,
                                trainable=True)
    lstm_layer = Bidirectional(LSTM(args.lstm_dim))
    dropout_layer = Dropout(args.dropout_rate)
    decode_layer = Dense(units=args.vocab_sz,
                         activation='softmax')

    embed = embedding_layer(input_seq)
    x = lstm_layer(embed)
    x = dropout_layer(x)
    pred = decode_layer(x)
    model = Model(inputs=input_seq,
                    outputs=pred)
    model.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])
    print(model.summary())
    return model
