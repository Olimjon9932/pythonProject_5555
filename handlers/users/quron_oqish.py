import requests as requests
from aiogram import types

from data.config import BOT_TOKEN
from keyboards.default.oqish import tugmalar
from keyboards.default.menu import tugma
from loader import dp, bot


# Echo bot
@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.reply_photo(photo="https://t.me/salom9899/11",caption="📖QURON O'QISH📖 bolimiga xush kelibsiz\nPastdagi menulardan birini tanlang",reply_markup=tugmalar)
@dp.message_handler(text="1.FOTIHA")
async def bot_echo(message: types.Message):
    await message.answer(text="""1. Mehribon va rahmli Alloh nomi bilan (boshlayman). 
2-3-4. Hamdu sano butun olamlar Robbisi, Mehribon va Rahmli, jazo (qiyomat) kunining Egasi — Podshohi bo‘lmish Alloh uchundir. 
5. Sengagina ibodat qilamiz va Sendangina madad so‘raymiz.
6-7. Bizlarni, g‘azabga duchor bo‘lmagan va haq yo‘ldan toymagan zotlarga in’om qilgan yo‘ling bo‘lmish — To‘g‘ri yo‘lga yo‘llagaysan.""")


@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖",reply_markup=tugmalar)

@dp.message_handler(text="2.BAQARA")
async def bot_echo(message: types.Message):
    await message.answer( text = """1. Alif, Lom, Mim.  
  
2. Ushbu (ilohiy) Kitob (Qur'on) shubhadan xoli va (u shunday) taqvodorlar uchun hidoyat  
(manbai)dirkim, 
 
3. ular g'oyib (diniy xabarlar)ga imon keltiradigan, namozni mukammal o'qiydigan va Biz rizq qilib  
bergan narsalardan (sadaqa va) ehson qiladiganlardir. 
 
4. Yana, ular Siz (Muhammad)ga va Sizdan ilgari (o'tgan payqambarlarga) nozil qilingan narsa (ilohiy  
kitoblar)ga imon keltiradigan hamda oxirat (qiyomat)ga qat'iy ishonch hosil qiladiganlardir. 
 
5. Aynan ular Parvardigorlari tomonidan (ato etilgan) hidoyat uzradirlar va aynan ular najot  
topuvchilardir. 
 
6. Haqiqatan, kufr (imonsizlik)ni tanlaganlar - ularni ogohlantirsangiz ham, ogohlantirmasangiz ham,  
ularga baribir - imon keltirmaydilar. 
 
7. Ularning dillari va quloqlariga Alloh muhr urib qo'ygan. Ko'zlarida esa parda (bor). Ular uchun  
ulkan azob (tayyorlab qo'yilgandir). 
 
8. Odamlar orasida shundaylar ham borki, ular "Biz Allohga va oxiratga imon keltirdik", - deydilar.  
Vaholanki, o'zlari mo'min emaslar. 
 
9. Ular (bu bilan) Allohni va imon keltirganlarni aldamoqchi bo'ladilar. Lekin, o'zlari sezmagan holda  
o'zlarinigina aldaydilar. 
 
10. Ularning dillarida xastalik (shubha va kibr kasali) bor. Alloh ularga (shu) xastalikni ziyoda qildi.  
(Mo'minmiz, deb) yolg'on gapirganlari uchun ularga (oxiratda) alamli azob bordir. 

"""
)


@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="3.IXLOS")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  (Ey, Muhammad,) ayting: "U Alloh yagonadir.

2.  Alloh behojat, (lekin) hojatbarordir.

3.  U tug'magan va tug'ilmagan ham.

4.  Shuningdek, Unga biror tengqur ham yo'qdir.

Izoh: Ixlos surasining fazilatlari haqida ko'pgina hadisi shariflar vorid bo'lgan. 
Zero, uning mazmuni tavhidga, ya'ni, Allohning zoti yakka va yagona ekani, Uning sifatlari komil bo'lib, bandalarining sifat va xususiyatlaridan tubdan farq qilishi tasvirlangan. Mazkur hadislarda bu sura Qur'oni karimning uchdan biriga tengligi, uni o'n bor o'qigan kishiga jannatda bir qasr barpo etilishi, uni qiroat qilish jannatiylik sababi ekani kabi bashoratlar mavjud""")


