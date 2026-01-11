import asyncio
import logging
import json
import os
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandObject
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime

# --- SOZLAMALAR ---
API_TOKEN = '8211312966:AAFybS2_LAgADfQVobVZ1G-McNmBBTcty2g'
ADMIN_ID = 512345678  # BU YERGA O'ZINGIZNING ID RAQAMINGIZNI YOZING!
ADMIN_USERNAME = "oyatillo14"
CHANNEL_URL = "https://t.me/insta_akkount2"
DB_FILE = 'users_data.json'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- MA'LUMOTLAR BAZASI ---
if not os.path.exists(DB_FILE):
    with open(DB_FILE, 'w') as f:
        json.dump({}, f)

def load_data():
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- DIZAYN ELEMENTLARI ---
STARS = "⭐ ⭐ ⭐ ⭐ ⭐"
LINE = "━━━━━━━━━━━━━━━━━━━━"

# --- BIO MA'LUMOTLARI ---
bio_data = {
    "food": [
        "🍕 Mazali hayot, shinam muhit!\n📍 Manzil: Toshkent\n📞 Buyurtma: +998...",
        "🍔 Eat well, Live better!\n✨ Eng mazali burgerlar bizda\n🚚 Yetkazib berish mavjud",
        "🍰 Shirinliklar dunyosiga xush kelibsiz!\n🎂 Har kuni yangi pishiriqlar",
        "🥗 Sog'lom tanlovlar, mazali taomlar!\n🌿 Organik mahsulotlar\n📩 Buyurtma uchun DM",
        "🍣 Sushi va rolls olamiga sayohat!\n🎏 Har kuni yangi menu\n🚚 Yetkazib berish mavjud",
        "🍩 Donuts va qandolatlar\n💖 Shirinliklarimiz bilan hayotingni shirin qil\n📞 Buyurtma qiling",
        "🥘 An'anaviy va xalqaro taomlar\n🍴 Har taomga sevgi qo‘shamiz\n📍 Toshkent",
        "🍹 Fresh va vitaminli ichimliklar\n🌞 Sog‘lom hayot uchun\n📩 DM orqali buyurtma",
        "🍔 Fast food yoki slow food?\n🔥 Har doim yangi ta’mlar\n🚚 Yetkazib beramiz",
        "🍰 Birthday yoki coffee time?\n🎉 Biz bilan shirin dam\n📞 Buyurtma: +998...",
        "🥗 Salat va smoothie bar\n💚 Sog‘lom tanlov\n📩 Onlayn buyurtma mavjud",
        "🍕 Pitsa va panini sevgisi\n🍅 Faqat sifatli mahsulotlar\n📍 Toshkent",
        "🍣 Sushi party har kuni!\n🎏 Fresh va tayyor\n🚚 Yetkazib berish mavjud",
        "🍩 Shirinliklar bilan quvonch\n💖 Har bir qadam shirin\n📞 DM orqali buyurtma",
        "🥘 Taomlarimiz bilan dunyoni kashf et!\n🍴 Har doim yangi retseptlar\n📍 Toshkent",
        "🍹 Vitaminli va fresh drinks\n🌞 Energiya bilan kuningizni boshlang\n📩 DM orqali",
        "🍔 Burger & snack heaven\n🔥 Mazali va tez yetkazib berish\n📞 Buyurtma",
        "🍰 Sweet moments with us!\n🎂 Har doim yangi shirinliklar\n🚚 Yetkazib berish",
        "🥗 Healthy life starts here\n🌿 Fresh va organic\n📍 Toshkent",
        "🍕 Pizza & smiles\n🍅 Har bir bo‘lakda sevgi\n📞 Buyurtma qilish mumkin"
    ],
    "shop": [
        "👗 Stil va sifat uyg'unligi\n🛍️ O'zbekiston bo'ylab yetkazish\n📥 Buyurtma uchun DM",
        "✨ Go'zallik sizdan, liboslar bizdan\n💎 Premium sifatdagi kiyimlar\n🌟 @insta_akkount2",
        "👠 Trendy va zamonaviy\n🛒 Har xil brendlar\n📩 DM orqali buyurtma",
        "👜 Bag va aksessuarlar\n💖 Har biri original\n📍 Toshkent",
        "👚 Yozgi kollektsiyalar tayyor!\n🌞 Eng yangi liboslar\n📥 DM orqali buyurtma",
        "👖 Denim va casual uslublar\n🔥 Har kuni yangi chegirma\n📞 Bog‘lanish: +998...",
        "👗 Fashion hub\n🌟 Kiyimlarimiz bilan stil yarating\n📩 DM mavjud",
        "🧥 Outerwear va cozy look\n❄️ Sifat va qulaylik\n📍 Toshkent",
        "👟 Sport va street style\n🏃 Har bir qadamga mos\n📥 DM orqali",
        "👗 Evening & party wear\n✨ Har doim zamonaviy\n📞 Buyurtma: +998...",
        "👜 Luxury va minimalizm\n💎 Har bir detal muhim\n📩 DM orqali",
        "👚 Casual va office wear\n🛍️ Eng yaxshi materiallar\n📍 Toshkent",
        "👠 Trendsetter uchun\n🔥 Moda va stil birlashadi\n📞 Buyurtma",
        "👖 Jeans & more\n💖 Har kuni yangi koleksiya\n📥 DM orqali",
        "🧥 Seasonal outerwear\n❄️ Sifat + qulaylik\n📍 Toshkent",
        "👟 Sneakers & lifestyle\n🏃 Har bir qadamga mos\n📩 DM orqali",
        "👗 Glam & chic outfits\n✨ Har doim zamonaviy\n📞 Buyurtma",
        "👜 Elegant bags\n💎 Har bir detal original\n📍 Toshkent",
        "👚 Trendy tops & dresses\n🔥 Stil va sifat\n📩 DM orqali",
        "👠 Shoes & heels heaven\n💖 Har qadamda qulaylik\n📞 Buyurtma"
    ],
    "smm": [
        "🚀 Biznesingizni raketa kabi uchiramiz\n📈 Sotuvlarni oshirish sirlari\n📩 Hamkorlik uchun DM",
        "💎 SMM Universe Pro - Professional xizmatlar\n🎯 Target | Dizayn | Kontent\n🔥 Brendingizni yarating",
        "📊 Sotuvlar va brendni oshiring\n🚀 Social media marketing\n📩 DM orqali bog‘laning",
        "🎯 Kontent va kampaniyalar\n💡 Kreativ strategiyalar\n📞 Biz bilan bog‘laning",
        "📈 Target reklamalar\n💻 Digital marketing mutaxassislari\n🔥 Natijaga erishing",
        "💎 Brendingizni yaratamiz\n🚀 SMM, SEO, Content\n📩 Hamkorlik uchun DM",
        "📊 Social media audit\n🎯 Strategiya va dizayn\n📞 Bog‘lanish: +998...",
        "🚀 Instagram, Telegram, TikTok\n💡 Kreativ va innovatsion\n📩 DM orqali",
        "🎯 Natijaga yo‘naltirilgan kampaniyalar\n💻 Marketing automation\n🔥 Biz bilan rivojlaning",
        "📈 Analitika + kreativ\n💎 SMM bilan o‘sish\n📞 Bog‘lanish: +998...",
        "💡 Kontent strategiyasi\n🚀 Brendingizni yuqoriga ko‘tarish\n📩 DM orqali",
        "🎯 Ads & target marketing\n📊 Statistika va optimizatsiya\n🔥 Natija kafolatlangan",
        "📊 Social media optimization\n💎 Eng samarali yechim\n📞 Bog‘lanish: +998...",
        "🚀 TikTok va Instagram uchun\n🎯 Viral kampaniyalar\n📩 Hamkorlik uchun DM",
        "💡 Kreativ kontent\n📈 Harakat bilan natija\n🔥 Biz bilan rivojlaning",
        "🎯 Targeting & Ads\n💻 Marketing strategiyasi\n📞 Bog‘lanish: +998...",
        "📊 Social media boost\n🚀 Sotuvlarni oshiring\n📩 DM orqali",
        "💎 Kontent va branding\n🎯 Har doim yuqori sifati\n🔥 Hamkorlik uchun",
        "🚀 Campaign management\n📈 Analitika va optimizatsiya\n📞 DM orqali",
        "💡 Brendingizni o‘siting\n🎯 Social media mutaxassislari\n🔥 Natijaga erishing"
    ],
    "sport": [
        "💪 Bugun qilmagan ishingni ertaga afsus qilasan\n🏋️‍♂️ Har kuni mashg'ulot\n🏆 Maqsad sari olg'a!",
        "🔥 To'xtama, harakat qil!\n🥗 Sog'lom turmush tarzi\n🥇 Champion Mindset",
        "🏋️‍♀️ Har kuni o‘z ustingda ishlash\n💦 Terlab, kuch top\n🏆 Natija kutmoqda",
        "💪 Iroda + harakat = muvaffaqiyat\n🏃‍♂️ Sport bilan hayot\n🥇 Eng yaxshisi sen",
        "🔥 Sport — kuch va energiya\n💦 Harakat qil, to‘xtama\n🏆 Maqsad sari",
        "💪 Har kuni bir oz yaxshilanish\n🏋️ Mashq qilish — hayot\n🥇 G‘alaba senga",
        "🏃‍♀️ Yurak va mushaklarni kuchaytir\n💦 Terlab, rivojlan\n💯 Harakat senga kuch",
        "💪 Sabr, iroda va kuch\n🏋️‍♂️ Har doim o‘z ustingda ishlash\n🏆 Natija yaqin",
        "🔥 Harakat qil, o‘zingni sinab ko‘r\n💦 Sport bilan sog‘lom hayot\n🥇 Maqsad sari",
        "💪 Jismoniy va ruhiy rivojlanish\n🏃 Har kuni yangi qadam\n🏆 Orzular sari",
        "🏋️ Mashqlar orqali kuch top\n💦 Har bir ter bo‘lagi natija\n🥇 O‘z ustingda ishlash",
        "🔥 To‘xtama, rivojlanishni davom et\n💪 Har kuni kuch va motivatsiya\n🏆 G‘alaba yaqin",
        "💪 Harakat + iroda = natija\n🏃‍♂️ Sog‘lom turmush tarzi\n🥇 Eng yaxshisi sen",
        "🏋️‍♀️ Mashq bilan ruhni mustahkamlash\n💦 Harakat qil, to‘xtama\n🏆 Maqsad sari yuring",
        "🔥 Bugun terlab, ertaga g‘alaba\n💪 Har doim o‘z ustingda ishlash\n🥇 Champion mindset",
        "💪 Kuch va qat’iyat\n🏃 Har kuni yangi imkoniyat\n🏆 Natija yaqin",
        "🏋️ Mashq qilish — eng yaxshi sarmoya\n💦 Tanani rivojlantir\n🥇 Maqsad sari yuring",
        "🔥 Harakat qil, cheklovlarni yeng\n💪 Sog‘lom turmush tarzi\n🏆 G‘alaba senga",
        "💪 Har kuni o‘z ustingda ishlash\n🏃‍♀️ Kichik qadamlar — katta natija\n🥇 Orzular sari",
        "🏋️‍♂️ Sport bilan hayotini kuchaytir\n💦 Terlab, yaxshilang\n🏆 Natijaga erishing"
    ]
}

