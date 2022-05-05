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
    sys.stdout.flush()
    sys.stdout.write(content + "\n")
    sys.stdout.flush()


with open("/tmp/out.txt", "w") as f:
    while True:
        sender, data = read_message()

        log(f"writing {repr(data)}")
        f.write(data + "\n")
        f.flush()

        send_message(sender, "INTRdone")
