# LSTM Preacher
Teaching a machine to write sermons.

Char-based LSTM for writing Chinese sermons.

## Data
* 572 讲道s - locally-sourced, some repeated/empty.  
* 28 chapters of Matthew [(CNVS)](https://ebible.org/details.php?id=cmn-ncvs) 

Total of 4319 unique characters, including punctuation and newlines.

## Preprocess
Documents are preprocessed by removing all english characters, then converting to a list of integers.  
	e.g. 主内弟兄姐妹平安。 -> [246, 337, 97, 98, 5, 6, 584, 401, 25]
All documents are then combined into a single list of documents.

## Training & Generation
Run `./run.sh`.

## Architecture
Single layer LSTM.

## Sample Sermon Extracts
```
弟兄姐妹，你不要问自己，也知道天父上帝差了祂来的，并且知道天父爱世上的人，好像祂爱主耶稣一样。
意思，我是基督的宣教？
```
