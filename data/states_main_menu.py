from handlers.users import show_main_menu, show_goods_basket, show_catalog

states_main_menu: dict = {
    'AskQuestion': show_main_menu,
    'ReportBug': show_main_menu,
    'Checkout': show_goods_basket,
    'AddToBasket': show_catalog,
    'EditBasket': show_goods_basket
}
