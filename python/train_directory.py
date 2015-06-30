#!/usr/bin/env python
import sys, gensim, logging, os


def usage():
    txt = """
        Usage: python train_directory.py <input_dir> <output_file>

        Where
            <input_dir> is the path to the directory where files used for training can be found, e.g. ../fen_output
            <output_file> is the path where the model (in binary form) will be saved. Default value is ../learned_vectors/output.model.bin
        """
    print(txt)  



class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()



def main(input_dir,output_file):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    path_to_dir = current_dir+"/"+input_dir
    path_to_output_file = current_dir+"/"+output_file

    sentences = MySentences(input_dir)

    model = gensim.models.Word2Vec(sentences,workers=8)    

    model.save_word2vec_format(path_to_output_file,binary=True)
    


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) not in [1,2]:
        usage()
        sys.exit(2)
    else:
        input_dir = args[0]
        output_file = args[1] if len(args) == 2 else "../learned_vectors/output.model.bin" 
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        main(input_dir,output_file)







