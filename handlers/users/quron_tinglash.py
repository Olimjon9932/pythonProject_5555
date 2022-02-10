from aiogram import types
from keyboards.default.quron_tinglash import absd
from loader import dp, bot


# Echo bot
@dp.message_handler(text="🎧QURON TINGLASH🎧")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/Quron_Mishary_Roshid/4",caption="🎙Barcha suralar Mishari Rashid🎙 \n🎙tomonidan ijro qilingan🎙\n👇Marhamat suralarni tinglang👇",reply_markup=absd)

@dp.message_handler(text="FOTIHA")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/3')

@dp.message_handler(text="BAQARA")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/4')

@dp.message_handler(text="IXLOS")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/5')

@dp.message_handler(text="KAVSAR")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/6')

@dp.message_handler(text="FALAQ")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/7')

@dp.message_handler(text="ASR")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/8')

@dp.message_handler(text="HASHAR")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/34')

@dp.message_handler(text="NOS")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/35')

@dp.message_handler(text="AN'OM")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/36')

@dp.message_handler(text="YASIN")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/37')

@dp.message_handler(text="MUHAMMAD")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/38')

@dp.message_handler(text="QADR")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/39')

@dp.message_handler(text="ZALZAL")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/40')

@dp.message_handler(text="SHARH")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/41')

@dp.message_handler(text="QURAYSH")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/42')

@dp.message_handler(text="MO'UN")
async def bot_echo(message: types.Message):
    await message.reply_audio(audio='https://t.me/salom9899/43')


