from .add_to_basket import AddToBasket
from .edit_basket import EditBasketDeletePos, EditBasketEditPos
from .checkout import Checkout
from .ask_question import AskQuestion
from .report_bug import ReportBug

states_list: list = [AddToBasket, EditBasketDeletePos, EditBasketDeletePos, Checkout, AskQuestion, ReportBug]
states_dict: dict = {
    'AddToBasket': AddToBasket,
    'EditBasketDeletePos': EditBasketDeletePos,
    'EditBasketEditPos': EditBasketEditPos,
    'Checkout': Checkout,
    'AskQuestion': AskQuestion,
    'ReportBug': ReportBug
}
