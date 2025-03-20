import random
#1

text = input("Введите слово или предложение: ")

vowels = "aeiouüöõäAEIOUÜÖÕÄ"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
punctuation = ".,!?;:-\"'()"

vowel_count = 0
consonant_count = 0
space_count = 0
punctuation_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1
    elif char in punctuation:
        punctuation_count += 1
    elif char == " ":
        space_count += 1

print(f"Гласных: {vowel_count}")
print(f"Согласных: {consonant_count}")
print(f"Пробелов: {space_count}")
print(f"Знаков препинания: {punctuation_count}")

#2

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print("*" * number)

#9 nimi kontroll

while True:
    name = input("Type your name ")
    if name.isalpha():
        break
    else:
        print("Only letters!")
name = name.capitalize()
vowels1 = "aeiouüöõäAEIOUÜÖÕÄ"
consonants1 = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vowel_count1 = 0
consonant_count1 = 0
for char1 in name:
    if char1 in vowels1:
        vowel_count1 += 1
    elif char1 in consonants1:
        consonant_count1 += 1
print(f"Hello {name}! There are {vowel_count1} vowel letters and {consonant_count1} consonant letters")
print(f"There are {len(name)} letters in this name")
name1 = sorted(set(name))
print(f"Letters in order {name1}")

#12 Koostage loend 10 juhuslikust numbrist 1 kuni 100. Kirjutage programm, mis vahetab selle loendi miinimaalse ja maksimaalse elemendid

numbers = [random.randint(1, 100) for _ in range(10)]
print("Исходный список:", numbers)
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
print("Измененный список:", numbers)

#16

answers = ["Jah, kindlasti!", "Jah!", "Võib-olla!", "Ei!"]
print("Tere! Sa võid küsida minult jah/ei küsimuse.")
input("Esita oma küsimus: ")
response = random.choice(answers)
print("Minu vastus on:", response)

#11

vowels2 = "aeiouüöõäAEIOUÜÖÕÄbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
character_list = []
multiplied_list = []
n=10
for i in range(n):
    char = vowels2[i]
    character_list.append(char)
    multiplied_list.append(char * (i + 1))
print("Character list:", character_list)
print("Multiplied list:", multiplied_list)



#14 pealinnad

capitals = ["Tallinn", "Riga","Vilnius", "Helsinki", "Stockholm", "Oslo", "Kopenhagen", "Varsava", "Berlin", "Paris", "Amsterdam", "London", "Milan", "Kiev", "Minsk", "Bratislava"]
for item in capitals:
    print(item)
sorted_capitals = sorted(capitals)
print("A-x order")
for item in sorted_capitals:
    print(item)
capitals.append(input("Add one more Capital "))
capitals.append(input("Add one more Capital "))
sorted_capitals = sorted(capitals)
print(f"Meie järjendis on {len(sorted_capitals)} pealinnad")
for capitals1, item in enumerate(sorted_capitals, start=1):
    print(f"{capitals1}. {item}")

#7 sortereemine

megalist = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), ]
megalist_sort = sorted(megalist) 
print("Kasvavalt")
for item in megalist_sort:
    print(item)
print("Kahanevalt")
megalist_reverse = sorted(megalist, reverse=True)
for item in megalist_reverse:
    print(item)

#5 vahetus

