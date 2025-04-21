import streamlit as st
import numpy as np
import time
from PIL import Image, ImageDraw

# Smaller Game Constants
WIDTH, HEIGHT = 200, 150
BALL_RADIUS = 4
PADDLE_WIDTH, PADDLE_HEIGHT = 3, 30
PADDLE_SPEED = 8
BALL_SPEED = 2

def create_game_frame(ball_pos, paddle1_pos, paddle2_pos):
    image = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    
    for y in range(0, HEIGHT, 10):
        draw.line([(WIDTH//2, y), (WIDTH//2, y+5)], fill=(255, 255, 255), width=1)
    

    draw.rectangle([5, paddle1_pos, 5+PADDLE_WIDTH, paddle1_pos+PADDLE_HEIGHT], fill=(255, 255, 255))
    draw.rectangle([WIDTH-10, paddle2_pos, WIDTH-10+PADDLE_WIDTH, paddle2_pos+PADDLE_HEIGHT], fill=(255, 255, 255))
    
    # Draw ball
    draw.ellipse([ball_pos[0]-BALL_RADIUS, ball_pos[1]-BALL_RADIUS, 
                 ball_pos[0]+BALL_RADIUS, ball_pos[1]+BALL_RADIUS], 
                 fill=(255, 255, 255))
    
    return image

def initialize_game():
    if 'ball_pos' not in st.session_state:
        st.session_state.ball_pos = [WIDTH//2, HEIGHT//2]
        st.session_state.ball_dx = BALL_SPEED
        st.session_state.ball_dy = BALL_SPEED
        st.session_state.paddle1_pos = HEIGHT//2 - PADDLE_HEIGHT//2
        st.session_state.paddle2_pos = HEIGHT//2 - PADDLE_HEIGHT//2
        st.session_state.score1 = 0
        st.session_state.score2 = 0
        st.session_state.game_active = False

def update_game_state():
    if not st.session_state.game_active:
        return
 

    st.session_state.ball_pos[0] += st.session_state.ball_dx
    st.session_state.ball_pos[1] += st.session_state.ball_dy
    
   
    if st.session_state.ball_pos[1] <= BALL_RADIUS or st.session_state.ball_pos[1] >= HEIGHT - BALL_RADIUS:
        st.session_state.ball_dy *= -1
    
    paddle1 = [5, st.session_state.paddle1_pos, 5+PADDLE_WIDTH, st.session_state.paddle1_pos+PADDLE_HEIGHT]
    paddle2 = [WIDTH-10, st.session_state.paddle2_pos, WIDTH-10+PADDLE_WIDTH, st.session_state.paddle2_pos+PADDLE_HEIGHT]
    
   
    if (st.session_state.ball_pos[0] - BALL_RADIUS <= paddle1[2] and 
        st.session_state.ball_pos[0] + BALL_RADIUS >= paddle1[0] and
        st.session_state.ball_pos[1] + BALL_RADIUS >= paddle1[1] and
        st.session_state.ball_pos[1] - BALL_RADIUS <= paddle1[3]):
        st.session_state.ball_dx *= -1
        st.session_state.ball_pos[0] = paddle1[2] + BALL_RADIUS


    if (st.session_state.ball_pos[0] + BALL_RADIUS >= paddle2[0] and 
        st.session_state.ball_pos[0] - BALL_RADIUS <= paddle2[2] and
        st.session_state.ball_pos[1] + BALL_RADIUS >= paddle2[1] and
        st.session_state.ball_pos[1] - BALL_RADIUS <= paddle2[3]):
        st.session_state.ball_dx *= -1
        st.session_state.ball_pos[0] = paddle2[0] - BALL_RADIUS

   
    if st.session_state.ball_pos[0] < 0:
        st.session_state.score2 += 1
        st.session_state.ball_pos = [WIDTH//2, HEIGHT//2]
        st.session_state.ball_dx = BALL_SPEED
        st.session_state.ball_dy = BALL_SPEED
    elif st.session_state.ball_pos[0] > WIDTH:
        st.session_state.score1 += 1
        st.session_state.ball_pos = [WIDTH//2, HEIGHT//2]
        st.session_state.ball_dx = -BALL_SPEED
        st.session_state.ball_dy = BALL_SPEED

st.set_page_config(layout="wide")
st.title("🎮 Mini Pong - Tiny Ball & Paddles Edition")
st.write("Use the buttons to move paddles. Click Start to play!")

initialize_game()


st.markdown("### Paddle Controls")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("⬆️ P1 Up"):
        st.session_state.paddle1_pos = max(0, st.session_state.paddle1_pos - PADDLE_SPEED)
with col2:
    if st.button("⬇️ P1 Down"):
        st.session_state.paddle1_pos = min(HEIGHT - PADDLE_HEIGHT, st.session_state.paddle1_pos + PADDLE_SPEED)
with col3:
    if st.button("⬆️ P2 Up"):
        st.session_state.paddle2_pos = max(0, st.session_state.paddle2_pos - PADDLE_SPEED)
with col4:
    if st.button("⬇️ P2 Down"):
        st.session_state.paddle2_pos = min(HEIGHT - PADDLE_HEIGHT, st.session_state.paddle2_pos + PADDLE_SPEED)


col_start, col_reset = st.columns(2)
with col_start:
    if st.button("▶️ Start / Pause"):
        st.session_state.game_active = not st.session_state.game_active
with col_reset:
    if st.button("🔁 Reset"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()


st.markdown(f"### 🏆 Score")
st.write(f"Player 1: {st.session_state.score1} | Player 2: {st.session_state.score2}")

update_game_state()
frame = create_game_frame(
    st.session_state.ball_pos,
    st.session_state.paddle1_pos,
    st.session_state.paddle2_pos
)
st.image(frame, use_container_width=True)

if st.session_state.game_active:
    time.sleep(0.07)
    st.rerun()
