from utils.db_api.db_commands import add_item


# Add to database goods
async def add_items():
    await add_item(id=1, name='Футболка <НОС>', price=700,
                   photos=['AgACAgIAAxkBAAIUomAAAZCd1EOi07D2leVhwPIpxiWU6gAC568xG3uHAUgh62ynvi5ABuCxlJcuAAMBAAMCAAN4AAP0qAUAAR4E',
                           'AgACAgIAAxkBAAIUpGAAAZCzZGtHp9230lKKMUf6-KRyUQAC6K8xG3uHAUg-r2AVKBv8xF0fIpsuAAMBAAMCAAN4AAPbTQEAAR4E',
                           'AgACAgIAAxkBAAIUpmAAAZDaYZqTybvp4EXPdlAIirh4AgAC6a8xG3uHAUgAAe18dqkGGrCIvymbLgADAQADAgADeAAD5VQBAAEeBA'],
                   emodji='👕',
                   category_name='Одежда', category_code='1clothes')
    await add_item(id=2, name='Поло <НОС>', price=700,
                   photos=['AgACAgIAAxkBAAIUqGAAAZEZ9s0OcqfaSliv3fy9th4ZXAAC668xG3uHAUjlORnhL2I_jYTeYZouAAMBAAMCAAN4AAP4cQMAAR4E',
                           'AgACAgIAAxkBAAIUqmAAAZEx572BdTy76Prle95Yipkz9AAC7K8xG3uHAUite8rtlbs-0sfnUZguAAMBAAMCAAN4AAOCnAUAAR4E',
                           'AgACAgIAAxkBAAIUrGAAAZFGuyk4WKOMLqwNOSPhNY4Y1QAC7a8xG3uHAUiIkSDdKB01IslQVZkuAAMBAAMCAAN4AAMMagMAAR4E',
                           'AgACAgIAAxkBAAIUrmAAAZFT5op18CFKfU3_b6SZmelKEAAC7q8xG3uHAUgAAXJMB_50RT8yUy6bLgADAQADAgADeAADLjMBAAEeBA'],
                   emodji='🥼',
                   category_name='Одежда', category_code='1clothes')
    await add_item(id=3, name='Значок <НОС>', price=60,
                   photos=['AgACAgIAAxkBAAIUsGAAAZFldg0ZB1BReO3ST9TAJvO-5gAC768xG3uHAUiWMNx1GXzvg6zH0pouAAMBAAMCAANtAAOrfQACHgQ',
                           'AgACAgIAAxkBAAIUsmAAAZF2CJbUID_M_GMoSF96JoaDlQAC8K8xG3uHAUgd4Rd4cswh3RxxU5guAAMBAAMCAAN4AAP7lwUAAR4E',
                           'AgACAgIAAxkBAAIUtGAAAZGROs0KZ4N7sQl_uQmr-LygIQAC8a8xG3uHAUgKaOA-YFmZS5chpZYuAAMBAAMCAANtAANHiAYAAR4E'],
                   emodji='😀',
                   category_name='Другое', category_code='3other')
    await add_item(id=4, name='Браслет <НОС>', price=45,
                   photos=['AgACAgIAAxkBAAIS1V__OGNxVSCNL5R5SwXsKBIJrcZ8AAK4sDEbJx74S815NXNRlSZdIz_wly4AAwEAAwIAA3gAA--BBQABHgQ'],
                   emodji='💍',
                   category_name='Другое', category_code='3other')
    await add_item(id=5, name='Флаг <НОС> (большой)', price=600,
                   photos=['AgACAgIAAxkBAAIUtmAAAZG5UrQ6QkX9fRLDPn8CrWqXFgAC8q8xG3uHAUigP0PEJZVJ9f6OoJYuAAMBAAMCAAN4AAOoiwYAAR4E',
                           'AgACAgIAAxkBAAIUuGAAAZHJ3xxD3xmcI6ZlByLS2NRoQgAC868xG3uHAUiGZJK-_ylui8UD2ZYuAAMBAAMCAAN4AAOESQYAAR4E',
                           'AgACAgIAAxkBAAIUumAAAZHg9JYN-mMUl_4Firn3Dr5ilAAC9K8xG3uHAUigqCfkrd7b8Xga55cuAAMBAAMCAAN4AAPjqwUAAR4E'],
                   emodji='🏁',
                   category_name='Другое', category_code='3other')
    await add_item(id=6, name='Блокнот <НОС>', price=55,
                   photos=['AgACAgIAAxkBAAIUvGAAAZH6j29096luU0SwKJ2_0fAz0AAC9a8xG3uHAUgTG5FRtCzRTJQPx5cuAAMBAAMCAAN4AANqhAUAAR4E',
                           'AgACAgIAAxkBAAIUvmAAAZISltvwcEAL_jOMq9QQDLAQlAAC9q8xG3uHAUixsM768eBshk8a55cuAAMBAAMCAAN4AAMCpwUAAR4E'],
                   emodji='📔',
                   category_name='Другое', category_code='3other')
    await add_item(id=7, name='Стенд информационный <НОС>', price=1200,
                   photos=['AgACAgIAAxkBAAIS21__OPC11O7duK-pr7SlK9H69Ps6AAK4sDEbJx4AAUjXCuadGlIuL_md6JcuAAMBAAMCAAN4AAMznwUAAR4E'], emodji='💼',
                   category_name='Стенды', category_code='2stands')
    await add_item(id=8, name='Стенд обычный <НОС>', price=700,
                   photos=['AgACAgIAAxkBAAIS21__OPC11O7duK-pr7SlK9H69Ps6AAK4sDEbJx4AAUjXCuadGlIuL_md6JcuAAMBAAMCAAN4AAMznwUAAR4E'], emodji='💼',
                   category_name='Стенды', category_code='2stands')
    await add_item(id=9, name='Стенд-паук <НОС>', price=1500,
                   photos=['AgACAgIAAxkBAAIS21__OPC11O7duK-pr7SlK9H69Ps6AAK4sDEbJx4AAUjXCuadGlIuL_md6JcuAAMBAAMCAAN4AAMznwUAAR4E'], emodji='💼',
                   category_name='Стенды', category_code='2stands')
