n = int(input())
numbers = list(map(int, input().split()))
digits = []
for i in numbers:
    temp = list(map(int, str(i)))
    digits.append((max(temp)*11 + min(temp)*7) % 100)
counts = [0]*10
counts2 = [0]*10
for i in range(0, len(digits), 2):
    counts[(digits[i]//10)] += 1
for i in range(1, len(digits), 2):
    counts2[(digits[i]//10)] += 1
ans = 0
for i in range(0, len(digits)):
    if counts[i] > 2 or counts2[i] > 2:
        ans += 2
    elif counts[i] == 2 or counts2[i] == 2:
        ans += 1
print(ans, end="")