height = int(input("Введите рост: "))
weight = int(input("Введите  вес: "))
steps = int(input("Введите количество шагов: "))
time = int(input("Введите время: "))

step_length = height / 4 + 0.37
distance = steps * step_length / 1000
speed = distance / time / 60

energy = 0.035 * weight + (speed ** 2 / height) * 0.029 * weight

print(distance, "км,", energy, "ккал/мин")

if (distance < 2):
    print("Старайсе больше, у теюя всё получится!")
elif (distance < 4):
    print("Неплохо, но можно лучше!")
elif (distance > 4):
    print("Отличная тренировка, ты молодец!")
