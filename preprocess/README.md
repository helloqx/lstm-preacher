# Preprocessing Scripts
`rename.sh`		- renames files to numeric, outputs index

`remove_eng.sh`		- removes english characters and spaces from .txt
`preprocess.py`		- changes .txt to list of integers and outputs vocab
`add_to_doclist.py`	- combines/adds .pkl list of integers to single .pkl file

## To Generate Doclist and Vocab
`python preprocess.py --data_dir <DATA-DIR>`
`python add_to_doclist.py --data_dir <DATA-DIR>`

## To Add to Existing Doclist and Vocab
`python preprocess.py --data_dir <DATA-DIR> --vocab <EXISTING-VOCAB>`
`python add_to_doclist.py --data_dir <DATA-DIR> --doc_file <EXISTING-DOCLIST>`
