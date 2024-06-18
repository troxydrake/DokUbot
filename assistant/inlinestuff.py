# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


from telethon import Button
from telethon.tl.types import InputWebDocument as wb

from . import *

SUP_BUTTONS = [
    [
        Button.url("• Repo •", url="https://github.com/naya1503/Naya-Userbot"),
        Button.url("• Support •", url="t.me/Top_Mutualan_Indonesia"),
    ],
]

ofox = "https://telegra.ph/file/b9781dee8b753b7c66000.jpg"
gugirl = "https://telegra.ph/file/2bdcf315cf65414cb07dd.jpg"
aypic = "https://telegra.ph/file/c0d6de3e5501c55222855.jpg"

apis = [
    "QUl6YVN5QXlEQnNZM1dSdEI1WVBDNmFCX3c4SkF5NlpkWE5jNkZV",
    "QUl6YVN5QkYwenhMbFlsUE1wOXh3TVFxVktDUVJxOERnZHJMWHNn",
    "QUl6YVN5RGRPS253blB3VklRX2xiSDVzWUU0Rm9YakFLSVFWMERR",
]


@in_pattern("repo", owner=True)
async def repo(e):
    res = [
        await e.builder.article(
            title="Bee Userbot",
            description="Userbot | Telethon",
            thumb=wb(aypic, 0, "image/jpeg", []),
            text="**◈ ʙᴇᴇ ꭙ ᴜꜱᴇʀʙᴏᴛ​ ◈**",
            buttons=SUP_BUTTONS,
        ),
    ]
    await e.answer(res, switch_pm="Bee Userbot", switch_pm_param="start")
