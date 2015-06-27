# as shown in http://rare-technologies.com/word2vec-tutorial/

import gensim, logging, os

# from gensim.models.word2vec import LineSentence

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

current_dir = os.path.dirname(os.path.realpath(__file__))

# each line represents a full chess match
input_dir = current_dir+"/../fen_output"
output_file = current_dir+"/../learned_vectors/output.model.bin"

sentences = MySentences(input_dir)
# sentences = LineSentence(input_dir+"/aa")

model = gensim.models.Word2Vec(sentences,workers=8)

# model.save_word2vec_format(output_file, binary=True)