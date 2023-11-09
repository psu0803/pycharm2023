data: list[int] = []

i = 0
while i < 5:
            value = int(input(f"입력 0 부터 100사이: "))
            if 0 <= value <= 100:
                data.append(value)
                i += 1
                break
            else:
                print("0부터 100사이로 다시 시도 하세요.")

avg = sum(data)/len(data)

gavg: list[int] = []

i = 0
while i < len(data) and len(gavg) < 5:
    if data[i] > avg:
        gavg.append(data[i])
    i += 1

while len(gavg) < 5:
    min_value = min(data)
    data.remove(min_value)
    gavg.append(min_value)

print("입력값:", data)
print("평균:", avg)
print("5개의 평균 보다 큰:", gavg)