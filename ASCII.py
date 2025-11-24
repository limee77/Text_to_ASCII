from pyfiglet import Figlet
import zmq
f = Figlet(font='slant')

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("ASCII Service Listening on Port 5555")

    while True:
        # wait for request from client
        message = socket.recv_string()
        print(f"[ASCII] Service received: {message}")

        if message.startswith("ascii:"):
            user_text = message.split("ascii:", 1)[1]
            ascii_art = f.renderText(user_text)
            socket.send_string(ascii_art)
        else:
            socket.send_string("Error: Unknown command...")

if __name__ == "__main__":
    main()

