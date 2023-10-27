from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


# Show information about organisation
@dp.message_handler(text='Информация')
@dp.message_handler(text='Информация ℹ')
@dp.message_handler(Command('info'))
async def bot_info(message: types.Message):
    await message.answer(text=f'Информация о <Название организации скрыто>: ')
    await message.answer(
        text=f'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Parturient montes nascetur ridiculus mus mauris. Risus pretium quam vulputate dignissim suspendisse in. Et malesuada fames ac turpis egestas maecenas pharetra. Velit ut tortor pretium viverra. Ut eu sem integer vitae. Nascetur ridiculus mus mauris vitae. At consectetur lorem donec massa. Faucibus interdum posuere lorem ipsum. Viverra ipsum nunc aliquet bibendum enim facilisis gravida neque. Arcu bibendum at varius vel pharetra vel turpis nunc eget. Sit amet consectetur adipiscing elit. Felis bibendum ut tristique et. Diam sollicitudin tempor id eu nisl nunc. Vestibulum lorem sed risus ultricies tristique. Quis hendrerit dolor magna eget est lorem.')
    await message.answer(
        text=f'Pellentesque habitant morbi tristique senectus et. Nisl purus in mollis nunc sed. Odio euismod lacinia at quis. Leo vel fringilla est ullamcorper. Nullam ac tortor vitae purus faucibus. A scelerisque purus semper eget duis at. Congue eu consequat ac felis donec. Quis enim lobortis scelerisque fermentum dui faucibus in ornare. Est ante in nibh mauris cursus mattis molestie a.')
    await message.answer(
        text=f'Elit pellentesque habitant morbi tristique senectus et netus et. Id ornare arcu odio ut sem. Maecenas ultricies mi eget mauris pharetra et ultrices neque ornare. Egestas diam in arcu cursus euismod quis viverra. Ante in nibh mauris cursus mattis molestie a. Aliquam faucibus purus in massa tempor nec. Aenean et tortor at risus viverra adipiscing at. Imperdiet proin fermentum leo vel orci. Suspendisse ultrices gravida dictum fusce ut placerat. Volutpat est velit egestas dui id ornare. Amet facilisis magna etiam tempor.  ')
    await message.answer(text=f'Наши контакты: \n'
                              f'Сайт: \n'
                              f'Вконтакте: https://vk.com/ \n'
                              f'Тик ток: https://vm.tiktok.com/')
