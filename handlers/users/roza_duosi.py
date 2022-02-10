from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(text="💫RO'ZA DUOSI💫")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://www.savol-javob.com/wp-content/uploads/2020/05/5afc53b68687c.jpg",caption="""Ro'zada og'iz yopish/ochish duolari:     
Ro'za tutish - Og'iz ochish duosi:
Allohumma laka sumtu va bika amantu va ‘alayka tavakkaltu va ‘ala rizqika aftartu, fag‘firli ya g‘offaruma qoddamtu va ma axxortu.
Ma’nosi: Ey Alloh, ushbu ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. 
Ey gunohlarni afv qiluvchi Zot, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.

Iftorlik - Og'iz yopish duosi:
Navaytu an asuma sovma shahri romazona minal fajri ilal mag‘ribi, xolisan lillahi ta’ala. Allohu akbar.
Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun. Alloh Buyukdir.""")