# --- ASOSIY MENYU ---
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍️ INSTAGRAM AKKOUNT SAVDO")],
        [KeyboardButton(text="💎 PREMIUM SERVISLAR")],
        [KeyboardButton(text="📝 BIO GENERATOR"), KeyboardButton(text="💰 HAMYON & PUL ISHLASH")],
        [KeyboardButton(text="🎬 REELS MASTER"), KeyboardButton(text="🚀 VIRAL HASHTAGS")],
        [KeyboardButton(text="📊 STATISTIKA"), KeyboardButton(text="👨‍💻 ADMIN SUPPORT")]
    ],
    resize_keyboard=True
)

# --- START ---
@dp.message(Command("start"))
async def start_cmd(message: types.Message, command: CommandObject):
    data = load_data()
    user_id = str(message.from_user.id)
    args = command.args

    if user_id not in data:
        data[user_id] = {"balance": 0, "referrals": 0, "name": message.from_user.full_name}
        if args and args in data and args != user_id:
            data[args]["balance"] += 500
            data[args]["referrals"] += 1
            try:
                await bot.send_message(args, f"🔔 **Bonus!**\nSizning havolangiz orqali do'stingiz qo'shildi: +500 so'm!")
            except: pass
    save_data(data)
    
    welcome = (
        f"{STARS}\n\n"
        f"        👋 **ASSALOMU ALAYKUM**\n"
        f"    🚀 **SMM UNIVERSE PRO-GA XUSH KELIBSIZ**\n\n"
        f"              {LINE}\n"
        f"  Professional SMM xizmatlari va avtomatlashtirilgan\n"
        f"  tizimlar markaziga xush kelibsiz!\n"
        f"              {LINE}\n\n"
        f"✨ **Kerakli bo'limni tanlang:**"
    )
    await message.answer(welcome, reply_markup=main_menu, parse_mode="Markdown")

