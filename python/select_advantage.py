#!/usr/bin/env python
import logging,os,re,sys


def main(color,threshold):
	current_dir = os.path.dirname(os.path.realpath(__file__))

	input_file = current_dir+"/../aa_vocab_min_count_2"
	output_file = current_dir+"/./"+color+"_adv.out.txt"

	valid_line = re.compile('^(\w+)\/(\w+)\/(\w+)\/(\w+)\/(\w+)\/(\w+)\/(\w+)\/(\w+)\s\d+$')
	suffix = ' w KQkq e3 0 1'

	out = open(output_file,'w')

	with open(input_file) as f:
		for line in f:
			
			whites = 0
			blacks = 0
			match = valid_line.match(line)
			
			if match is None:
				continue
			else:
				for grp in match.groups():
					for char in grp:
						if char.isalpha() and char.istitle():
							whites += 1
						elif char.isalpha() and (not char.istitle()):
							blacks += 1
						else:
							continue		

				if color == 'white':
					if whites - blacks > threshold:
						lineclean  = re.sub(' \d+$','',line)+suffix+"\n"

						out.write(lineclean)
				else:
					if blacks - whites > threshold:
						lineclean  = re.sub(' \d+$','',line)+suffix+"\n"
						out.write(lineclean)	

			# next game
			whites = 0
			blacks = 0			
			
	out.close()		

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) !=  2:
    	print("MUST INFORM COLOR and THRESHOLD!\n\n")
        sys.exit(2)
    else:
        color=args[0]
        threshold = args[1]
        main(color,threshold)