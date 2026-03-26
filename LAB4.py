tasks = {}

n = int(input("Enter number of tasks: "))

for i in range(n):
    print()
    name = input("Enter task name: ")
    dep_count = int(input("How many dependencies for " + name + "? "))

    deps = []
    for j in range(1, dep_count + 1):
        dep = input("Enter dependency " + str(j) + ": ")
        deps.append(dep)

    tasks[name] = deps

print("\nTASK STRUCTURE:")
for task in tasks:
    print(task + " -> " + str(tasks[task]))

print("\nINITIAL TASKS (no dependencies):")
initial_found = False
for task in tasks:
    if len(tasks[task]) == 0:
        print(task)
        initial_found = True
if initial_found == False:
    print("None")

print("\nEXECUTION ORDER:")

finished = set()
order = []

progress = True
while progress == True:
    progress = False
    for task in tasks:
        if task in finished:
            continue

        all_done = True
        for dep in tasks[task]:
            if dep not in finished:
                all_done = False

        if all_done == True:
            finished.add(task)
            order.append(task)
            progress = True
            break

incomplete = []
for task in tasks:
    if task not in finished:
        incomplete.append(task)

if len(incomplete) > 0:
    print("No task can be started.")
    print("\nERROR: Circular dependency detected!")
    print("These tasks could not be completed:")
    for task in incomplete:
        print(task)
else:
    for i in range(len(order)):
        print("Step " + str(i+1) + ": " + order[i])
    print("\nALL TASKS COMPLETED SUCCESSFULLY")