# --- 🛍️ INSTAGRAM AKKOUNT SAVDO ---
@dp.message(F.text == "🛍️ INSTAGRAM AKKOUNT SAVDO")
async def insta_market_full(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📈 KANALGA O'TISH", url=CHANNEL_URL)],
        [InlineKeyboardButton(text="💰 AKKOUNT SOTISH SHARTLARI", callback_data="sell_conditions")],
        [InlineKeyboardButton(text="👨‍💻 ADMINGA BOG'LANISH", url=f"https://t.me/{ADMIN_USERNAME}")]
    ])
    text = (
        f"🛍️ **INSTAGRAM MARKETPLACE**\n"
        f"{LINE}\n"
        f"Profilingizni sotish yoki yangi akkount sotib olish\n"
        f"uchun quyidagi tugmalardan foydalaning.\n\n"
        f"👇 **Tanlang:**"
    )
    await message.answer(text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data == "sell_conditions")
async def conditions_call(callback: types.CallbackQuery):
    text = (
        f"💰 **AKKOUNT SOTISHINGIZ UCHUN TALABLAR**\n"
        f"{LINE}\n"
        f"1. Akkountingiz axvatini skrinshot tashlaysiz.\n"
        f"2. Istoriyalaringizni nech kishi ko'rishini skrinshot qilib tashlaysiz.\n"
        f"3. Login va Parol admin tekshiruvi uchun beriladi.\n"
        f"4. Akkountingiz ni holati (Settings > Account Status) skrinshot qilib tashlaysiz.\n"
        f"4. Sotuvdan tushgan pul 2 soat ichida to'lanadi.\n\n"
        f"Batafsil ma'lumot uchun adminga murojaat qiling."
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ ORQAGA", callback_data="back_to_market")]])
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data == "back_to_market")
async def back_market_call(callback: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📈 KANALGA O'TISH", url=CHANNEL_URL)],
        [InlineKeyboardButton(text="💰 AKKOUNT SOTISH SHARTLARI", callback_data="sell_conditions")],
        [InlineKeyboardButton(text="👨‍💻 ADMINGA BOG'LANISH", url=f"https://t.me/{ADMIN_USERNAME}")]
    ])
    await callback.message.edit_text(f"🛍️ **INSTAGRAM MARKETPLACE**\n{LINE}\n👇 **Tanlang:**", reply_markup=kb, parse_mode="Markdown")