@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="4.KAVSAR")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  (Ey, Muhammad,) albatta, Biz Sizga Kavsarni ato etdik.

Izoh: Kavsar so'zining daryo va hovuzdan boshqa ma'nolari ham mavjud ekanligi tafsirlarda bayon etilgan.
 Masalan, Kavsar - bu kasir so'zining mubolag'a siyqasi, ya'ni juda ko'p (yaxshi) narsalar, yaxshiliklarni ato etdik, degan ma'noni ham anglatadi.

2.  Bas, Rabbingiz uchun namoz o'qing va (tuya) so'yib qurbonlik qiling!

3.  Albatta, g'animingizning o'zi (barcha yaxshiliklardan) mahrumdir.

Izoh: Sura oxirida Payg'ambar dushmanlarini ta'riflab Alloh taolo ular - abtar, deydi. 
Abtar so'zining ham bir necha tafsirlari mavjud. Masalan abtar - barcha yaxshiliklardan mahrum; nomi o'chadigan; nasl-nasabi quriydigan; sulolasi qirqilgan va hokazo.
 Payg'ambar (a. s.)ga nisbatan mushriklar bu so'zni qo'llab, undan o'g'il farzand qolmadi, demak uning nomi ham, zurriyoti ham qirqildi, deb ta'na qilganlarida, Alloh taolo shu qisqa sura orqali ularga raddiya berdi.""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="5.FALAQ")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  (Ey, Muhammad,) ayting: "Panoh tilab iltijo qilurman tong Parvardigoriga,

2.  yaratgan narsalari yovuzligidan,

3.  zulmatga cho'mgan tun yovuzligidan,

4.  tugunchalarga dam uruvchi ayollar yovuzligidan

5.  hamda hasadchining hasadi yovuzligidan.

Izoh: Bu suraning fazilatlari to'g'risida ko'pgina hadisi shariflar mavjud. 
Barcha yomonlik va yovuzliklardan omonda bo'lish uchun Falaq, Nos, 
Ixlos suralarini o'qib Allohdan najot so'rashning foydalari to'g'risida Payg'ambarimiz Muhammad (a. s.) ko'p bashoratlarni aytib ketganlar.""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="6.ASR")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  Asrga qasamki,

Izoh: Asr so'zi arab tilida bir necha mazmunga dalolat qiladi. 
Jumladan, asr namozi, har yuz yillik muddat, Payg’ambarimiz yashagan asr, siqib suvini chiqarish kabi ma'nolarni o'z ichiga oladi. 
Surada zikr etilgan asr so'zidan murod asr namozi yoxud asri saodat, ya'ni, Rasululloh yashagan asr maqsad qilingan bo'lishi mumkin. Vallohu a'lam.

2.  (har bir) inson ziyon (baxtsizlik)dadir!

3.  Faqat imon keltirgan va solih amallarni qilgan, bir-birlariga 
Haq (yo'li)ni tavsiya etgan va bir- birlariga sabrli bo'lishni tavsiya etgan zotlargina (bundan ustasnodirlar).""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="7.HASHAR")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  Osmonlardagi va Yerdagi bor narsa Allohga tasbeh aytur. U qudrat va hikmat sohibidir.

2.  U ahli kitoblardan (yahudiylardan) kofir bo'lgan kimsalarni birinchi "to'plash"dayoq o'z diyorlaridan haydab chiqargan zotdir. (Ey, mo'minlar,) sizlar ularni chiqib ketishlarini o'ylagan ham emas edingiz, ular ham o'zlarining qal'alarini Alloh (azobi)dan to'suvchi deb o'ylagan edilar. Bas, Alloh(ning azobi) ular hisobga olmagan tomondan keldi va dillariga qo'rqinch soldi. Ular uylarini o'z qo'llari va mo'min- larning qo'llari bilan buzar edilar. Bas, ey, aql egalari, (ulardan) ibrat olingiz!

Izoh: Qamalda qolgan Banu Nazir qabilasi kishilari ikkinchi bor sulh tuzishni taklif qiladilar, lekin Rasululloh bir marta sulhga xiyonat qilgan bu qabila bilan sulh tuzishdan bosh tortadilar va narsalarini olib yurtdan chiqib ketishlarini talab qiladilar. Talab amalga oshadi.

