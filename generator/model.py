from keras.layers import Input, Embedding, LSTM, Dense
from keras.models import Model

def get_model(args)
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