# --- 💎 PREMIUM SERVISLAR ---
@dp.message(F.text == "💎 PREMIUM SERVISLAR")
async def premium_services(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✈️ Telegram (Obunachi/Like)", callback_data="serv_tg")],
        [InlineKeyboardButton(text="📸 Instagram (Obunachi/Like)", callback_data="serv_inst")],
        [InlineKeyboardButton(text="👨‍💻 ADMIN BILAN BOG'LANISH", url=f"https://t.me/{ADMIN_USERNAME}")]
    ])
    text = (
        f"💎 **PREMIUM SMM SERVISLAR**\n"
        f"{LINE}\n"
        f"Xizmatlardan foydalanish uchun quyidagi bo'limlardan birini tanlang:\n"
    )
    await message.answer(text, reply_markup=kb, parse_mode="Markdown")

# --- XIZMATLAR CALLBACKS ---
@dp.callback_query(F.data == "serv_tg")
async def tg_services(callback: types.CallbackQuery):
    text = (
        f"✈️ **TELEGRAM XIZMATLARI**\n"
        f"{LINE}\n"
        f"💡 **Hurmatli xaridor, Telegramga nakrutka urish uchun adminga yozing!**\n\n"
        f" Admin sizga nechta kerakligini ko'rib arzon narxda Xizmat ko'rsatadi!!! \n\n "
        f" Adminqa qancha obunachi kerakligini yozsangiz sizga hisoblab tashlab beradi💯 \n"

    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👨‍💻 MUROJAAT UCHUN ADMIN", url=f"https://t.me/{ADMIN_USERNAME}")],
        [InlineKeyboardButton(text="⬅️ ORQAGA", callback_data="back_to_premium")]
    ])
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data == "serv_inst")
async def inst_services(callback: types.CallbackQuery):
    text = (
        f"📸 **INSTAGRAM XIZMATLARI**\n"
        f"{LINE}\n"
        f"💡 **Hurmatli xaridor, Instagramga nakrutka urish uchun adminga yozing!**\n\n"
        f" Admin sizga nechta kerakligini ko'rib arzon narxda Xizmat ko'rsatadi!!! \n\n "
        f" Adminqa qancha obunachi kerakligini yozsangiz sizga hisoblab tashlab beradi💯 \n"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👨‍💻 MUROJAAT UCHUN ADMIN", url=f"https://t.me/{ADMIN_USERNAME}")],
        [InlineKeyboardButton(text="⬅️ ORQAGA", callback_data="back_to_premium")]
    ])
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data == "back_to_premium")
async def back_prem(callback: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✈️ Telegram (Obunachi/Like)", callback_data="serv_tg")],
        [InlineKeyboardButton(text="📸 Instagram (Obunachi/Like)", callback_data="serv_inst")],
        [InlineKeyboardButton(text="👨‍💻 ADMIN BILAN BOG'LANISH", url=f"https://t.me/{ADMIN_USERNAME}")]
    ])
    await callback.message.edit_text(f"💎 **PREMIUM SMM SERVISLAR**\n{LINE}", reply_markup=kb, parse_mode="Markdown")