3.  Agar Alloh ularga surgunni yozmaganida, albatta, ularni mana shu dunyoda (qatl qilish yoki asrga olish bilan) azoblagan bo'lur edik. Ular uchun oxiratda do'zax azobi ham bordir.

4.  Bunga sabab, ularning Alloh va Uning payg'ambariga qarshi turganlaridir. Kimki Allhga qarshi tursa, bas, Alloh jazosi qattiq zotdir.

5.  (Ey, imon keltirganlar,) sizlar (Banu Nazir xurmozorlaridan) biror xurmo daraxtini kesdinglarmi yoki uni o'z tanalarida turgan holida qoldirdinglarmi, bas, (qilingan ish) Allohning izni bilan va fosiq (itoatsiz) kimsalarni rasvo qilish uchundir.

6.  Alloh O'z Payg'ambariga ulardan o'lja qilib bergan narsalar ustiga sizlar ot va tuyalarni minib borganlaringiz yo'q (qiynalib qo'lga kiritganlaringiz yo'q), lekin Alloh O'z payg' ambarlarini O'zi xohlagan kimsalardan ustun qilib qo'yar. Alloh har narsaga qodirdir.

7.  Alloh qishloq (shahar)larning (kofir) aholisidan o'z payg'ambariga o'lja qilib bergan narsalar - toki sizlardan boy-badavlat kishilar o'rtasidagina qo'lma-qo'l bo'lib yuraveradigan narsa bo'lib qolmasligi uchun - Allohga, Payg'ambarga va (u zotning) qarindoshlari, yetimlar, miskinlar va musofirlarga tegishlidir. Payg'ambar sizlarga keltirgan narsani olinglar, u sizlarni qaytargan narsadan qaytinglar va Allohdan qo'rqinglar! Albatta, Alloh jazosi qattiq zotdir.

8.  (U o'ljalar yana) o'z diyorlaridan va mol-mulklaridan haydab chiqarilgan zotlar - kambag'al muhojirlarnikidir, zero, ular Allohdan fazl va rizolik istaganlar hamda Alloh va Uning payqambariga yordam berganlar. Aynan o'shalar (imonlarida) sodiqdirlar.

9.  Ulardan (muhojirlardan) ilgari (Madinadek) diyorda yashagan va imonni saqlaganlar (ansorlar) esa o'zlari (yonlari)ga hijrat qilib kelgan kishilarni suyurlar va dillarida ularga berilgan narsa (o'ljalar) sababli hasad sezmaslar hamda o'zlarida ehtiyoj bo'la turib, (ehson qilishda o'zgalarni) ixtiyor qilurlar. Kimki o'z nafsi baxilligidan saqlana olsa, bas, ana o'shalar iqbollidirlar.

Izoh: Bu oyati karimada madinalik musulmonlar qanchalik oliyjanob muruvvatli va saxiy ekanlari ta'rif etilgan.
 
O'zlari muhtoj bo'laturib, narsalarini o'zga muhtojlarga ehson qilish bu saxovat va karamning eng yuqori cho'qqisidir. Bu xislat arab tilida "iysor" deyiladi.

10.  Ulardan keyin (dunyoga) kelgan zotlar ayturlar: "Ey, Rab bimiz, O'zing bizlarni va bizlardan ilgari imon bilan o'tganlarni mag'firat qilgin va qalblarimizda imon keltirgan zotlarga nisbatan gina paydo qilmagin! Ey, Rabbimiz, albatta, Sen mehribon va rahmlidirsan!"
""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="8.NOS")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  (Ey, Muhammad,) ayting: "Panoh tilab iltijo qilurman odamlar Parvardigoriga,

2.  odamlar Podshohiga,

3.  odamlar Ilohiga

4.  yashirin vasvasachi (shayton) yovuzligidanki,

5.  (u) odamlarning dillariga vasvasa solur.

