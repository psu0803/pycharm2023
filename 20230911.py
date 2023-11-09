from typing import List

data = []

for i in range(5):
    while True:
            value = int(input(f"입력 0 부터 100사이: "))
            if 0 <= value <= 100:
                data.append(value)
                break
            else:
                print("0부터 100사이로 다시시도하세요.")

avg = sum(data)/len(data)

gavg: list[int] = []

for value in data:
    if value > avg and len(gavg) < 5:
        gavg.append(value)

print("입력값:", data)
print("평균:", avg)
print("5개의 평균보다큰:", gavg)