# --- 📝 BIO GENERATOR ---
@dp.message(F.text == "📝 BIO GENERATOR")
async def bio_gen(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🍔 Food / Blog", callback_data="gen_food"), InlineKeyboardButton(text="👗 Fashion / Shop", callback_data="gen_shop")],
        [InlineKeyboardButton(text="🚀 SMM / Business", callback_data="gen_smm"), InlineKeyboardButton(text="⚽ Sport / Motiv", callback_data="gen_sport")],
        [InlineKeyboardButton(text="💎 SHAXSIY BIO (TEKINGA)", url=f"https://t.me/{ADMIN_USERNAME}")],
        [InlineKeyboardButton(text="🎲 RANDOM BIO", callback_data="gen_random")]
    ])
    text = (
        f"📝 **PROFESSIONAL BIO GENERATOR**\n"
        f"{LINE}\n"
        f"Tanlangan yo'nalish bo'yicha 20 tadan (jami 80 ta) kreativ variantlar!\n\n"
        f"👇 **Yo'nalishni tanlang:**"
    )
    await message.answer(text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data.startswith("gen_"))
async def handle_bio_generation(callback: types.CallbackQuery):
    category = callback.data.split("_")[1]
    
    if category == "random":
        all_lists = list(bio_data.values())
        combined = sum(all_lists, [])
        selected_bio = random.choice(combined)
    else:
        selected_bio = random.choice(bio_data.get(category, ["Variant topilmadi..."]))

    res_text = (
        f"✅ **Siz uchun tayyorlandi:**\n\n"
        f"`{selected_bio}`\n\n"
        f"{LINE}\n"
        f"💡 **Eslatma:** Maxsus, tekinga va takrorlanmas Bio yozdirish uchun adminga murojaat qiling!"
    )
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 YANA BITTA GENERATSIYA", callback_data=callback.data)],
        [InlineKeyboardButton(text="👨‍💻 ADMINGA TEKINGA BIO YOZDIRISH", url=f"https://t.me/{ADMIN_USERNAME}")],
        [InlineKeyboardButton(text="⬅️ ORQAGA", callback_data="back_to_bio_main")]
    ])
    
    await callback.message.edit_text(res_text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data == "back_to_bio_main")
