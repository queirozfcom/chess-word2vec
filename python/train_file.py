#!/usr/bin/env python
import sys,logging, os
from gensim.models import word2vec

def usage():
    txt = """
        Usage: python train_file.py <input_file> <output_file>

        Where
            <input_file> is the path to the text file used for training, e.g. ../fen_output/aa
            <output_file> is the path where the model (in text form) will be saved. Default value is ../learned_vectors/output.model.txt
        """
    print(txt)  


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def main(input_file,output_file):

	current_dir = os.path.dirname(os.path.realpath(__file__))

	path_to_input  = current_dir+"/"+input_file
	path_to_output = current_dir+"/"+output_file


	sentences = word2vec.LineSentence(path_to_input)

	model = word2vec.Word2Vec(sentences,workers=8)

	model.save(path_to_output)


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) not in [1,2]:
        usage()
        sys.exit(2)
    else:
        input_file = args[0]
        output_file = args[1] if len(args) == 2 else "../learned_vectors/output.model.txt" 
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        main(input_file,output_file)