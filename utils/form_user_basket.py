from utils.db_api.db_commands import get_item
from utils.db_api.schemas.items import Item


# Return user basket to commit it to database
async def form_user_basket(state_data, basket_name: list[str], basket_count: list[int], basket_item_price: list[int],
                           total_price: int) -> (list, list, int):
    # Get Item
    item: Item = await get_item(state_data['item_id'])

    # If it yet in basket -> update count
    if state_data['item_name'] in basket_name:
        item_ind = basket_name.index(state_data['item_name'])
        basket_count[item_ind] += int(state_data['item_count'])
    else:  # Else add new
        basket_name.append(state_data['item_name'])
        basket_count.append(int(state_data['item_count']))
        basket_item_price.append(item.price)

    # Update total price
    total_price += item.price * int(state_data['item_count'])

    return basket_name, basket_count, basket_item_price, total_price
