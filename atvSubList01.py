
# PET SHOP DATABASE

def line():
    print('-' * 20)


from numpy import mean

qntAnimals = 6
# qntAnimals = you can put any number that you want to
animals = []
animalsDisp = ('DOG', 'CAT', 'BIRD', 'FISH', 'RABBIT', 'BUNNY')

# Data Entry
for i in range(qntAnimals):
    print('\033[7;36;40mEnter the animal info:\033[m')
    name = str(input('\033[36mName: ')).strip().upper()
    age = int(input('\033[36mAge: '))
    while (age < 0) or (age > 100):
        age = int(input('\033[31mEnter a valid age: '))
    types = str(input('\033[36mType: ')).strip().upper()
    while types not in animalsDisp:
        types = str(input('\033[31mEnter a type that is available in database: ')).strip().upper()
    animals.append([name, age, types])

line()

# Rabbits Quantity
qntRabbit = 0
for i in range(qntAnimals):
    if animals[i][2] == 'RABBIT' or animals[i][2] == 'BUNNY':
        qntRabbit += 1
print(f'The quantity of registered rabbits is: {qntRabbit}')

line()

# Cat names
catsName = []
for i in range(qntAnimals):
    if animals[i][2] == 'CAT':
        cat = animals[i][0]
        catsName.append(cat)
print(f'''All registered cat names: 
{catsName}.''')

line()

# Birds ages
birdsAge = []
for i in range(qntAnimals):
    if animals[i][2] == 'BIRD':
        b = animals[i][1]
        birdsAge.append(b)
print(f'''All registered bird ages:
{birdsAge}''')

line()

# Animals with less than 2 years names:
animalsTwoYears = []
for i in range(qntAnimals):
    if animals[i][1] < 2:
        twoYears = animals[i][0]
        animalsTwoYears.append(twoYears)
print(f'''Registered animals with less than two years:
{animalsTwoYears}''')

line()

# Dogs ages mean
dogsAge = []
for i in range(qntAnimals):
    if animals[i][2] == 'DOG':
        dog = animals[i][1]
        dogsAge.append(dog)

meanAgeDog = mean(dogsAge)
print(f'The average dog age is {meanAgeDog:.0f}.')

line()

# Search animal by type
questionType = 'YES'
while questionType == 'YES':
    questionType = str(input('''\033[7;33;40mDo you want to make a search\033[m
\033[7;33;40mamong the registered animals?\033[m ''')).strip().upper()
    if questionType == 'YES':
        typeAnimal = str(input('''\033[7;36;40mEnter the animal type\033[m 
\033[7;36;40mthat you want to search:\033[m ''')).strip().upper()
        for i in range(qntAnimals):
            if animals[i][2] == typeAnimal:
                print(f'Name: {animals[i][0]}; Age: {animals[i][1]}')
    else:
        break
