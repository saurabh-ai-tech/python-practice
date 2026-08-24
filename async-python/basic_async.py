# 1. Solution
# import asyncio

# async def hello():
#     print("Hello from async function")


# asyncio.run(hello())


# 2. Solution
# import asyncio
# async def wait():
#     print("Start")
#     await asyncio.sleep(5)
#     print("Finished")


# asyncio.run(wait())

# 3. Solution 

import asyncio

async def get_number():
    await asyncio.sleep(1)
    return 10

print(asyncio.run(get_number()))

