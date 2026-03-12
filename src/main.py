from data.rv import data_entry 
from calculate.cc import calculate_totals

client, quantity, unit_price, is_vip = data_entry()

subtotal, discount, total = calculate_totals(quantity, unit_price, is_vip)

print("\n--- Sales Summary ---")
print(f"Customer: {client}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")

if is_vip:
        print(f"VIP discount: ${discount:.2f}")

print(f"Total to pay: ${total:.2f}")

