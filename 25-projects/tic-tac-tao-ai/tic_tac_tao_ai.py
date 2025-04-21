import google.generativeai as genai

# Configure your Gemini API with the key
genai.configure(api_key="AIzaSyC8bPS9TWLaI6gvxLVdLvKkbuQjf2Qt6zk")


# Sum function to help check for wins
def sum(a, b, c):
    return a + b + c


# Function to print the board
def printBoard(xState, zState):
    zero = '❎' if xState[0] else ('🅾️' if zState[0] else 0)
    one = '❎' if xState[1] else ('🅾️' if zState[1] else 1)
    two = '❎' if xState[2] else ('🅾️' if zState[2] else 2)
    three = '❎' if xState[3] else ('🅾️' if zState[3] else 3)
    four = '❎' if xState[4] else ('🅾️' if zState[4] else 4)
    five = '❎' if xState[5] else ('🅾️' if zState[5] else 5)
    six = '❎' if xState[6] else ('🅾️' if zState[6] else 6)
    seven = '❎' if xState[7] else ('🅾️' if zState[7] else 7)
    eight = '❎' if xState[8] else ('🅾️' if zState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")


# Function to check if there's a winner
def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X Won the match")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O Won the match")
            return 0
    return -1


# Function to ask Gemini for its next move
def ask_gemini_move(xState, zState):
    board = ['❎' if xState[i] else ('🅾️' if zState[i] else str(i)) for i in range(9)]
    board_str = (
        f"{board[0]} | {board[1]} | {board[2]}\n"
        f"--|---|--\n"
        f"{board[3]} | {board[4]} | {board[5]}\n"
        f"--|---|--\n"
        f"{board[6]} | {board[7]} | {board[8]}"
    )
    prompt = f"""
You are playing as 'O' in Tic Tac Toe.
The board is shown below (0-8 are empty positions):

{board_str}

Based on the current board, what is the best number (0-8) to place your 'O'?
Only reply with the number of the position. Do not explain.
"""


    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    response = model.generate_content(prompt)
    move = response.text.strip()

    
    if move.isdigit() and int(move) in range(9):
        return int(move)
    else:
        print("Gemini returned an invalid move.")
        return None



if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while True:
        printBoard(xState, zState)

        if turn == 1:
            print("Your Turn (X)")
            value = int(input("Enter your move (0-8): "))
            xState[value] = 1
        else:
            print("Gemini's Turn (O)")
            move = ask_gemini_move(xState, zState)
            if move is not None:
                print(f"Gemini chose: {move}")
                zState[move] = 1
            else:
                print("Gemini returned an invalid move. Game stopped.")
                break

        cwin = checkWin(xState, zState)
        if cwin != -1:
            print("Match over")
            break

        if all(xState[i] == 1 or zState[i] == 1 for i in range(9)):
            print("Match is tie")
            break

        turn = 1 - turn