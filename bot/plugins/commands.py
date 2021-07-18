#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"{file_name} \n \n <b>പുതിയ സിനിമകൾ ഇറങ്ങുമ്പോൾ തന്നെ ലഭിക്കാൻ ചാനെലിൽ ജോയിൻ ചെയ്യൂ.. \n ⊰᯽⊱┈──╌❊╌──┈⊰᯽⊱<b> \n @NEW_MLM_HD_MOVES \n @mlm_movies_update<b>" ,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🔰 UPDATE CHANNEL 🔰', url="https://t.me/mlm_movies_update"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('🔰 MOVIE REQESTING GROUP 🔰', url='https://t.me/NEW_MLM_HD_MOVES'),
    ],[
        InlineKeyboardButton('🔰 UPDATE CHANNEL 🔰', url='https://t.me/mlm_movies_update'),
    ],[
        InlineKeyboardButton('OWNER 👨‍✈️', url='https://t.me/mrplantozz_bot'),
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ],[
       InlineKeyboardButton('CLOSE 🔒', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('HOME ⚓', callback_data='start'),
        InlineKeyboardButton('ABOUT ⭕', callback_data='about')
    ],[
        InlineKeyboardButton('CLOSE 🔒', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚓', callback_data='start'),
        InlineKeyboardButton('Close 🔒', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
