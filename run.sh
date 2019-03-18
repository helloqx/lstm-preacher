#!/bin/bash
CUDA_VISIBLE_DEVICES=2,3 python main.py --doc_file documents_600.pkl --vocab_file vocab_4319.pkl --train --gen --lstm_dim 200

