# 최대로 할인 받기

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 최대할인은 가장비싼걸 가장 큰 할인율로 받으면 됨.

def get_max_discounted_price(prices, coupons):
    coupons.sort(reverse=True)
    prices.sort(reverse=True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print(int(get_max_discounted_price(shop_prices, user_coupons)))  # 926000 이 나와야 합니다.