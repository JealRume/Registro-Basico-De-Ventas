# Sales calculations

def calculate_totals(quantity, unit_price, is_vip):
    subtotal = quantity * unit_price
    discount = 0.0

    if is_vip:
        discount = subtotal * 0.1  # 10% discount for VIP customers
    total = subtotal - discount

    return subtotal, discount, total

