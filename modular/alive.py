################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import *

from Mix import DEVS, bot, ky, udB, user
from Mix.core.waktu import get_time, start_time

from .gcast import refresh_dialog

__modles__ = "Alive"
__help__ = """
 Help Command Alive

• Perintah : <code>{0}alive</code>
• Penjelasan : Alive.
"""


@ky.ubot("alive", sudo=True)
async def _(c: user, m):
    try:
        x = await c.get_inline_bot_results(bot.me.username, "alive")
        await m.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        await m.reply(error)


@ky.inline("^alive")
async def _(c, iq):
    pmper = None
    stutas = None
    start = datetime.now()
    await user.invoke(Ping(ping_id=0))
    pink = (datetime.now() - start).microseconds / 1000
    upnya = await get_time((time() - start_time))
    ape = await refresh_dialog("group")
    apa = await refresh_dialog("users")
    if user.me.id in DEVS:
        stutas = "<b>Author</b>"
    else:
        stutas = "<b>Connoisseur</b>"
    cekpr = udB.get_var(user.me.id, "PMPERMIT")
    if cekpr:
        pmper = "enable"
    else:
        pmper = "disable"
    txt = f"""
<b>Dan-Userbot</b>
    <b>status:</b> {stutas}
      <b>dc_id:</b> {user.me.dc_id}
      <b>ping_dc:</b> {str(pink).replace('.', ',')} ms
      <b>pmpermit:</b> {pmper}
      <b>peer_users:</b> {len(apa)}
      <b>peer_groups:</b> {len(ape)}
      <b>bot_uptime:</b> {upnya}
"""
    bo_ol = [[InlineKeyboardButton(text="Support", url="t.me/Disney_storeDan")]]
    cekpic = udB.get_var(user.me.id, "ALIVEPIC")
    if not cekpic:
        duar = [
            (
                InlineQueryResultArticle(
                    title="Alive Teks",
                    input_message_content=InputTextMessageContent(txt),
                    reply_markup=InlineKeyboardMarkup(bo_ol),
                )
            )
        ]

    else:
        filem = (
            InlineQueryResultVideo
            if cekpic.endswith(".mp4")
            else InlineQueryResultPhoto
        )
        url_ling = (
            {"video_url": cekpic, "thumb_url": cekpic}
            if cekpic.endswith(".mp4")
            else {"photo_url": cekpic}
        )
        duar = [
            filem(
                **url_ling,
                title="Alive Picture",
                caption=txt,
                reply_markup=InlineKeyboardMarkup(bo_ol),
            )
        ]
    await c.answer_inline_query(iq.id, cache_time=0, results=duar)
