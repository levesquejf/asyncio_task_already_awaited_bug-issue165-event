import asyncio


async def sleep(timeout, event):
    print(f"Sleep for {timeout}", flush=True)
    try:
        print("Create Task", flush=True)
        t = asyncio.ensure_future(event.wait())
        await asyncio.wait([t], timeout=timeout)
    except asyncio.TimeoutError:
        pass

    print("Cancel Task", flush=True)
    t.cancel()
    try:
        print("Will await", flush=True)
        await t
    except asyncio.CancelledError:
        pass


async def run():
    event = asyncio.Event()
    await sleep(1, event)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


if __name__ == "__main__":
    main()
