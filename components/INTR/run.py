import sys
import threading

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
    sys.stdout.write(to + "\n" + content + "\n")
    sys.stdout.flush()

log(f"INTR has started!")
with open(sys.argv[1], "r") as fr, open(sys.argv[1], "w") as fw:
    def t1():
        while True:
            sender, msg = read_message()

            fw.write(f"{sender} sent {repr(msg)}\n")
            fw.flush()

    threading.Thread(target=t1, daemon=True).start()

    while True:
        msg = fr.readline().strip()

        log("Got input", msg)
        send_message("RLAY", "CONS" + msg)
