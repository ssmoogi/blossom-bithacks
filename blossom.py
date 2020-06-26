"""
Blossom | BitHacks 2020

"""
import numpy as np

tasks = []
duration = []
difficulty = []
priority = []
task_weight = []

schedule = []
preferred = []

reward = 10

duration_w = 1
difficulty_w = 1
priority_w = 1

dur = False
dif = False
pri = False

sched_filled = False
running = True;

while running:
    message = input("Blossom: ")
    if message == "add":
        amount = input("How many tasks do you want to add? ")
        sched_filled = True
        for i in range(int(amount)):
            a = input("Task: ")
            tasks.append(a)
            b = int(input("Duration: "))
            duration.append(b)
            c = int(input("Difficulty: "))
            difficulty.append(c)
            d = int(input("Priority: "))
            priority.append(d)
            task_weight.append((b * duration_w) + (c * difficulty_w) + (d * priority_w))
            preferred.append("placeholder")
        
    if message == "show":
        if sched_filled == False:
            print("Please use the command [add] to fill in your schedule.")
        else:
            for x in tasks:
                print(x)
            
    if message == "schedule":
        if sched_filled == False:
            print("Please use the command [add] to fill in your schedule.")
        else:
            tasks = np.array(tasks)
            task_weight = np.array(task_weight)
            sort = task_weight.argsort()
            schedule = tasks[sort]
            schedule = schedule[::-1]
            print("Here is your schedule: ")
            for x in schedule:
                print(x)
            
    if message == "feedback" and reward <= 30 and sched_filled == True:
        correct = input("Did you like this schedule? [y/n] ")
        if correct == "y":
            print("Thank you for your feedback")
            reward += 1
        else:
            print("Please rearrange your schedule so we can improve our services.")
            reward -= 1
            for x in range(len(tasks)):
                order = int(input("Where would you place [%s]? " %tasks[x]))
                preferred[x] = tasks[order - 1]
                if order == 1:
                    #change values based on highest placing task
                    task_vals = [duration[x], difficulty[x], priority[x]]
                    max_task = max(task_vals)
                    for x in range(len(task_vals)):
                        if task_vals[x] == max_task:
                            if x == 0 and dur == False:
                                duration_w -= 0.1
                            elif x == 0 and dur == True:
                                duration_w += 0.1
                            elif x == 1 and dif == False:
                                difficulty_w -= 0.1
                            elif x == 1 and dif == True:
                                difficulty_w += 0.1
                            elif x == 2 and pri == False:
                                priority_w -= 0.1
                            elif x == 2 and pri == True:
                                priority_w += 0.1
                
            print("Here is your preferred schedule: ")
            for x in preferred:
                print(x)
            print("Please wait as we adjust our system...")
            print("Duration Weight: %f" %duration_w)
            print("Difficulty Weight: %f" %difficulty_w)
            print("Priority Weight: %f" %priority_w)
            if duration_w == 0:
                dur = True
            elif duration_w == 1:
                dur = False
                
            if difficulty_w == 0:
                dif = True
            elif difficulty_w == 1:
                dif = False
            
            if priority_w == 0:
                pri = True
            elif priority_w == 1:
                pri = False
                
    if message == "feedback" and sched_filled == False:
        print("Please use the command [add] to fill in your schedule.")
            
    if message == "reset":
        tasks = []
        duration = []
        difficulty = []
        priority = []
        task_weight = []
        schedule = []
        preferred = []
        sched_filled = False
    
    if message == "stop":
        running = False