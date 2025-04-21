import streamlit as st
import numpy as np
import random

# Grid size
grid_height = 20
grid_width = 10

def init_game():
    st.session_state.grid = np.zeros((grid_height, grid_width), dtype=int)
    st.session_state.piece = get_random_piece()
    st.session_state.piece_position = [0, grid_width // 2 - 1]
    st.session_state.game_over = False
    st.session_state.score = 0

def get_random_piece():
    pieces = [
        np.array([[1, 1, 1, 1]]),   # I
        np.array([[1, 1], [1, 1]]),  # O
        np.array([[0, 1, 0], [1, 1, 1]]),  # T
        np.array([[1, 1, 0], [0, 1, 1]]),  # S
        np.array([[0, 1, 1], [1, 1, 0]]),  # Z
        np.array([[1, 0, 0], [1, 1, 1]]),  # L
        np.array([[0, 0, 1], [1, 1, 1]])   # J
    ]
    return random.choice(pieces)

def render_grid():
    temp_grid = st.session_state.grid.copy()
    piece = st.session_state.piece
    x, y = st.session_state.piece_position
    for i in range(piece.shape[0]):
        for j in range(piece.shape[1]):
            if piece[i, j]:
                if 0 <= x + i < grid_height and 0 <= y + j < grid_width:
                    temp_grid[x + i, y + j] = 2
    return temp_grid

def show_grid(grid):
    emojis = {0: "⬛", 1: "🟥", 2: "🟨"}
    lines = []
    for row in grid:
        line = "".join(emojis[cell] for cell in row)
        lines.append(line)
    st.markdown("<br>".join(lines), unsafe_allow_html=True)

def is_valid_position(piece, pos):
    x, y = pos
    for i in range(piece.shape[0]):
        for j in range(piece.shape[1]):
            if piece[i, j]:
                xi, yj = x + i, y + j
                if xi >= grid_height or yj < 0 or yj >= grid_width:
                    return False
                if xi >= 0 and st.session_state.grid[xi, yj] == 1:
                    return False
    return True

def place_piece():
    piece = st.session_state.piece
    x, y = st.session_state.piece_position
    for i in range(piece.shape[0]):
        for j in range(piece.shape[1]):
            if piece[i, j]:
                st.session_state.grid[x + i, y + j] = 1
    clear_full_rows()
    st.session_state.piece = get_random_piece()
    st.session_state.piece_position = [0, grid_width // 2 - 1]
    if not is_valid_position(st.session_state.piece, st.session_state.piece_position):
        st.session_state.game_over = True

def clear_full_rows():
    grid = st.session_state.grid
    new_grid = [row for row in grid if not all(cell == 1 for cell in row)]
    cleared = grid_height - len(new_grid)
    st.session_state.score += cleared
    while len(new_grid) < grid_height:
        new_grid.insert(0, np.zeros(grid_width, dtype=int))
    st.session_state.grid = np.array(new_grid)

def move(dx, dy):
    if st.session_state.game_over:
        return
    new_pos = [st.session_state.piece_position[0] + dx,
               st.session_state.piece_position[1] + dy]
    if is_valid_position(st.session_state.piece, new_pos):
        st.session_state.piece_position = new_pos
    elif dx == 1:  # trying to move down but failed, so place
        place_piece()

def rotate():
    if st.session_state.game_over:
        return
    rotated = np.rot90(st.session_state.piece, -1)
    if is_valid_position(rotated, st.session_state.piece_position):
        st.session_state.piece = rotated

st.set_page_config("Tetris", layout="centered")
st.title("🧱 Streamlit Tetris")
if "grid" not in st.session_state:
    init_game()

st.markdown(f"**Score:** {st.session_state.score}")
show_grid(render_grid())

# Buttons
cols = st.columns(5)
if cols[0].button("⬅"):
    move(0, -1)
if cols[1].button("➡"):
    move(0, 1)
if cols[2].button("🔁"):
    rotate()
if cols[3].button("⬇"):
    move(1, 0)
if cols[4].button("Tick ⏬"):
    move(1, 0)

if st.session_state.game_over:
    st.error("💀 Game Over!")
    if st.button("🔄 Restart"):
        init_game()
        st.rerun()
