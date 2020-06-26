"""
Blossom | BitHacks 2020

"""
#imports
import numpy as np

#task and atribute lists
tasks = []
duration = []
difficulty = []
priority = []
task_weight = []

#manipulated versions of original lists
schedule = []
preferred = []

#reward variable, starts from 10
reward = 10

#attribute weight variables
duration_w = 1
difficulty_w = 1
priority_w = 1

#variables to reverse the direction +/- the weights are changed
dur = False
dif = False
pri = False

#other booleans that manage overall program
sched_filled = False
running = True;

#main loop; runs until [stop] command used
while running:

    #asks for message
    message = input("Blossom: ")

    #create new task(s) command
    if message == "add":

        #set number of tasks being added
        amount = input("How many tasks do you want to add? ")

        #allows other functions to be used
        sched_filled = True

        #adds specified number of tasks to lists
        for i in range(int(amount)):
            a = input("Task: ")
            tasks.append(a)
            b = int(input("Duration: "))
            duration.append(b)
            c = int(input("Difficulty: "))
            difficulty.append(c)
            d = int(input("Priority: "))
            priority.append(d)

            #calculate total weight of the task
            task_weight.append((b * duration_w) + (c * difficulty_w) + (d * priority_w))

            #create a placeholder spot for the preferred schedule list (will be used in [feedback])
            preferred.append("placeholder")
        
    #show all tasks unordered command
    if message == "show":

        #if schedule is empty
        if sched_filled == False:
            print("Please use the command [add] to fill in your schedule.")

        #print the tasks in the order inputted by the user
        else:
            for x in tasks:
                print(x)
    
    #creates a schedule from the tasks and their weights
    if message == "schedule":

        #if schedule is empty
        if sched_filled == False:
            print("Please use the command [add] to fill in your schedule.")

        #order and print schedule based on task weights influenced by user preferences
        else:
            tasks = np.array(tasks)
            task_weight = np.array(task_weight)
            sort = task_weight.argsort()
            schedule = tasks[sort]
            schedule = schedule[::-1]
            print("Here is your schedule: ")
            for x in schedule:
                print(x)
    
    #collects feedback and changes model based on feedback given
    if message == "feedback" and reward <= 30 and sched_filled == True:
        
        #asks if the user liked the schedule or not
        correct = input("Did you like this schedule? [y/n] ")

        #if user likes the schedule, reward is increase by 1
        if correct == "y":
            print("Thank you for your feedback.")
            reward += 1

        #if user doesn't like the given schedule, the program collects feedback on how the user prefers their schedule to be, and reward decreases by 1
        else:
            print("Please rearrange your schedule so we can improve our services.")
            reward -= 1

            #asks the user where in their schedule they'd place each task
            for x in range(len(tasks)):
                order = int(input("Where would you place [%s]? " %tasks[x]))

                #creates a preferred schedule list
                preferred[x] = tasks[order - 1]

                #changes are made based on the first task in the user's preferred schedule
                if order == 1:
                    #creates list to store each the top placing task's attribute values
                    task_vals = [duration[x], difficulty[x], priority[x]]

                    #finds the highest valued attribute
                    max_task = max(task_vals)

                    #depending on the highest valued attribute, the program changes the weights by eigher adding or subtracting 0.1
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
            
            #prints preferred schedule
            print("Here is your preferred schedule: ")
            for x in preferred:
                print(x)

            #prints new weights
            print("Please wait as we adjust our system...")
            print("Duration Weight: %f" %duration_w)
            print("Difficulty Weight: %f" %difficulty_w)
            print("Priority Weight: %f" %priority_w)

            #reverses direction +/- weighted values are changed if they hit 1 or 0
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
                
    #if schedule is empty
    if message == "feedback" and sched_filled == False:
        print("Please use the command [add] to fill in your schedule.")
    
    #resets all lists
    if message == "reset":
        tasks = []
        duration = []
        difficulty = []
        priority = []
        task_weight = []
        schedule = []
        preferred = []
        sched_filled = False
    
    #exits while loop and stops program
    if message == "stop":
        running = False