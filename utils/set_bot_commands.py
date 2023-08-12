from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "start the bot"),
            types.BotCommand("help", "how to use this bot"),
            types.BotCommand("info","info about this bot")

        ]
    )
