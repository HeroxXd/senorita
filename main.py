import asyncio
from pytgcalls import idle
from senorita import call_py, bot

async def mulai_bot():
    print("[SENORITA]: STARTING BOT CLIENT")
    await bot.start()
    print("[SENORITA]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[SENORITA]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())
