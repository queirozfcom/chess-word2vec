#!/usr/bin/env python
import sys,logging, os
from gensim.models.word2vec import Word2Vec

def usage():
    txt = """
        Load a previously saved vector model and open a python shell to manipulate it

        Usage: python -i load_model.py <text_model>

        Where
            <text_model> is the path to the previously saved model (in text format), e.g. ../fen_output/learned_vectors/output.model.txt
        """
    print(txt)  

print(__name__)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def main(model_file):

	current_dir = os.path.dirname(os.path.realpath(__file__))

	path_to_model_file  = current_dir+"/"+model_file
	global model
	model = Word2Vec.load(path_to_model_file,binary=False)

	print("\nLook at https://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.Word2Vec to see all interesting things you can do with a model.\n")
	print("The model has been loaded into a variable called model.")
	print("You can use it now. (but you'll need to re-import modules like gensim if you want to use module-level functions)\n\n")




if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 1:
        usage()
        sys.exit(2)
    else:
        input_model_file = args[0]
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        main(input_model_file)