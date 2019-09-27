import operator
#making a method that counts the number of words and puts them in an order

#getting names from user
name_of_person1 = input('Please enter the proper full name of person1: ') + ':' + ' ' 
name_of_person2 = input('Please enter the proper full name of person2: ') + ':' + ' ' 

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    dela = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    return dela[0]

  
  
#opening up the data file
with open('datasheet.txt', 'r', encoding="utf-8") as file:
  data = file.read().lower()

data = data.splitlines()


#making lists for the data storage
person1 = []
person2 = []


#for loop to get the values for person1
for i in range(10000):
  try:
    person1.append(data[i].split(name_of_person1.lower())[1].split('\n')[0])
  except:
    pass

#for loop to get the values for person2
for i in range(10000):
  try:
    person2.append(data[i].split(name_of_person2.lower())[1].split('\n')[0])
  except:
    pass

#Printing out the most used word with the number of times for person1
dummy_person1 =''
for i in range(len(person1)):
  dummy_person1 = str(dummy_person1) + ' ' + str(person1[i])
  
print('The most used word and count for person1 is', word_count(dummy_person1))

#Printing out the most used word with the number of times for person2
dummy_person2 =''
for i in range(len(person2)):
  dummy_person2 = str(dummy_person2) + ' ' + str(person2[i])
  
print('The most used word and count for person2 is', word_count(dummy_person2))
