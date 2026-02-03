from tools import get_ticket_price


def handle_tool_call(tool_call):
    
    arguments = dict(tool_call.args)
    city = arguments.get('destination_city')
    
    price = get_ticket_price(city)
    
    return price, city