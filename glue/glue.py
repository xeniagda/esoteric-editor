import os
import signal
import asyncio
import asyncio_channel as ch
import traceback

component_channels = {}

async def process_stdout(proc, name):
    while True:
        receiver = ""
        while receiver == "":
            receiver = await proc.stdout.readexactly(5)
        receiver = receiver[:-1]
        data = (await proc.stdout.readuntil(b"\n"))[:-1]

        print(f"{name} is sending {repr(data)} to {receiver}")
        await component_channels[receiver].put((name, data))

async def send_stdin(proc, ch):
    async for (sender, data) in ch:
        proc.stdin.write(sender + b"\n" + data + b"\n")
        await proc.stdin.drain()

async def start_component(cmd, name):
    name_b = name.encode("utf-8")

    msg_channel = ch.create_channel()
    component_channels[name_b] = msg_channel

    proc = await asyncio.create_subprocess_shell(
        cmd,
        cwd=os.path.join("components", name), # Undocumented!
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
    )

    await asyncio.gather(
        process_stdout(proc, name_b),
        send_stdin(proc, msg_channel),
    )

async def main():
    os.setpgrp() # create new process group, become its leader

    try:
        await asyncio.gather(
            start_component("python3 run.py /dev/ttys003 | tee /dev/ttys002", "INTR"),
            start_component("python3 run.py", "RLAY"),
            start_component("python3 run.py", "CONS"),
        )
    except Exception as e:
        traceback.print_exc()
    finally:
        print("bye")
        os.killpg(0, signal.SIGKILL) # kill all processes in my group

if __name__ == "__main__":
    asyncio.run(main())
