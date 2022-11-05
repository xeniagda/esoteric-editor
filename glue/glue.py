import subprocess
import sys
import os
import signal
import asyncio
import asyncio_channel as ch
import traceback

component_channels = {}

RESET = "\033[0m"
LOG_COLOR = "\033[38;5;69m"
MSG_COLOR = "\033[38;5;195m"
ERROR_COLOR = "\033[38;5;1m"
TITLE = "\033[1m"

def is_win32():
    if os.name.lower() == "nt":
        return True
    return False

async def process_stdout(proc, name):
    try:
        while True:
            receiver = ""
            while receiver == "":
                receiver = await proc.stdout.readexactly(5)
            receiver = receiver[:-1]
            data = (await proc.stdout.readuntil(b"\n"))[:-1]

            print(f"{MSG_COLOR}{name.decode('utf-8')}->{receiver.decode('utf-8')}{RESET} {repr(data)}")
            await component_channels[receiver].put((name, data))
    except asyncio.CancelledError as e:
        print(f"{ERROR_COLOR}CANCELLED STDOUT PROCESSOR FOR [{name}]{RESET}")
        return

async def send_stdin(proc, ch, name):
    try:
        async for (sender, data) in ch:
            proc.stdin.write(sender + b"\n" + data + b"\n")
            await proc.stdin.drain()
    except asyncio.CancelledError as e:
        print(f"{ERROR_COLOR}CANCELLED STDIN PROCESSOR FOR [{name}]{RESET}")
        return

async def pretty_stderr(proc, name):
    try:
        while True:
            line = await proc.stderr.readline()
            if line == b'':
                print(f"{LOG_COLOR}CLOSED [{name}]{RESET}")
                break
            print(f"{LOG_COLOR}LOG [{name}]{RESET} {line.decode('utf-8').strip()}")
    except asyncio.CancelledError as e:
        print(f"{ERROR_COLOR}CANCELLED LOG FOR [{name}]{RESET}")
        return


async def start_component(cmd, name):
    is_win = is_win32()

    print(f"{TITLE}Starting {name}{RESET}")
    name_b = name.encode("utf-8")

    msg_channel = ch.create_channel(100)
    component_channels[name_b] = msg_channel

    proc = None

    if is_win:
        print(f"{LOG_COLOR}LOG [{name}]{RESET} => Win32 platform detected, using: CREATE_NEW_PROCESS_GROUP flag...={name}")
        proc = await asyncio.create_subprocess_shell(
            cmd,
            cwd=os.path.join("components", name), # Undocumented!
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
        )
    else:
        proc = await asyncio.create_subprocess_shell(
            cmd,
            cwd=os.path.join("components", name), # Undocumented!
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

    stdout_processor = asyncio.create_task(process_stdout(proc, name_b))
    stdin_processor = asyncio.create_task(send_stdin(proc, msg_channel, name))
    stderr_logger = asyncio.create_task(pretty_stderr(proc, name))

    await proc.wait()
    if proc.returncode == 0:
        print(f"{TITLE}{name} exited{RESET}")
    else:
        print(f"{TITLE}{ERROR_COLOR}{name} exited with status code {proc.returncode}{RESET}")

    stdout_processor.cancel()
    stdin_processor.cancel()
    stderr_logger.cancel()

async def main():
    is_win = is_win32()
    tty = "dev/ttys005"
    py_cmd = "python3"

    if not is_win:
        os.setpgrp() # create new process group, become its leader
    
    try:
        if is_win:
            print("Win32 platform detected!!!")
            tty = "/dev/cons1"
            py_cmd = "python"

        await asyncio.gather(
            start_component(f"{py_cmd} run.py {tty}", "INTR"),
            start_component(f"{py_cmd} run.py", "RLAY"),
            start_component(f"{py_cmd} run.py", "CONS"),
        )
    except:
        traceback.print_exc()
    finally:
        print("bye")
        
        if not is_win:
            os.killpg(0, signal.SIGKILL) # kill all processes in my group
            return

        os.kill(0, signal.SIGTERM)

if __name__ == "__main__":
    asyncio.run(main())
