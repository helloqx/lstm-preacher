#!/bin/bash
CUDA_VISIBLE_DEVICES=2,3 python main.py --doc_file documents_297.pkl --vocab_file vocab_3842.pkl --train --gen --lstm_dim 200 --model_type bilstm

