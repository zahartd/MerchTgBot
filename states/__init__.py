from .add_to_basket import AddToBasket
from .edit_basket import EditBasketDeletePos, EditBasketEditPos
from .checkout import Checkout
from .ask_question import AskQuestion
from .report_bug import ReportBug
from .mailing import Mailing
from .new_item import NewItem

states_list: list = [AddToBasket, EditBasketDeletePos, EditBasketDeletePos, Checkout, AskQuestion, ReportBug, Mailing,
                     NewItem]
states_dict: dict = {
    'AddToBasket': AddToBasket,
    'EditBasketDeletePos': EditBasketDeletePos,
    'EditBasketEditPos': EditBasketEditPos,
    'Checkout': Checkout,
    'AskQuestion': AskQuestion,
    'ReportBug': ReportBug,
    'Mailing': Mailing,
    'NewItem': NewItem
}
