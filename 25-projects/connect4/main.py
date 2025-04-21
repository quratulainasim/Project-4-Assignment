import streamlit as st
import numpy as np

def create_board():
    return np.zeros((6, 7), dtype=int)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for r in range(5, -1, -1):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    for c in range(7 - 3):
        for r in range(6):
            if all(board[r][c + i] == piece for i in range(4)):
                return True
    for c in range(7):
        for r in range(6 - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True
    for c in range(7 - 3):
        for r in range(6 - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True
    for c in range(7 - 3):
        for r in range(3, 6):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True
    return False

def render_cell(value):
    return "⚪" if value == 0 else "🔴" if value == 1 else "🟡"

if "board" not in st.session_state:
    st.session_state.board = create_board()
    st.session_state.turn = 0
    st.session_state.game_over = False

st.set_page_config("Connect Four")
st.title("🔵 Connect Four - Button Board Edition")


st.subheader("Click a column to drop your piece")
col_buttons = st.columns(7)
for i, col in enumerate(col_buttons):
    if col.button(f"⬇️", key=f"btn_col_{i}") and not st.session_state.game_over:
        if is_valid_location(st.session_state.board, i):
            row = get_next_open_row(st.session_state.board, i)
            drop_piece(st.session_state.board, row, i, st.session_state.turn + 1)

            if winning_move(st.session_state.board, st.session_state.turn + 1):
                st.session_state.game_over = True
                st.success(f"🎉 Player {st.session_state.turn + 1} wins!")

            elif np.all(st.session_state.board != 0):
                st.session_state.game_over = True
                st.warning("🤝 It's a draw!")

            st.session_state.turn = (st.session_state.turn + 1) % 2
        else:
            st.warning(f"🚫 Column {i} is full.")

st.write("### Game Board")
flipped = np.flip(st.session_state.board, 0)
board_rows = flipped.tolist()
for row in board_rows:
    cols = st.columns(7)
    for i, cell in enumerate(row):
        cols[i].markdown(f"<div style='font-size: 30px; text-align: center'>{render_cell(cell)}</div>", unsafe_allow_html=True)

if st.session_state.game_over:
    if st.button("🔄 Restart Game"):
        st.session_state.board = create_board()
        st.session_state.turn = 0
        st.session_state.game_over = False
        st.rerun()

