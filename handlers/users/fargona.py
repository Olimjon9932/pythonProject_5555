from aiogram import types
from keyboards.default.namoz_vaqtlari import www
from keyboards.default.menu import tugma
from loader import dp


# Echo bot
@dp.message_handler(text="FARG'ONA")
async def bot_echo(message: types.Message):
    await message.answer(text="""Namoz Vaqtlari:
=========================
📌 《 🏙 Farg'ona 》 vaqti bilan
--------------------------------------------
🌓  Tong:         -  05:53 
🌞  Quyosh:     -  07:15 

🕰  Bomdod:   -  05:53  
🕰  Peshin:      -  12:27  
🕰  Asr:           -  15:45 
🕰  Shom:       -  17:46  
🕰  Xufton:      -  18:57 
--------------------------------------------
    
📅 2022-yil|Oyning 8-kuni|Seshanba|Soat 16:42""", reply_markup=tugma)
