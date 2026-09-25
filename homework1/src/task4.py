# Task 4: Functions and Duck Typing

# calculate the discount, for example, can take in float or int
def calculate_discount(price, discount):
    temp = (price*discount) / 100
    total = price - temp
    
    return round(total, 2)

def main():
    original_price = 56.89
    discount = 10.6
    final_price = calculate_discount(original_price, discount)    
    print(f"original price: ${original_price:.2f}")
    print(f"discount: {discount}% off")
    print(f"final price: ${final_price:.2f}")

if __name__ == "__main__":
    main()