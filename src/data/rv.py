# Data entry
def data_entry():
    client = input("Name of client: ")
    quantity = int(input("Quantity: "))
    unit_price = float(input("Unit price: "))
    is_vip = input("¿is client VIP? (s/n): ").lower() == 's'
    return client, quantity, unit_price, is_vip
 