from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("start"))
async def start_msg(client, message):
	await message.reply_text(
		f"درود بر {message.from_user.mention} .\n من بات دانلودر NLM هستم و میتونم فایل مورد علاقتو از یوتیوب دانلود کنم,",
		reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🛠 کمک", callback_data=f"کمک"),
					InlineKeyboardButton("🧰 درباره ما", callback_data=f"درباره ما")
				]]
			),
		quote=True)

@Client.on_callback_query()
async def cb_handler(client, update):
	cb_data = update.data
	
	if "کمک" in cb_data:
		await update.message.edit_text("فقط کافیه لینک مورد علاقتو به فرم روروبر برام ارسال کنی و کنارش یکی از کلمات(Audio/Video) رو بذاری تا بتونم بفهمم فیلم اون رو میخوای یا اهنگشو.\nبرای مثال :\n`https://www.youtube.com/watch?v=Fifk9DfJo video",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🧰 درباره ما", callback_data=f"درباره ما"),
					InlineKeyboardButton("🔙 برشگت", callback_data=f"برگشت")
				]]
			))
	elif "درباره ما" in cb_data:
		await update.message.edit_text("چنل اصلی ما : @NLM_News \nبقیه بات ها :@The_Aryana_PY\nسازنده : @aryana_gha",
			reply_markup=InlineKeyboardMarkup(
				[[
                                        InlineKeyboardButton("🛠 کمک", callback_data=f"کمک"),
					InlineKeyboardButton("🔙 برشگت", callback_data=f"برگشت")
				]]
			))
	elif "برکشت" in cb_data:
		await update.message.edit_text(f"سلامی دوباره بر {update.from_user.mention}, برای دریافت راهنمایی گزینه کمک رو بزنید  ",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🛠 کمک", callback_data=f"کمک"),
					InlineKeyboardButton("🧰 درباره ما", callback_data=f"درباره ما")
				]]
			))
