money1 = 10000
money2 = 0
bag = []

while money2 < money1:
    item_name = input("상품명: ")
    item_price = int(input("가격: "))
    bag.append((item_name, item_price))
    money2 += item_price

remaining_money = money1 - money2

print("총 지출 금액:", money2)
print("남은 돈:", remaining_money)

