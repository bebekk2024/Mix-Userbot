import asyncio
import importlib
import sys
from contextlib import closing, suppress

from pyrogram import *
from pyrogram.errors import *
from uvloop import install

from assistant import BOT_PLUGINS
from Mix import *
from modular import USER_MOD

lool = asyncio.get_event_loop()


async def start_user():
    LOGGER.info(f"Starting Telegram User Client...")
    try:
        await user.start()
        LOGGER.info(f"Importing All Modules...")
        for modul in USER_MOD:
            imported_module = importlib.import_module(f"modular." + modul)
            if hasattr(imported_module, "modles") and imported_module.modles:
                imported_module.modles = imported_module.modles
                if hasattr(imported_module, "help") and imported_module.help:
                    CMD_HELP[imported_module.modles.replace(" ", "_").lower()] = (
                        imported_module
                    )
    except (SessionExpired, ApiIdInvalid, UserDeactivatedBan):
        LOGGER.info("Check your session or api id!!")
        sys.exit(1)


async def start_bot():
    LOGGER.info(f"Starting Telegram Bot Client...")
    if bot_token is None:
        await autobot()
    try:
        await bot.start()
        for plus in BOT_PLUGINS:
            imported_module = importlib.import_module("assistant." + plus)
            importlib.reload(imported_module)
    except (AccessTokenExpired, SessionRevoked, AccessTokenInvalid):
        LOGGER.info("Token Expired.")
        sys.exit(1)


async def starter():
    LOGGER.info(f"Check Updater...")
    await cek_updater()
    LOGGER.info(f"Updater Finished...")
    LOGGER.info(f"Connecting to {ndB.name}...")
    if ndB.ping():
        LOGGER.info(f"Connected to {ndB.name} Successfully!")
    await start_user()
    if user.is_connected:
        await start_bot()
    await asyncio.gather(refresh_cache(), check_logger())
    LOGGER.info("Successfully Started Userbot.")
    await asyncio.gather(getFinish(), isFinish(), idle())


if name == "main":
    install()
    with closing(lool):
        with suppress(asyncio.exceptions.CancelledError):
            lool.run_until_complete(starter())
        lool.run_until_complete(asyncio.sleep(3.0))
