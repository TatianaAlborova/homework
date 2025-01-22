import asyncio

async def start_strongman(name, power, started_event):

    await started_event.wait()

    print(f"Силач {name} начал соревнования.")

    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {i} шар")

    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    competitors = [
        ("Pasha", 3),
        ("Denis", 4),
        ("Apollon", 5)
    ]

    started_event = asyncio.Event()
    tasks = [asyncio.create_task(start_strongman(name, power, started_event)) for name, power in competitors]

    started_event.set()

    for task in tasks:
        await task

asyncio.run(start_tournament())
