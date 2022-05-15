import aiohttp
# import asyncio

async def pars_www():
    link = 'https://api.imsr.su/main/get_tasks'
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as res:
            return await res.json()

# asyncio.run(pars_www())
            