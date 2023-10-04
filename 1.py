N = int(input("Введіть кількість елементів масиву: "))
while N < 1:
    N = (input("Введіть кількість елементів масиву(кількість елементів не може бути менше одного): "))
print("Введіть", N, "елементів масиву:")
arr = [float(input()) for _ in range(N)]
S = 0
kil = 0
for i in range(N):
    if arr[i] > 0:
        S = S + arr[i]
        kil += 1
S = S / kil
print("Масив: ", arr)
print("Середнє арифметичне даних масиву: ", S)