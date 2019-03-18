import pickle as pk
from generator.util import WordDict
with open('vocab_4319.pkl', 'rb') as asd:
  q = pk.load(asd)
z = "主内弟兄姐妹平安。"
for i in z:
  q.word_dict[i]
