import chess
import chess.engine

def print_board(board):
    print(board)

def main():
    board = chess.Board()
    while not board.is_game_over():
        print_board(board)
        move = input("Enter your move (in UCI format, e.g., e2e4): ")
        
        if move == "exit":
            print("Game exited.")
            break
        
        try:
            board.push_uci(move)
        except ValueError:
            print("Invalid move! Try again.")
            continue
    
    print("Game over!")
    print("Result:", board.result())

if __name__ == "__main__":
    main()
