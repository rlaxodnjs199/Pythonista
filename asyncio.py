import asyncio

async def py35_coro():
    await stuff()

# coroutine
def reader():
    for i in range(4):
        yield '<< %s' % i

# subcoroutine
def reader_wrapper(g):
    yield from g

wrap = reader_wrapper(reader())
for i in wrap:
    print(i)