6.  (O'zi) jinlar va odamlardandir".

Izoh: Hadisi shariflarda kelgan ma'lumotlarga qaraganda Qur'oni karimning oxiridagi mazkur ikki sura janob Rasululloh sehrlanganlarida shifo tariqasida nozil qilingan. 
Qissaning asli shunday bo'lgan. Yahudiylardan Labid ibn al-A'sam degan bir munofiq o'zini musulmon ko'rsatib, Payqambar huzurlariga kelib-ketib yurar va ba'zi hojatlarini ado etishda xizmat qilib turar ekan.
Shu xodimni qo'lga olib bir guruh yahudiylar uning yordamida Rasulullohning to'kilgan sochlari va taroqidan sinib tushgan tishlarini qo'lga tushiradilar va shu narsalarga sehr jodu qilib bir eski quduqqa tashlaydilar. 
Shundan keyin Rasulullohning sochlari to'kilib, olti oy betob bo'lib yotib qoladilar. Bir kuni ikki farishta kelib, biri tizzalari ro'parasiga, ikkinchisi bosh tomonlariga o'tirib bir-biri bilan savol-javob qiladilar.
 Biri:
-  Unga nima bo'libdi? -desa, ikkinchisi:
-  Sehrlanibdi, - der edi.
-  Kim sehrlabdi?
-  Labid ibn al-A'sam ismli bir yahudiy.
-  Sehrni nimaga o'qibdi?
-  To'kilgan sochlari va taroq tishlariga.
-  Sehr o'qilgan narsalar qayerga tashlangan?
-  Zarvon ismli quduqqa.
Shundan keyin odam yuborib ko'rsalar, haqiqatan, o'sha quduqda soch tolalari, taroq tishlari va nina suqilgan yana o'n ikkita tugun bor ekan. Shu paytda Alloh taolo mazkur ikki surani nozil qiladi. Suralarni har bir marta o'qiganlarida, bittadan tugun yechilar ekan. Shunday qilib, o'n ikki marta o'qiganlarida darddan butunlay foriq bo'lib ketgan ekanlar. Rasul Akram (s. a. v. ) sahobalarning: "Labidni qatl etaylik", - degan talablarini esa rad qilgan ekanlar.""")


@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="9.AN'OM")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  Hamd osmonlar va Yerni yaratgan, zulmatlar va nurni paydo etgan Allohga (xos)dir. So'ngra kufrga ketganlar Parvardigorlariga (soxta ma'budalarni) tenglashtirmoqdalar.

2.  (U) Sizlarni (Odam Atoni) loydan yaratib, so'ngra ajal (muddati)ni hal qilgan zotdir. Belgilangan ajal (qiyomat bo'lish vaqti va boshqa hisoblar) ham Uning huzuridadir. (Shundan) keyin (ham) sizlar shak qilmoqdasizlar.

3.  U osmonlarda ham, Yerda ham Allohdir. Sir tutganu oshkor qilgan narsalaringizni bilur. Qilayotgan ishlaringizni (ham) bilur.

4.  Ularga (Makka mushriklariga) Parvardigorlarining dalillaridan (qanday bir) dalil kelmasin, (baribir) undan yuz o'giruvchi bo'ldilar.

5.  Ularga haqiqat (Qur'on) kelishi bilan uni yolg'onga chiqardilar. Ularga o'zlari mazax qilib yurgan narsa (Qur'on)ning xabarlari tez orada kelib qolur.

6.  Ulardan oldin necha avlodni halok etganimizni ko'rmadilarmi?! Ularga Yerda sizlarga bermagan imkoniyatlarni berdik, ustilariga osmon (yomg'ir)ni yog'dirdik va ostilaridan anhorlarni oqizib qo'ydik. So'ngra gunohlari tufayli ularni halok qildik va ulardan keyin boshqa avlodni keltirdik.

7.  Bordiyu Sizga (ey, Muhammad,) qog'ozga (yozilgan) bitikni tushirsagu uni qo'llari bilan siypalab ko'rganlarida ham (baribir) kufrga ketganlar: "Bu aniq sehrdan boshqa (narsa) emas", - degan bo'lur edilar.

8.  Yana ular: "Unga biror farishta tushsa edi", - dedilar. Agar farishta tushirsak, ish hal bo'lur edi. So'ngra ularga muhlat berib o'tirilmas edi.

