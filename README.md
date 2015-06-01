# chess-word2vec
A couple of experiments using Google's word2vec tool to mine information from serialized chess matches

## Chess tools

- [lutanho.net PGN to FEN converter (javascript)](http://www.lutanho.net/pgn/pgn2fen.html)
 - Converts from PGN to FEN

- [Ruby chess toolkit and PGN parser](https://github.com/capicue/pgn)
 - can generate games (from pgn, fen or empty), play them interactively, convert any state to fen and output it in extended ascii to the command line

- [Chess.js](https://github.com/jhlywa/chess.js)
 - Mature JS lib; can be used in the browser or on nodeJS.
 - Has a method called `.validate_fen(fen)` that could be very useful to test the validity of a given FEN string.

- [PGN Parser in golang](https://github.com/wfreeman/pgn)
 - Parses PGN files and provides functions and primitives to cycle through games, moves and so on
 - The only lib that has an example of a PGN file consisting of many matches, and there's actually an example that takes each game, executes all moves for it and dumps the FEN representation after every move! Sounds exactly what I need.
 
## Word2vec

- [original word2vec github export](https://github.com/queirozfcom/word2vec)
- [Python implementation using the original C code for learning but Python for everything else](https://github.com/danielfrg/word2vec)
- [Deeplearning4j](https://github.com/deeplearning4j/deeplearning4j)
 - can do a whole lot more than just word2vec
 - Distributed/Parellel/GPU implementations
 - Plugs in nicely to MR, Spark, AWS, etc
 - 2K commits
- [gensim](https://github.com/piskvorky/gensim/)
- [word2vec on cuda](https://github.com/whatupbiatch/cuda-word2vec)

## Data

- [Millionbase 2.2 (1.4G worth of PGN files)](http://www.top-5000.nl/pgn.htm)
 - I've uploaded it to S3 but the link is private right now

### Other

- [chessboard.js (UI)](https://github.com/oakmac/chessboardjs/)

- [angular-chess (UI)](http://theborakompanioni.github.io/angular-chess/#/start)
 - Packages chessboard.jd and chess.js for use in AngularJS. Beautiful.

