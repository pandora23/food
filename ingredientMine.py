
import csv

#read in ingredient ontology

flavorTags = []
ingredients  = {}
ingredientSets = {}
interactionSets = {}


reader = None

with open('Ingredients.csv') as ingredientsCsv:
    reader = csv.reader(ingredientsCsv, delimiter=' ', quotechar='|')
    flavorTags = reader.next()[0].split(',')[1:]
    print(flavorTags)
    for row in reader:
        name = row[0].split(',')[0]
        features = row[0].split(',')[1:]
        ingredients.update({name: features})


#read in ingredient sets for recipes
with open('recipes.txt') as recipes:
    class1 = ''
    name = ''
    ingreds = []
    for line in recipes:
        #done = False
        if('GOOD' in line):
            class1 = 'GOOD'
            ingreds = ['GOOD']
            print(line)
        elif('BAD' in line):
            class1 = 'BAD'
            ingreds = ['BAD']
        elif('DONE' in line):
            print('f')
            ingredientSets.update({name: ingreds})
        elif(line[0].isupper()):
            print(line)
            name = line[:-1]
        else:
            ingreds.append(line[1:-1])
            
            
#get ingredient interactions
potentialInteractions = []
for tag in flavorTags:
    for tag2 in flavorTags:
        interactionLabel = tag + '' + tag2
        potentialInteractions.append(interactionLabel)



trainingData = []
        
for recipe in ingredientSets:
    
    interactions = []
    print(recipe)
    print('----------------------------------------------------------------------------')
    interactionSet = []
    for i in range(len(potentialInteractions)):
        interactionSet.append(0)
    for ingredient in ingredientSets[recipe][1:]:
        for ingredient2 in ingredientSets[recipe][1:]:
            print(ingredient, ingredient2)
            flavorCount = 0;
            
            for val in ingredients[ingredient]:
                flavorCount2 = 0;
                for val2 in ingredients[ingredient2]:
                    if(val == '1' and val2 == '1'):
                        #print(val,val2)
                        print(flavorTags[flavorCount], flavorTags[flavorCount2])
                        #print(potentialInteractions.index(flavorTags[flavorCount]+''+flavorTags[flavorCount2]))
                        #print(potentialInteractions[potentialInteractions.index(flavorTags[flavorCount]+''+flavorTags[flavorCount2])])
                        interactionSet[potentialInteractions.index(flavorTags[flavorCount]+''+flavorTags[flavorCount2])] = 1
                    flavorCount2 = flavorCount2+1
                flavorCount = flavorCount+1

    interactionSet.append(ingredientSets[recipe][0])
    interactionSets.update({recipe: interactionSet})
    
    trainingData.append(interactionSet)

print(trainingData)


with open('foodData1.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    labels = potentialInteractions
    labels.append('CLASS1')
    labels.append('NAME1')
    print(labels)
    writer.writerow(labels)

    for recipe in interactionSets:
        newRow = interactionSets[recipe]
        newRow = newRow + [recipe]
        writer.writerow(newRow)




            
    

 



			

        
