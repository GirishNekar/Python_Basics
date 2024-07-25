

import random

def count_random(coupon_num):
    count = 0
    distinct_coupons = set(coupon_num) 

    while distinct_coupons:
        random_coupon = random.randint(1, 100)  
        if random_coupon in distinct_coupons:
            distinct_coupons.remove(random_coupon)  
        count += 1  

    return count


num = int(input("Enter the number of distinct coupon numbers: "))
coupon_num = []


for _ in range(num):
    while True:
        x = int(input("Enter a coupon number > 0 and <= 100: "))
        if 0 < x <= 100:
            coupon_num.append(x)
            break
        else:
            print("Please enter a valid coupon number between 1 and 100.")


print(count_random(coupon_num))

