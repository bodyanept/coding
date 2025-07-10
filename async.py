import time
def oneSec():
    for i in range(0,10):
        print('hello')
        time.sleep(1)


oneSec()


import asyncio
async def oneSec(name, delay):
    await asyncio.sleep(delay)
    print(f'salam, {name}, posle {delay} seconds')


async def main():
    await asyncio.gather(
        oneSec('andruha', 1),
        oneSec('echpochmak', 4),
        oneSec('gleb', 2)
        )
        
        
asyncio.run(main())
