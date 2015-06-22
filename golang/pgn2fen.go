
// the first command line argument is the path to the file to read
// the second command-line argument is the directory where to place the generated files

package main
import (
    "os"
    "log"
    "bufio"
    "fmt"
    "regexp"
    "time"
    "strings"

    "gopkg.in/wfreeman/pgn.v1"
    )
func main() {

    argsWithoutProg := os.Args[1:]

    if len(argsWithoutProg) == 0{
        printHelpAndExit()
    } 

    re := regexp.MustCompile(`^.+\/([^\/]+)$`)

    pgnFilePath := argsWithoutProg[0]

    fileName := re.FindAllStringSubmatch(pgnFilePath,-1)[0][1]

    targetDir := argsWithoutProg[1]

    err := os.Mkdir(targetDir,0755)

    if err != nil && os.IsNotExist(err){
        log.Fatal(err)
    }

    inFile,err := os.Open(pgnFilePath)

    if err != nil{
        log.Fatal(err)
    }

    outFile,err := os.Create(makeOutputFile(targetDir,fileName))

    if err != nil{
        log.Fatal(err)
    }

    w:= bufio.NewWriter(outFile)

    ps := pgn.NewPGNScanner(inFile)
    

    start := time.Now()

    ReadingGames:    
    for ps.Next() {
        // scan the next game
        game, err := ps.Scan()

        if err != nil {
            continue ReadingGames
        }

        // make a new board so we can get FEN positions
        b := pgn.NewBoard()

        //ReadingMoves:
        for _, move := range game.Moves {
            // make the move on the board
            err = b.MakeMove(move)

            // print out FEN for each move in the game
            fen := strings.TrimSpace(b.String())

            cleanLine := cleanFENString(fen)      

            w.WriteString(cleanLine)
        }
    }
    
    w.Flush()
    inFile.Close()
    outFile.Close()

    elapsed := time.Since(start)
    log.Printf("Prcessing took %s", elapsed)

}

func cleanFENString(input string) string{

    onlyPiecesRE := regexp.MustCompile(`^([^\/\s]+\/[^\/\s]+\/[^\/\s]+\/[^\/\s]+\/[^\/\s]+\/[^\/\s]+\/[^\/\s]+\/[^\/\s]+)\s.+$`)

    onlyPiecesMatch := onlyPiecesRE.FindAllStringSubmatch(input,-1)

    if onlyPiecesMatch == nil {
      log.Fatal("Invalid FEN!")
    }

    onlyPieces := onlyPiecesMatch[0][1]

    newLine := fmt.Sprint(onlyPieces," ")

    // replace forward slashes with underscores
    slashesRE := regexp.MustCompile(`\/`)
    newLine  = slashesRE.ReplaceAllString(newLine,"_")

    return newLine
}

func makeOutputFile(dirName, fileName string) string {

    re := regexp.MustCompile(`^.+?\/`)

    var dirNameTrailingSlash string = dirName

    if re.MatchString(dirName) {
        dirNameTrailingSlash = dirName 
    } else {
        dirNameTrailingSlash = fmt.Sprint(dirName,"/")
    }   

    outputFileName := fmt.Sprint("./",dirNameTrailingSlash,fileName)

    return outputFileName
}

func printHelpAndExit(){
    fmt.Println("")
    fmt.Println("Usage: go run pgn2fen.go <pathToInputPGNFile> <pathToOutputDirectory>")
    fmt.Println("")
    
    os.Exit(0)
}