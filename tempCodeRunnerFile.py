#!/usr/bin/env python3
import socket
import time

HOST = '127.0.0.1'
PORT = 30002

def send_urscript(script: str, host=HOST, port=PORT, wait=1.0):
    """
    Connect to the URScript command port, send the script, and wait.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        # URScript is plain text, newline-separated
        s.sendall(script.encode('utf8'))
        # give the robot time to start executing
        time.sleep(wait)

if __name__ == '__main__':
    # A little URScript program that:
    #  1. Moves to a safe “pen‐up” pose via movej
    #  2. Moves (pen‐down) in straight lines to sketch a “7”
    urscript = """
def draw_seven():
  # 1) Move to a safe start pose (all joint angles in radians)
  movej([0.0, -1.57, 0.0, -1.57, 0.0, 0.0], a=1.2, v=0.25)

  # 2) Draw the top horizontal: from (0.2,0.2,0.2) to (0.8,0.2,0.2)
  movel(p[0.2, 0.2, 0.2, 0, 3.14, 0], a=0.5, v=0.1)
  movel(p[0.8, 0.2, 0.2, 0, 3.14, 0], a=0.5, v=0.1)

  # 3) Draw the diagonal down‐left to (0.2, -0.2, 0.2)
  movel(p[0.2, -0.2, 0.2, 0, 3.14, 0], a=0.5, v=0.1)
end

draw_seven()
"""
    send_urscript(urscript)