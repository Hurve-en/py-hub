from collections import deque
import json
# import spacy 

items = ["pen" , "book", "pen"]
print(items.index("pen"))
print(items.count("pen"))
items.remove("pen")
last = items.pop()
print(items , last)

print("===================================")

values = [10,20,30,40,50]
print(values[2:3])
print(values[:2])
print(values[3:])
print(values[::3])
print(values[::-2])

print("===================================")

tasks = ["Read", "Test", "Submit"]
tasks[1:2] = ["Code", "Test"]
del tasks[3:]
print(tasks)

print("===================================")

#Practice: A task list

task_list = ["Read", "Code", "Submit"]
task_list.insert(2, "Test")
task_list[0] = "Review"
print(task_list[:2])
task_list.pop()
print(task_list)

print("===================================")

#Stacks: last in, first out
stack = []
stack.append("Page A")
stack.append("Page B")
stack.append("Page C")
print(stack)
stack.pop()
print(stack)

print("===================================")
#Queues: first in, first out
queue = deque(["Ana" , "Ben"])
queue.append("Cara")
print(queue.popleft())

print(list(queue))

print("===================================")
#Tracing a phrase stack

stack = ["a", "useful", "tool"]
phrase = ""
while stack: 
    phrase = stack.pop() + " " + phrase

    print(phrase.strip())

print("===================================")
#List comprehensions
scores = [70,85,90]

passed = []
for score in scores:
    if score >= 75:
        passed.append(score)

        passed = [ s for s in scores if s >= 75]

        print(passed)

print("===================================")
#Nested comprehensions

#The secret is that Python does not read list comprehensions from left to right. It reads them from the inside-out (or right-to-left).
# Then python looks left and split it
sentences = ["Data matters", "Python helps"]
word_lists = [
    [word.lower() for word in sentence.split()] 
    for sentence in sentences
    # Python read this section first
]

print(word_lists)
    
print("===================================")
#NLP demonstration

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("A useful tool supports students.")
# chunks = [chunk.text for chunk in doc.noun_chunks]
# print(chunks)

print("NLP DEMONSTRATION")

print("===================================")
#Tuples: a fixed sequence

location = (10.3244, 123.4543)
latitude, longitude = location
print(latitude)
print(longitude)

print("===================================")
#What immutability means

record = ("Ana", 20)
# record [1] = 21 Error

record = (record[0] , 21)
print(record)

print("===================================")
#A list of tuples

times = ["8:00", "9:00"]
tasks = ["Review", "Practice"]
schedule = [(t, task) for t, task in zip(times,tasks)]
print(schedule[1])
print(schedule[0])
print(schedule[0][0])
print(schedule[1][1])
print(schedule[1][0])
print(schedule[0][1])

print("===================================")

sched = [("08:00", "Review"), ("09:00", "Practice")]
sched[1] = ("9:30", sched[1][1])

print(sched)

print("===================================")
#Dictionaries

student = {"name": "Ana", "year": 2}

print(student["name"])
student["year"] = 3
student["course"] = "BS CpE"
student["height"] = "6'7"
print(student)

print("===================================")
#Reading and iterating over a dictionary
students = {"name": "Hurveen", "year": 2}
print(students.get("email", "Not provided"))

for key, value in students.items():
    print(key,value)


print("===================================")
#A list of dictionaries
friends = [
    {"name": "hurveen", "year": 3, "scores": [90, 90]},
    {"name": "kendall", "year": 3, "scores": [90, 90]}
]

print(friends[0] ["scores"][1])
friends[0]["scores"].append(92)
friends[1]["scores"].append(92)
print(friends)

print("===================================")
#setdefault: insert only when absent
counts = {}
print(counts.setdefault("python", 0))
counts["python"] += 1
print(counts.setdefault("python", 99)) #Python completely ignores the 99. It leaves the dictionary alone and simply returns the existing value.
print(counts)

print("===================================")
#Word frequency with a dictionary
text = "Python is useful. Python helps."
words = text.lower().replace(".","").split()
counts = {}
for word in words:
    counts.setdefault(word, 0)
    counts[word] += 1
    print(counts)

print("===================================")
#JSON and dictionaries
text = '{"name": "Ana", "active": true}'
student = json.loads(text)#Converts the JSON string text into a Python dictionary. It changes JSON true into Python True
print(student["active"])

json_text = json.dumps(student)#• Converts the Python dictionary back into a raw string. It changes Python True back into JSON true.

print(json_text)

print("===================================")

students = [{"name": "Ana", "scores": [80,90]},{"name": "Ben", "scores": [70,80]}]

for student in students:
    scores = student["scores"]
    student["average"] = sum(scores) / len(scores)
    if student["average"] >= 80:
        print(student["name"])


print("===================================")

#Sets: unique elements

tags = {"python", "data", "python"}
print(len(tags))
tags.add("code")
print("data" in tags)

empty_set = set()
empty_dictionary = {}

print("===================================")
#Union, intersection and difference

a = {"food", "coffee", "cup"}
b = {"food", "juice", "glass"}

print(sorted( a & b))
print(sorted(a - b))
print(len (a | b))

print("===================================")

#Removing duplicates

names = ["Ana", "Ben", "Ana", "Cara"]
unique = set(names)
print(sorted(unique))

ordered = list(dict.fromkeys(names))

print("===================================")

#Solution Group related photos
photos = [
    {"name": "a.jpg", "tags": {"food", "cup"}},
    {"name": "b.jpg", "tags": {"food", "plate"}},
    {"name": "c.jpg", "tags": {"city", "sky"}},
    {"name": "d.jpg", "tags": {"food", "cup"}}
]

groups = {}
for i in range(len(photos)):
    for j in range(i + 1, len(photos)):
        # 1. Fixed "tag" to "tags"
        shared = photos[i]["tags"] & photos[j]["tags"] 
        if shared:
            key = tuple(sorted(shared))
            # 2. Changed group.setdefault to groups.setdefault
            group = groups.setdefault(key, set()) 
            group.add(photos[i]["name"])
            group.add(photos[j]["name"])

print(groups)

