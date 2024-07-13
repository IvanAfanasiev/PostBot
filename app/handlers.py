import asyncio
from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.filters import Command

import app.keyboards as kb

router = Router()

PHOTOS_ID = []
new_message = True
TARGET_CHANNEL_ID = '@example_target_id'
SOURCE_CHANNEL_ID = '@example_source_id'
ADMIN_PASSWORD = 'Password'

POST_DELAY = 120 * 60 # in seconds

last_message_indx = 0
wait = True

class Login(StatesGroup):
    password = State()


@router.message(Command('start'))
async def send_welcome(message: Message):
    await message.answer("Hello, "
                        +"{user}!\nLog in, please".format(user=message.from_user.username)
                        ,
                        reply_markup=kb.welcome_panel
                        )


@router.callback_query(F.data == 'stop posting') 
async def stop_posting(callback: CallbackQuery):
    await callback.answer('work stopped (=')
    global wait
    wait = False


@router.callback_query(F.data == 'start posting') 
async def start_posting(callback: CallbackQuery):
    global last_message_indx
    # to avoid circular import
    from main import bot
    can_send = False
    last_indx = 0
    global wait
    await callback.answer('work started (=')
    while wait:
        can_send = False
        if wait == True:
            while can_send == False:
                last_message_indx+=1
                try:
                    await bot.copy_message(TARGET_CHANNEL_ID, SOURCE_CHANNEL_ID, last_message_indx)
                    last_indx = last_message_indx
                    await callback.message.answer("posted {indx}".format(indx=last_message_indx))
                    # delete the message in the source channel if it necessary
                    # await bot.delete_message(SOURCE_CHANNEL_ID, i)
                    # await message.answer("deleted {indx}".format(indx=i))
                    can_send = True
                except:
                    # if next 100 iterations return empty
                    if ((last_message_indx - last_indx)>100):
                        await callback.message.answer("The posts are over")
                        wait = False
                        break 
                    continue 
        # send message every 2 hours
        await asyncio.sleep(POST_DELAY)


# F.data looks at the callback from the buttons in the bot message
@router.callback_query(F.data == 'post now') 
async def make_post_now(callback: CallbackQuery):
    global last_message_indx
    # to avoid circular import
    from main import bot
    can_send = False
    last_indx = 0
    await callback.answer('posted! (=')
    while can_send == False:
        last_message_indx+=1
        try:
            await bot.copy_message(TARGET_CHANNEL_ID, SOURCE_CHANNEL_ID, last_message_indx)
            last_indx = last_message_indx
            await callback.message.answer("posted {indx}".format(indx=last_message_indx))
            # delete the message in the source channel if it necessary
            # await bot.delete_message(SOURCE_CHANNEL_ID, i)
            # await message.answer("deleted {indx}".format(indx=i))
            can_send = True
        except:
            # if next 100 iterations return empty
            if ((last_message_indx - last_indx)>100):
                await callback.message.answer("The posts are over")
                wait = False
                break 
            continue 


# F.text check the text in the user message
@router.callback_query(F.data == 'login') 
async def login(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Login.password)
    await callback.answer('Enter the password', show_alert=False)
    await callback.message.answer('Enter the password')


@router.message(Login.password)
async def check_password(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    if data['password'] != ADMIN_PASSWORD:
        await message.answer('Invalid password 😜')
        return
    await state.clear()
    await message.reply('Correct password', reply_markup=kb.main_panel)


# F.photo looks if the message from the user contains a photo
@router.message(F.photo)
async def get_photos(message: Message):
    global new_message
    if new_message:
        PHOTOS_ID.clear()
    len = message.photo.__len__() - 1
    media_group = MediaGroupBuilder(caption="")
    PHOTOS_ID.append(message.photo[-1].file_id)
    if (PHOTOS_ID.__len__()) != len:
        new_message = False
        return
    for photo in PHOTOS_ID:
        media_group.add_photo(photo)
    new_message = True
    await message.answer_media_group(media=media_group.build())
