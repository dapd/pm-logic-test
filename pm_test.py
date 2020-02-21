# Logic test - Answer
# Author: Diogo Dantas
import json

# Read input file
with open('source_file_2.json') as json_file:
    data = json.load(json_file)

# Create dicts
managers = {}
watchers = {}

# Manipulate the dataset
for project in data:
    for manager in project["managers"]:
        if manager in managers:
            managers[manager].append((project["name"],project["priority"]))
        else:
            managers[manager] = [(project["name"],project["priority"])]
    for watcher in project["watchers"]:
        if watcher in watchers:
            watchers[watcher].append((project["name"],project["priority"]))
        else:
            watchers[watcher] = [(project["name"],project["priority"])]

# Sort projects
for manager in managers:
    managers[manager].sort(key=lambda tup: tup[1])
    # Remove priority
    idx = 0
    for project in managers[manager]:
        managers[manager][idx] = project[0]
        idx = idx+1

for watcher in watchers:
    watchers[watcher].sort(key=lambda tup: tup[1])
    # Remove priority
    idx = 0
    for project in watchers[watcher]:
        watchers[watcher][idx] = project[0]
        idx = idx+1


# Write output files
with open('managers.json', 'w') as outfile1:
    json.dump(managers, outfile1)

with open('watchers.json', 'w') as outfile2:
    json.dump(watchers, outfile2)