# chess-word2vec
A couple of experiments using Google's word2vec tool to mine information from serialized chess matches

## Potential tools

- [lutanho.net PGN to FEN converter (javascript)](http://www.lutanho.net/pgn/pgn2fen.html)
 - Converts from PGN to FEN

- [Ruby chess toolkit and PGN parser](https://github.com/capicue/pgn)
 - can generate games (from pgn, fen or empty), play them interactively, convert any state to fen and output it in extended ascii to the command line

- [Chess.js](https://github.com/jhlywa/chess.js)
 - Mature JS lib; can be used in the browser or on nodeJS.

- [PGN Parser in golang](https://github.com/wfreeman/pgn)
 - Parses PGN files and provides functions and primitives to cycle through games, moves and so on
 - The only lib that has an example of a PGN file consisting of many matches, and there's actually an example that takes each game, executes all moves for it and dumps the FEN representation after every move! Sounds exactly what I need.
 
### UI
Who knows?

- [chessboard.js](https://github.com/oakmac/chessboardjs/)

- [angular-chess](http://theborakompanioni.github.io/angular-chess/#/start)
 - Packages chessboard.jd and chess.js for use in AngularJS. Beautiful.