async def back_bio(callback: types.CallbackQuery):
    await bio_gen(callback.message)

# --- 🎬 REELS MASTER BO'LIMI ---
@dp.message(F.text == "🎬 REELS MASTER")
async def reels_master_main(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❓ REELS NIMA?", callback_data="reels_info")],
        [InlineKeyboardButton(text="⏰ REELS QO'YISH VAQTI", callback_data="reels_time")],
        [InlineKeyboardButton(text="🛠 REELS QO'YISH QOIDALARI?", callback_data="reels_how")],
        [InlineKeyboardButton(text="👨‍💻 MASLAHAT OLISH UCHUN", url=f"https://t.me/{ADMIN_USERNAME}")]
    ])
    text = (
        f"🎬 **REELS MASTER MARKAZI**\n"
        f"{LINE}\n"
        f"Bu yerda siz reels sirlari haqida batafsil ma'lumot olishingiz mumkin.\n\n"
        f"👇 **Tugmalarni tanlang:**"
    )
    await message.answer(text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data == "reels_info")
async def reels_info_call(callback: types.CallbackQuery):
    text = (
        f"1️⃣ **REELS NIMA?**\n"
        f"{LINE}\n"
        f"Reels — Instagram va boshqa platformalarda 15–90 soniyali qisqa videolar.\n\n"
        f"🎯 **Maqsadi:** Qiziqarli, informatsion yoki viral kontent yaratish, ko‘pchilikka yetib borish.\n"
        f"⚙️ **Algoritm asosida:** Foydalanuvchilarni jalb qilish va ularni platformada uzoqroq ushlab turish."
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ ORQAGA", callback_data="back_to_reels")]])
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data == "reels_time")
async def reels_time_call(callback: types.CallbackQuery):
    text = (
        f"2️⃣ **QACHON REELS QO‘YISH KERAK?**\n"
        f"{LINE}\n"
        f"✅ **Eng yaxshi vaqtlar:**\n"
        f"📅 Hafta kunlari: 6:00–9:00 / 12:00–14:00 / 19:00–21:00\n"
        f"🏖 Dam olish kunlari: 9:00–11:00 / 18:00–20:00\n\n"
        f"💡 **Oddiy qoida:** Auditoriya eng faol bo‘lgan paytda qo‘yish reachni oshiradi."
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ ORQAGA", callback_data="back_to_reels")]])
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data == "reels_how")
async def reels_how_call(callback: types.CallbackQuery):
    text = (
        f"3️⃣ **REELSNI QANDAY QILISH KERAK?**\n"
        f"{LINE}\n"
        f"📝 **1. Kontent turi:**\n"
        f"• Qiziqarli va tez (5–10 soniyada jalb qilish)\n"
        f"• Ma’lumotli / tutorial (qisqa 'how-to')\n"
        f"• Trend + Original (trend musiqa + o‘z kreativingiz)\n\n"
        f"📸 **2. Video sifati:**\n"
        f"• Yaxshi yoritilgan va 1080p sifat\n"
        f"• Vertikal format (9:16)\n\n"
        f"🎨 **3. Matn va stickerlar:**\n"
        f"• Qisqa va aniq yozuvlar\n"
        f"• CTA: 'Save this', 'DM for info'\n"
        f"• Trend hashtaglar (5–10 ta)"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ ORQAGA", callback_data="back_to_reels")]])
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data == "back_to_reels")
async def back_reels_call(callback: types.CallbackQuery):
    await reels_master_main(callback.message)

