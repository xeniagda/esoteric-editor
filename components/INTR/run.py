import sys
import threading

def read_message():
    sender = ""
    while len(sender) < 4:
        sender += sys.stdin.read(1)
    sys.stdin.read(1) # newline
    data = ""
    while True:
        ch = sys.stdin.read(1)
        if ch == "\n":
            break
        data += ch

    print(f"got {repr(data)} from {repr(sender)}", file=sys.stderr)

    return sender, data

def send_message(to, content):
    print(f"sending {repr(content)} to {repr(to)}", file=sys.stderr)
    sys.stdout.write(to + "\n")
    sys.stdout.write(content + "\n")
    sys.stdout.flush()

print(f"INTR has started!", file=sys.stderr)
with open(sys.argv[1], "r") as fr, open(sys.argv[1], "w") as fw:
    def t1():
        while True:
            msg = fr.readline()

            send_message("RLAY", "CONS" + msg)

    threading.Thread(target=t1, daemon=True).start()

    while True:
        sender, msg = read_message()

        fw.write(f"{sender} sent {repr(msg)}\n")
        fw.flush()