9.  Bordiyu uni (Payg'ambarni) farishta qilganimizda ham, uni erkak (kishi suratida) qilgan va ularga qorong'u (gumon) bo'lgan narsani (yana) qorong'uligicha qoldirgan bo'lar edik.

Izoh: Ya'ni tushirilgan farishtani erkak suratida qilganimizdan keyin ular yana: "bu farishta emas", - deb qaysarlik qilgan bo'lur edilar.

10.  Sizdan oldingi payg'ambarlar ham istehzo (mazax) qilingan. So'ngra ularni masxara qilganlarni o'sha mazax qilgan narsalari (ya'ni, haqiqat) qamrab oldi (halok etdi).

11.  Ayting: "Yerni sayr qilib (aylanib) chiqinglar. So'ngra (payg'ambarni) yolg'onchiga chiqarganlarning (oxir-)oqibati ne bo'lganini ko'ringlar!"

12.  Ayting: "Osmonlar va Yerdagi bor narsa kimniki?" Ayting: "Allohniki". (U) O'ziga rahmatni (bor mavjudotga rahm-shafqat qilishni) yozdi (va'da qildi). Sizlarni, albatta, Qiyomat kuniga jam qilajak.
 
Bunda shak yo'qdir. O'zlariga (nisbatan) ziyonkor bo'lganlar (bunga) imon keltirmaydilar.

13.  Kecha va kunduzda sokin turuvchi narsalar (ham) Unikidir. U eshituvchi va biluvchidir.

14.  Ayting: "Osmonlaru Yerni ixtiro etgan, (o'zgalarga) yedirib, O'zi yemaydigan - Allohdan o'zgani do'st tutayinmi?!" Ayting: "Darhaqiqat, men musulmonlarning birinchisi bo'lishga buyurildim. Aslo mushriklardan bo'lmangiz! (deb ham)"

15.  Ayting: "Albatta, men agar Rabbimga nofarmonlik qilsam, ulug' Kunning azobidan qo'rqaman".
""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="10.YASIN")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  Yo, Sin.

2.  (Ey, Muhammad, ushbu) hikmatli Qur'onga qasamki,

3.  haqiqatan, Siz payg'ambarlardandirsiz!

4.  (Siz) To'g'ri yo'ldadirsiz.

