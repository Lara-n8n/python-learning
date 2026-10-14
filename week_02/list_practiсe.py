names = ["Asel", "Aigerim", "Erlan", "Baks", "Simba", "Taison", "Forti", "Beka"]
scores = [71, 35, 51, 80, 98, 97, 92, 95]
threshold = 70

certificate = 0
references = 0

for i in range(len(names)):
    name = names[i]
    score = scores[i]

    if score >= threshold:
        print(f"{name}, ваш балл - {score}, ваш сертификат готов!")
        certificate = certificate + 1
    else:
        print(f"{name}, {score} баллов — вам выдана справка об участии.")
        references = references + 1

print(f"Сертификатов: {certificate}, справок: {references}")