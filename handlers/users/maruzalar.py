from aiogram import types
from keyboards.default.maruzalar import bbc

from loader import dp, bot


# Echo bot
@dp.message_handler(text="🌸MARUZALAR🌸")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/salom9899/16", caption="Siz ,,MARUZALAR'' bo'limidasiz\nMarhamat o'zingizga kerakli mavzuni tanlang\n\n\n\n"
"⚠️Ushbu botni yaqinlaringizga ham ulashishni unutmang\nSizga ham shunday bot kerak bo'lsa admin bilan bog'laning👇\n\n"
"👤Admin bilan bog'lanish:@Tojaliyev_1817",reply_markup=bbc)

@dp.message_handler(text="Internetda hizbutlarni eshitganiz bu ilm emas")
async def bot_echo(message: types.Message):
    await message.reply_video(video="https://t.me/salom9899/19", caption="🎙 Shukurulloh Domla\n\nInternetda hizbutlarni eshitganiz bu ilm emas")

@dp.message_handler(text="Alloh eng yomon ko'rgan narsa")
async def bot_echo(message: types.Message):
    await message.reply_video(video="https://t.me/salom9899/18", caption="🎙 Shayx Muhammad Sodiq Muhammad Yusuf\n\nAlloh eng yomon ko'rgan narsa")

@dp.message_handler(text="Qachon qiynalganni g'amini yeymiz")
async def bot_echo(message: types.Message):
    await message.reply_video(video="https://t.me/salom9899/21", caption="🎙 Shukurulloh Domla\n\nQachon qiynalganni g'amini yeymiz")

@dp.message_handler(text="Bolalaringizni tergab turing yoki tergasak jirillamang")
async def bot_echo(message: types.Message):
    await message.reply_video(video="https://t.me/salom9899/22", caption="🎙 Shukurulloh Domla\n\nBolalaringizni tergab turing yoki tergasak jirillamang")

@dp.message_handler(text="Qumor o'yneydiganlar haqida")
async def bot_echo(message: types.Message):
    await message.reply_video(video="https://t.me/salom9899/23", caption="🎙 Shukurulloh Domla\n\nQumor o'yneydiganlar haqida☝")

@dp.message_handler(text="Ichimlik suvi 2 kun hojatxonaga oqdi😱")
async def bot_echo(message: types.Message):
    await message.reply_video(video="https://t.me/salom9899/24", caption="🎙 Shukurulloh Domla\n\nIchimlik suvi 2 kun hojatxonaga oqdi😱")

@dp.message_handler(text="Hiyonatlarning eng yomonlaridan biri☝️")
async def bot_echo(message: types.Message):
    await message.reply_video(video="https://t.me/salom9899/25", caption="🎙 Shukurulloh Domla\n\nHiyonatlarning eng yomonlaridan biri☝️")

@dp.message_handler(text="Isbot dalilingiz yo'qmi o'zingizni qiynamang")
async def bot_echo(message: types.Message):
    await message.reply_video(video="https://t.me/salom9899/26", caption="🎙 Shukurulloh Domla\n\nIsbot dalilingiz yo'qmi o'zingizni qiynamang")

@dp.message_handler(text="Ota Onangga sharoit qilib ber")
async def bot_echo(message: types.Message):
    await message.reply_video(video="https://t.me/salom9899/29", caption="🎙 Shukurulloh Domla\n\nOta Onangga sharoit qilib ber")

@dp.message_handler(text="Kim taxorat bilan uxlasa")
async def bot_echo(message: types.Message):
    await message.reply_video(video="https://t.me/salom9899/30", caption="🎙 Shukurulloh Domla\n\nKim taxorat bilan uxlasa")

@dp.message_handler(text="Kimni qarasez dardi 2-xotin")
async def bot_echo(message:types.Message):
    await message.reply_video(video="https://t.me/salom9899/31", caption="🎙 Shukurulloh Domla\n\nKimni qarasez dardi 2-xotin")

@dp.message_handler(text="Ota Onaga baqirish haqida😱")
async def bot_echo(message:types.Message):
    await message.reply_video(video="https://t.me/salom9899/32", caption="🎙 Shukurulloh Domla\n\nOta Onaga baqirish haqida😱")

@dp.message_handler(text="Oiladagi infoqlarda ham mo'tadil bo'ling isrof qilmang")
async def bot_echo(message:types.Message):
    await message.reply_video(video="https://t.me/salom9899/44", caption="🎙 Shukurulloh Domla\n\nOiladagi infoqlarda ham no'tadil bo'ling isrof qilmang")

@dp.message_handler(text="Yomonlikdan qaytarishda biror shaxs yoki hududga nisbat berilmaydi")
async def bot_echo(message:types.Message):
    await message.reply_video(video="https://t.me/salom9899/45", caption="🎙 Muftiy Nuriddin Domla\n\nYomonlikdan qaytarishda biror shaxs yoki hududga nisbat berilmaydi")

@dp.message_handler(text="Yurtboshimiz tibbiyot sohasiga qilayotgan e'tiborlari")
async def bot_echo(message:types.Message):
    await message.reply_video(video="https://t.me/salom9899/46", caption="🎙 Shukurulloh Domla\n\nYurtboshimiz tibbiyot sohasiga qilayotgan e'tiborlari")

@dp.message_handler(text="Nasiya savdo haqida")
async def bot_echo(message:types.Message):
    await message.reply_video(video="https://t.me/salom9899/47", caption="🎙 Shukurulloh Domla\n\nNasiya savdo haqida")





























@dp.message_handler(text="👈Orqaga qaytish")
async def bot_echo(message: types.Message):
    await message.answer(text="Ortga muvaffaqiyatli qaytdingiz",reply_markup=bbc)