5.  (Bu Qur'on) qudratli va rahmli (Alloh)ning nozil qilgan (Kitob)idir,

6.  toki ota-bobolari ogohlantirilmay, g'ofil bo'lib qolgan qavmni ogohlantirgaysiz.

7.  Ularning ko'plariga So'z (azob haqidagi hukm) muqarrar bo'lgandir. Bas, ular imon keltirmaslar.

8.  Darhaqiqat, Biz ularning bo'yinlariga, to iyaklarigacha kishanlarni solib qo'ydik, bas, ular kekkayuvchilardir.

9.  Yana ularning oldilaridan bir to'siq (parda), ortlaridan bir to'siq (parda) qilib, ularni o'rab qo'ydik. Bas ular "ko'ra" olmaslar.

Izoh: Bu oyat Abu Jahl Maxzumiy haqida nozil bo'lgan. U Rasulullohni namoz o'qiyotgan paytlarida boshlariga tosh bilan urib majruh qilishga qasam ichgan bo'lib, maqsadini amalga oshirmoqchi bo'lganida toshni ko'targanicha qo'llari toshga yopishib qoladi. Sharmanda bo'lib o'z qavmiga qaytib kelgach, boshqa biri "Bu ishni men bajaraman" - deb ravona bo'lganida, Alloh taolo amri bilan uning ko'zi ko'r bo'lib qoladi.

10.  (Ey, Muhammad,) Siz ularni ogohlantirdingizmi yoki ogohlantirmadingizmi – ularga barobardir - imon keltirmaslar.

11.  Siz faqat Zikr (Јur'on)ga ergashgan va Rahmondan g'oyibona qo'rqqan kishilarnigina ogohlantira olursiz. Bas, o'shalarga mag'firat va ulug' mukofot (jannat) xushxabarini bering!

12.  Albatta, Biz o'liklarni tiriltirurmiz va ularning qilgan amallarini hamda (qoldirgan) izlarini yozib qo'yurmiz. Barcha narsani Biz aniqlab beruvchi Imom (Lavhul-Mahfuz)da hisobga olganmiz.

13.  (Ey, Muhammad,) Siz ularga qishloq (ahli)ni - u joyga elchilar kelgan paytini misol keltiring!
 
Izoh: Qishloqning nomi Antokiya bo'lib, u Rum (hozirgi Italiya) ning qadimiy qishloqlaridan biridir.

14.  O'shanda Biz ularga ikkita (elchi)ni yuborganimizda (ular) ikkisini yolg'onchiga chiqarishgach, uchinchi (elchi) bilan quvvatlantirdik. Bas, (uchchala elchi Antokiya ahliga): "Haqiqatan, biz sizlarga (yuborilgan) elchilarmiz", degan edilar.

15.  Ular: "Sizlar ham xuddi bizga o'xshagan odamlarsiz. Rahmon (Alloh) biror narsa (vahiy) nozil qilgani yo'q. Sizlar faqat yolg'on so'zlamoqdasizlar", - dedilar.

16.  (Elchilar) aytdilar: "Rabbimiz bilurki, bizlar, albatta, sizlarga (yuborilgan) elchilardirmiz!

17.  Bizlarning zimmamizda faqat (Allohning vahiysini sizlarga) aniq yetkazishgina bordir".

18.  (Ular) dedilar: "Bizlar sizlardan shumlanmoqdamiz. Јasamki, agar (da'vatlaringizni) to'xtatmasangizlar, sizlarni, albatta, toshbo'ron qilurmiz va sizlarga biz tomondan alamli azob yetar".

19.  (Elchilar) aytdilar: "Shumlanishingiz o'zlaringiz bilandir. Sizlarga nasihat qilinsa (shumlanasizlarmi)?! Yo'q, sizlar haddan oshgan qavmdirsiz!"

20.  (Shu payt) bir kishi shaharning ichkarisidan shoshgancha kelib, dedi: "Ey, qavmim, (bu) elchilarga ergashinglar!""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="11.MUHAMMAD")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  Kofir bo'lgan va (o'zgalarni ham) Alloh yo'lidan to'sgan kimsalarning amallarini (Alloh) zoye ketkazur.

2.  Imon keltirgan va solih amallarni qilgan hamda Muhammadga nozil qilingan narsaga (Qur'onga) - holbuki, u Parvardigorlari tomonidan kelgan haqiqatdir - imon keltirgan zotlarning esa yomonlik (gunoh)larini o'chirur va ishlarini o'nglar.

3.  Bunga sabab - kofir bo'lganlarning nohaq (yo'l)ga ergashganlari, imon keltirganlarining esa Parvardigorlari (tomoni)dan bo'lmish haq (Qur'on yo'li)ga ergashganlaridir. Alloh insonlarga ularning misollarini mana shunday bayon qilur.

4.  Bas, (ey, mo’minlar,) qachonki, sizlar (jang maydonida) kofir bo'lganlar bilan to'qnashganlaringizda, bo'yinlariga uringiz (o'ldiringiz)! Bas, qachonki, ularni qirg'inga tutib asir olgach, arqonlar bilan bog'langiz! So'ng yo (ularni ozod qilib) marhamat ko'rsatursizlar, yo (qo'yib yuborib) fidya (tovon) olursizlar. Toki urush yuklarini qo'ygunicha (to'xtagunicha, sizlarga buyruq) mana shudir. Agar Alloh xohlasa, ular ustidan (jangsiz ham) g'alaba qilur edi, lekin U sizlarning ayrimlaringizni ayrimlaringiz bilan imtihon qilish uchun (sizlarni jangga buyurdi). Alloh yo'lida o'ldirilganlarning amallarini (U) sira zoye ketkizmas.

Izoh: Hijratning uchinchi yilida Madina shahri hududidagi Uhud tog'i etagida musulmonlar bilan Makka mushriklari o'rtasida kechgan jangga oid oyatlar.

5.  Ularni (jannat yo'liga) hidoyat qilur va ishlarini isloh etur.

6.  Ularni (Alloh) O'zi ta'riflagan jannatga kiritur.

7.  Ey, imon keltirganlar, agar sizlar Allohga yordam bersangizlar (dinining rivoji uchun harakat qilsangizlar), U zot ham sizlarga yordam berur va qadamlaringizni sobit (barqaror) qilur.

8.  Kofir bo'lgan kimsalar uchun esa halokat bo'lur va (Alloh) ularning amallarini zoye ketkazur.

9.  Bunga sabab ularning Alloh nozil qilgan narsalarni (Qur'on va undagi hukmlarni) yomon ko'rganlaridir. Bas, (Alloh) ularning amallarini behuda ketkazur.

10.  Axir, ular yer yuzida sayr (sayohat) qilishib, o'zlaridan avvalgi (imonsiz) kimsalarning oqibatlari qanday bo'lganini ko'rsalar bo'lmaydimi? Alloh ularni yakson etdi-ku! Kofirlar uchun ham xuddi o'sha (oqibat)larning o'xshashi bo'lur.

11.  Bunga sabab imon keltirganlar Allohning do'sti (homiysi) ekani va kofirlarga esa hech qanday homiy yo'q ekanidir.

12.  Albatta, Alloh imon keltirgan va solih amallarni qilgan zotlarni ostidan anhorlar oqib turadigan jannatlarga kiritur. Kofir bo'lgan kimsalar esa (dunyo lazzatlaridan) foydalanib, chorva hayvonlari
 
yeganidek yeb-ichurlar va do'zax ularning joylaridir.

13.  (Ey, Muhammad,) Sizni haydab chiqargan shahar (Makka ahli)dan ko'ra (aholisi) quvvatliroq bo'lgan qanchadan-qancha shaharni halok qilganmiz. Bas, ularga biror yordamchi bo'lmagan.

14.  Axir, Parvardigori tomonidan (aniq) hujjatga (Qur'onga) ega bo'lgan kishi (Siz va mo’minlar) bilan qilgan yomon ishi o'ziga chiroyli ko'ringan va havoyi nafsiga ergashgan (kofir) barobar bo'lurmi?!

15.  Taqvoli zotlar uchun va'da qilingan jannatning misoli (sifati budir): Unda aynimas suvdan iborat daryolar ham, ta'mi o'zgarmas sutdan iborat daryolar ham, ichuvchilar uchun lazzatli (aqldan ozdirmaydigan) maydan bo'lmish daryolar ham va musaffo asaldan iborat daryolar ham bordir. Ular uchun u joyda barcha mevalardan bordir va (u joyda) Parvardigorlari (tomoni)dan mag'firat bordir. (Ana shunday zotlar) do'zaxda mangu qoladigan va qaynoq suv bilan sug'orilganda ichaklarini tilka- pora qilib tashlaydigan (kofir)lar kabi bo'lurmilar?!
""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="12.QADR")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  Albatta, Biz u (Qur'on)ni Qadr kechasida nozil qildik.

2.  (Ey, Muhammad,) Qadr kechasi nima ekanini Sizga ne ham anglatur?!

3.  Qadr kechasi ming oydan yaxshiroqdir.

Izoh: Bu ulug’ kecha Ramazon oyining 27-kechasi ekaniga dalolat qiladigan hadis va rivoyatlar ko'pdir.

4.  U (kecha)da farishtalar va Ruh (Jabroil) Parvardigorlarining izni bilan (yil davomida qilinadigan) barcha ishlar (rejasi) bilan (osmondan yerga) tusharlar.

5.  U (kecha) to tong otgunicha salomatlikdir.""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="13.ZALZAL")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  Qachonki, Yer o'zining (eng dahshatli) zilzilasi bilan qimirlaganida,

2.  Yer (o'z qa'ridagi konlaru murdalardan iborat) "yuk"larini (yuzaga) chiqarib tashlaganida

3.  va (qayta tirilishni inkor qiluvchi) inson (dahshatga tushib): "Unga ne bo'ldi ekan?" - deb qolganida

4.  ana o'sha kunda Yer o'z xabarlarini so'zlar.

Izoh: Yerning xabarlari uning ustida yurgan bandalarning qilmishlaridir. Ular haqida yerning Alloh oldida guvohlik berishi o'ta dahshatli hodisadir Suraning davomida har bir banda dunyoda qilib o'tgan yaxshi-yomon ishlari bitilgan nomai a'moli qo'liga berilgach, uni o'qib ko'rishi ta'kidlanadi. Bu oyatlardagi ilohiy hikmatlarni tafakkur bilan poyoniga yetish juda qiyin. Ba'zi ulug’ olimlarning yozishiga qaraganda, har bir inson oxiratda o'z nomasini o'qib ko'radi. Lekin boshqa odam buni o'qimaydi, bilmaydi ham. Aks holda ba'zi ishlaridan xijolat bo'lishga to'g’ri keladi. Alloh taolo o'sha joyda ham bandalarining noshoyista qilmishlarini hammaga fosh qilmay, o'zining rahmat va mag’firatini namoyon qilishidan bu yerda bashorat berilmoqda (Anisul-jalis).

5.  (So'zlashga) Rabbingiz vahiy (ruxsat) qilganini aytur.

6.  O'sha Kuni odamlar, ularga (nomai) a'mollarini ko'rsatilishi uchun to'da-to'da bo'lib chiqib kelurlar.

7.  Bas, kimki dunyoda zarra miqdorida yaxshilik qilgan bo'lsa, (Qiyomat kuni) uni ko'rar.

8.  Kimki zarra miqdorida yomonlik qilgan bo'lsa, uni ham ko'rar.""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="14.SHARH")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  (Ey, Muhammad,) ko'ksingizni (ilmu-hikmatga) keng ochib qo'ymadikmi?!

2.  Sizdan yukingizni olib qo'ydik,

3.  qaysiki, belingizni ezib turgan edi.

Izoh: Bellarini ezib turgan yuk On hazratdan sodir bo'lgan ba'zi kichik sahvu xatolar. Chunonchi "Abasa" surasi izohida qayd etildi.

4.  Zikringizni (martabangizni) ham baland qilib qo'ydik.

5.  Bas, albatta, har bir qiyinchilik bilan birga yengillik bordir.

6.  Albatta, har bir qiyinchilik bilan birga yengillik bordir.

7.  Bas, (ey, Muhammad,) qachonki, (namozdan) foriq bo'lsangiz, (o'rningizdan) turing

8.  va Rabbingiz sari rag'bat (bilan iltijo) qiling!""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="15.QURAYSH")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  Quraysh (aholisi)ga qulay qilib qo'ygani uchun,

2.  ya'ni ularga qishda (Yamanga) va yozda (Shomga) safar qilishni qulay qilib qo'ygani uchun

3.  mana shu Uy(Ka'ba)ning Parvardigoriga ibodat qilsinlar!

4.  Zero, (U) ularni ochlikdan (qutqarib) taomlantirdi va xavf (va xatar)dan xotirjam qildi.

Izoh: Surada Yamanga qishda, Shomga yozda safar qilish haqida aytildi. 
Makka ahli yozning issiq kunlari Yaman diyorlari o'ta qizib ketishini bilib, bu faslda salqinroq Shom diyoriga tijorat safarini uyushtirar, qishda kunlar biroz soviganda esa Yaman diyoriga safar qilar edilar.""")

@dp.message_handler(text="📖QURON O'QISH📖")
async def bot_echo(message: types.Message):
    await message.answer(text="📖QURON O'QISH📖", reply_markup=tugmalar)

@dp.message_handler(text="16.MO'UN")
async def bot_echo(message: types.Message):
    await message.answer(text="""Mehribon va rahmli Alloh nomi bilan (boshlayman).

1.  Dinni (oxirat jazosini) inkor etadigan kimsani ko'rdingizmi?!

2.  Bas, u yetimni jerkiydigan

3.  va miskin (bechora)ga taom berishga targ'ib qilmaydigan kimsadir. Izoh: Bu sifat egalari Makkaning ashaddiy kofirlaridir. Os ibn Voil, Valid ibn Mug'ira kabilardir. Oyat ular sha'niga doir bo'lsa-da, uning hukmi umumiy bo'lib, har bir momin-musulmon bu kabi salbiy xususiyatlardan xoli bo'lishiga harakat qilish zarurdir.

4.  Bas, shunday namozxonlar holiga voyki,

5.  ular namozlarini "unutib" qo'yadilar,

6.  riyokorlik qiladilar

7.  va ro'zg'or buyumlarini (kishilardan) man etadilar.""")

@dp.message_handler(text="👈Orqaga qaytish")
async def bot_echo(message: types.Message):
    await message.answer(text="Ortga muvaffaqiyatli qaytdingiz",reply_markup=tugma)