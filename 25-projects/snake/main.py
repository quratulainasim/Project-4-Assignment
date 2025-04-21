import streamlit as st
import numpy as np
import time
import random


GRID_SIZE = 20
DELAY = 0.4  # seconds between moves

def init_game():
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
    st.session_state.direction = "RIGHT"
    st.session_state.game_over = False
    st.session_state.score = 0

def move_snake():
    if st.session_state.game_over:
        return
    
    head_x, head_y = st.session_state.snake[-1]
    if st.session_state.direction == "UP":
        head_x -= 1
    elif st.session_state.direction == "DOWN":
        head_x += 1
    elif st.session_state.direction == "LEFT":
        head_y -= 1
    elif st.session_state.direction == "RIGHT":
        head_y += 1

    new_head = (head_x, head_y)

    if new_head in st.session_state.snake or not (0 <= head_x < GRID_SIZE and 0 <= head_y < GRID_SIZE):
        st.session_state.game_over = True
        return

    st.session_state.snake.append(new_head)

    if new_head == st.session_state.food:
        st.session_state.food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        st.session_state.score += 1
    else:
        st.session_state.snake.pop(0)

def draw_grid():
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    for x, y in st.session_state.snake:
        grid[x, y] = 1
    fx, fy = st.session_state.food
    grid[fx, fy] = 2

    st.markdown(f"### Score: {st.session_state.score}")
    for row in grid:
        st.text(" ".join(["🟩" if cell == 1 else "🍎" if cell == 2 else "⬜" for cell in row]))

st.set_page_config(layout="wide")
st.title("🐍 Mini Snake Game")

if "snake" not in st.session_state:
    init_game()
if "direction_changed" not in st.session_state:
    st.session_state.direction_changed = False

col1, col2 = st.columns([4, 1])

with col1:
    draw_grid()

with col2:
    st.write("### Controls")
    up = st.button("⬆️")
    left_col, right_col = st.columns(2)
    with left_col:
        left = st.button("⬅️")
    with right_col:
        right = st.button("➡️")
    down = st.button("⬇️")
    st.markdown("---")
    if st.button("🔁 Restart Game"):
        init_game()
        st.rerun()

if not st.session_state.get("direction_changed", False):
    if up and st.session_state.direction != "DOWN":
        st.session_state.direction = "UP"
        st.session_state.direction_changed = True
    elif down and st.session_state.direction != "UP":
        st.session_state.direction = "DOWN"
        st.session_state.direction_changed = True
    elif left and st.session_state.direction != "RIGHT":
        st.session_state.direction = "LEFT"
        st.session_state.direction_changed = True
    elif right and st.session_state.direction != "LEFT":
        st.session_state.direction = "RIGHT"
        st.session_state.direction_changed = True


if not st.session_state.game_over:
    time.sleep(DELAY)
    move_snake()
    st.session_state.direction_changed = False
    st.rerun()
else:
    st.error(f"Game Over! Your Score: {st.session_state.score}. Click 'Restart Game' to play again.")
