import sys

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
    sys.stdout.flush()
    sys.stdout.write(content + "\n")
    sys.stdout.flush()


with open("/tmp/out.txt", "w") as f:
    while True:
        sender, data = read_message()

        print(f"writing {data}", file=sys.stderr)
        f.write(data + "\n")
        f.flush()

        send_message(sender, "INTRdone")
