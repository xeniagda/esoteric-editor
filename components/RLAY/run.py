import sys

def log(*args):
    print(*args, file=sys.stderr, flush=True)

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

    return sender, data

def send_message(to, content):
    sys.stdout.write(to + "\n")
    sys.stdout.write(content + "\n")
    sys.stdout.flush()


while True:
    sender, data = read_message()
    to = data[:4]

    msg = "Relaying: " + data[4:]

    log("Relaying", repr(msg))

    send_message(to, msg)
