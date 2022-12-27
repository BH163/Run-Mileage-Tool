def main():
    task = 0
    while(task != 3):
        task = int(input("1)Establish weekly running goals\n2)Update weekly mileage\n3)Exit\n\nEnter selection: "))
        if task == 1:
            weeklyGoals()
        elif task == 2:
            mileageTracker()
        elif task == 3:
            break
   


def weeklyGoals():
    startMileage = int(input("Enter your usual weekly mileage: "))
    if (startMileage <= 0) :
        startMileage = 1
    weeklyGoal = int(input("Enter your weekly mileage goal: "))
    
    fileName = input("Enter a file name to save to: ")
    weeklyMiles = startMileage
    weekCount = 1
    
    fileLinesList = []
    
    while(weeklyMiles < weeklyGoal):
        fileLinesList.append([f'{(str(weekCount) + ":"):<4}', str(f'{weeklyMiles:.2f} {0:>5} \n')])
        weeklyMiles = weeklyMiles * 1.1
        weekCount += 1
    fileLinesList.append([f'{(str(weekCount) + ":"):<4}', str(f'{weeklyMiles:.2f} {0:>5} \n')])
    writeFile(fileLinesList, fileName)
    print("\n")
    

def writeFile(fileLinesList,fileName):
    file = open(fileName, 'w')
    file.writelines(f'{"Wk":<2} {"Goals":>6} {"Ran":>6}'"\n"f'{"-" * 18 }'"\n")
    for line in fileLinesList:
        file.writelines(line)
    file.close()

def mileageTracker():
    file = input("Enter the file name to update: ")
    fileName = file
    file = open(file)
    fileLines = file.readlines()
    print()
    # display file for user
    for line in fileLines:
        print(line.rstrip('\n'))
    print()
    fileLines = fileLines[2:]
    weekUpdate = input("Enter the week number you would like to update: ")
    addMiles = input("How many miles did you run: ")
    lineEdited = []
    for line in fileLines:
        line = line.split()
        if line[0] == (weekUpdate + ':'):
            lineEdited = [(f'{(weekUpdate + ":"):<4}'), (line[1]), (f'{int(line[2]) + int(addMiles):>6} \n')]
            fileLines[int(weekUpdate)-1] = lineEdited
    file.close()    
    writeFile(fileLines, fileName)
    print()
    
    
    




main()