# --- 🚀 VIRAL HASHTAGS (YANGILANGAN) ---
@dp.message(F.text == "🚀 VIRAL HASHTAGS")
async def viral_hashtags_menu(message: types.Message):
    hook_text = (
        f"🚀 **REELS VA POSTLARINGIZNI VIRAL QILING!**\n"
        f"{LINE}\n"
        f"To'g'ri hashtaglar — bu bepul reklamadir. Quyida turli sohalar uchun eng ko'p prosmotr olib keladigan hashtaglar to'plamini tayyorladik.\n\n"
        f"🔥 **Yo'nalishni tanlang va nusxalab oling:**"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⚡️ TECH & ENERGY (YAPONIYA)", callback_data="hash_tech")],
        [InlineKeyboardButton(text="🎂 SURPRISE & GIFTS", callback_data="hash_gift")],
        [InlineKeyboardButton(text="⚽️ FOOTBALL LEGENDS", callback_data="hash_football")],
        [InlineKeyboardButton(text="🏎 CARS & RACING", callback_data="hash_cars")],
        [InlineKeyboardButton(text="📸 PHOTOGRAPHY & ART", callback_data="hash_photo")]
    ])
    await message.answer(hook_text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data.startswith("hash_"))
async def show_hashtags(callback: types.CallbackQuery):
    category = callback.data.split("_")[1]
    
    hash_content = {
        "tech": "🔹 **Tech & Innovation (Japan Example):**\n\n日本利用压电瓷砖将脚步转化为电能。这些瓷砖捕捉来自你脚步的动能。当你行走时，你的重量和动作会对瓷砖产生压力。瓷砖会轻微弯曲，从而产生机械应力。瓷砖内部的压电材料将这种应力转化为电能。每一步都会产生少量电荷，而数百万步结合在一起就能产生足够的电力来驱动 LED 灯、数字显示屏和传感器。在像涩谷车站这样繁忙的地方，每天大约有 240 万个脚步为这一系统作出贡献。这些电能可以被储存或立即使用，从而减少对传统电力来源的依赖，并支持可持续的城市基础设施。这种方法将日常运动转化为实用的可再生能源 #日本 #知识 #事实 #你知道吗 #推荐 #科技 #创新 #历史 #技术 #实验 #热门 日本利用压电瓷砖将脚步转化为电能。这些瓷砖捕捉来自你脚步的动能。当你行走时，你的重量和动作会对瓷砖产生压力。瓷砖会轻微弯曲，从而产生机械应力。瓷砖内部的压电材料将这种应力转化为电能。每一步都会产生少量电荷，而数百万步结合在一起就能产生足够的电力来驱动 LED 灯、数字显示屏和传感器。在像涩谷车站这样繁忙的地方，每天大约有 240 万个脚步为这一系统作出贡献。这些电能可以被储存或立即使用，从而减少对传统电力来源的依赖，并支持可持续的城市基础设施。这种方法将日常运动转化为实用的可再生能源 #日本 #知识 #事实 #你知道吗 #推荐 #科技 #创新 #历史 #技术 #实验 #热门 日本利用压电瓷砖将脚步转化为电能。这些瓷砖捕捉来自你脚步的动能。当你行走时，你的重量和动作会对瓷砖产生压力。瓷砖会轻微弯曲，从而产生机械应力。瓷砖内部的压电材料将这种应力转化为电能。每一步都会产生少量电荷，而数百万步结合在一起就能产生足够的电力来驱动 LED 灯、数字显示屏和传感器。在像涩谷车站这样繁忙的地方，每天大约有 240 万个脚步为这一系统作出贡献。这些电能可以被储存或立即使用，从而减少对传统电力来源的依赖，并支持可持续的城市基础设施。这种方法将日常运动转化为实用的可再生能源 #日本 #知识 #事实 #你知道吗 #推荐 #科技 #创新 #历史 #技术 #实验 #热门",
        "gift": "🔹 **Surprise & Gifts (Mechanism):**\n\日本利用压电瓷砖将脚步转化为电能。这些瓷砖捕捉来自你脚步的动能。当你行走时，你的重量和动作会对瓷砖产生压力。瓷砖会轻微弯曲，从而产生机械应力。瓷砖内部的压电材料将这种应力转化为电能。每一步都会产生少量电荷，而数百万步结合在一起就能产生足够的电力来驱动 LED 灯、数字显示屏和传感器。在像涩谷车站这样繁忙的地方，每天大约有 240 万个脚步为这一系统作出贡献。这些电能可以被储存或立即使用，从而减少对传统电力来源的依赖，并支持可持续的城市基础设施。这种方法将日常运动转化为实用的可再生能源 #日本 #知识 #事实 #你知道吗 #推荐 #科技 #创新 #历史 #技术 #实验 #热门",
        "football": "🔹 **Football Legends:**\n\n#🎂要怎麼不經意的讓另一一半看到這篇文👀 儀式感滿滿🈵🔜蛋糕小熊蠟燭旋轉褸盒🕯️ 嘿~閉上眼睛～許個願吧✨ 希望你的願望會實現 （偷偷按下機關）有我幫你準備的小驚喜唷 ⚠️ 商品是蛋糕小熊機關盒 沒有附戒指💍禮物要自己準備唷  流行周邊好物推薦搜尋 ✨  玩具公仔搜尋🔍  寵物周邊搜尋 🔍  勗新商品資訊請看限時動態精選💭  下單方式🛒 🔜留言”+1；小編火速回覆你下單資訊 🔜留言”+1； 小編火速回覆你下單資訊  可自行截圖商品私訊購買‼️ 付款方式 台灣地📦匯款、ATM轉帳（可無摺）、街口支付 支持全球順豐配送🌍微信、支付寶收款  國外配送約2週左右 因天氣、不可控因素可能延誤 能接受再下單🗳️可詢問客服配送進度.",
        "photo": "🔹 **Photography & 2M Reach:**\n\n 🔥 #穿上NEYMAR球衣，你就是明星！ 🔥  就算不在球場，這件球衣也能讓你成為最閃耀的存在 ✨⚽️ 每一次穿上，都能感受到Neymar的能量與激情 💥 👕 限量版 – Neymar球衣 ✅ 輕盈舒適材質 ✅ 適合運動 & 街頭穿搭 ✅ 數量有限 — 錯過不再有！ 📸 拍照打卡、放上限時，朋友都會以為你是真球星 😎 🛒 下單方式： 👉 留言「+1」 👉 小編火速私訊回覆你 💳 付款方式：匯款 / ATM轉帳 / 街口支付 🌍 全球配送：支持微信、支付寶 🚚 國際運送約2週（因天氣或不可控因素可能延誤） ⚡️ Neymar粉絲的最佳禮物！",


    }
    
    res_text = hash_content.get(category, "Ma'lumot topilmadi.")
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ ORQAGA", callback_data="back_to_hash")]])
    await callback.message.edit_text(res_text + f"\n\n{LINE}\n☝️ Nusxalab oling va ishlatib ko'ring!", reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data == "back_to_hash")
async def back_to_hash_call(callback: types.CallbackQuery):
    await viral_hashtags_menu(callback.message)

# --- QOLGAN FUNKSIYALAR ---
@dp.message(F.text == "💰 HAMYON & PUL ISHLASH")
async def wallet(message: types.Message):
    data = load_data()
    user = data.get(str(message.from_user.id), {"balance": 0, "referrals": 0})
    ref_link = f"https://t.me/{(await bot.get_me()).username}?start={message.from_user.id}"
    await message.answer(f"💰 **BALANS**: {user['balance']} so'm\n👥 **REFERRAL**: {user['referrals']}\n🔗 Taklif havolasi:\n`{ref_link}`", parse_mode="Markdown")

@dp.message(F.text == "📊 STATISTIKA")
async def stats(message: types.Message):
    data = load_data()
    await message.answer(f"📊 BOT FOYDALANUVCHILARI: {len(data)} ta")

@dp.message(F.text == "👨‍💻 ADMIN SUPPORT")
async def support(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="✍️ ADMINGA YOZISH", url=f"https://t.me/{ADMIN_USERNAME}")]])
    await message.answer(f"👨‍💻 Adminga savol yoki shikoyatingiz bo'lsa murojat qiling!", reply_markup=kb)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())