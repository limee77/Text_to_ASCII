import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

text = input("Enter text to convert: ")

socket.send_string(f"ascii:{text}")
ascii_art = socket.recv_string()

print(ascii_art)
