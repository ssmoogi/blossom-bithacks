"""
Blossom | BitHacks 2020

"""
#libraries
import numpy as np
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def incoming_sms():
    # Start our TwiML response
    resp = MessagingResponse()

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
    
    body = request.values.get('Body', None)

    if body == 'hello':
        resp.message("Hello! Welcome to Blossom, your task organizing assistant.")

    if body == 'bye':
        resp.message("Goodbye, talk to you later!")

    if body == 'add':
        resp.message("How many tasks do you want to add?")
        add_sent = True
        amount = request.values.get('Body', None)
        sched_filled = True
        for i in range(int(amount)):
            resp.message("Task: ")
            a = request.values.get('Body', None)
            tasks.append(a)

            resp.message("Duration: ")
            b = int(request.values.get('Body', None))
            duration.append(b)

            resp.message("Difficulty: ")
            c = int(request.values.get('Body', None))
            difficulty.append(c)

            resp.message("Priority: ")
            d = int(request.values.get('Body', None))
            priority.append(d)

            task_weight.append((b * duration_w) + (c * difficulty_w) + (d * priority_w))
            preferred.append("placeholder")
        
    if body == 'show':
        if sched_filled == False:
            resp.message("Please use the message [add] to fill in your schedule.")
        else:
            for x in tasks:
                resp.message(x)
            
    if body == 'schedule':
        if sched_filled == False:
            resp.message("Please use the message [add] to fill in your schedule.")
        else:
            tasks = np.array(tasks)
            task_weight = np.array(task_weight)
            sort = task_weight.argsort()
            schedule = tasks[sort]
            schedule = schedule[::-1]
            resp.message("Schedule: ")
            for x in schedule:
                resp.message(x)
            
    if body == 'feedback' and sched_filled == True:
        resp.message("Did you like this schedule? [y/n] ")
        correct = request.values.get('Body', None)
        if correct == "y":
            resp.message("Thank you for your feedback.")
            reward += 1
        else:
            resp.message("Please rearrange your schedule so we can improve our services.")
            reward -= 1
            for x in range(len(tasks)):
                resp.message("Where would you place [%s]? " %tasks[x])
                order = int(request.values.get('Body', None))
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
                
            resp.message("Here is your preferred schedule: ")
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
                
    if body == 'feedback' and sched_filled == False:
        resp.message("Please use the command [add] to fill in your schedule.")
            
    if body == 'reset':
        tasks = []
        duration = []
        difficulty = []
        priority = []
        task_weight = []
        schedule = []
        preferred = []
        sched_filled = False

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)