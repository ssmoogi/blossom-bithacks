# blossom-bithacks
BitHacks Hackathon 2020 Project \
🔗 [Taikai Submission](https://taikai.network/en/bithacks/challenges/bithacks/projects/ckbvwc7mgrlbe0863xp1hkv4y) \
🎥 [Video Demo](https://youtu.be/9PlPIBgKYiM)

### purpose
Today’s teens are overwhelmed with work, yet aren’t that great at managing their time to get work done effectively and efficiently. There are so many commitments they need to balance among school work, sports, clubs, extracurriculars, and it doesn’t even leave room for all the distractions they face in their life. As a result, they often lose track of time and end up procrastinating until the last minute, piling up work without even realizing it.

### goal
Blossom aims to help people manage their time better and leave space to pursue other endeavors in their spare time. Our main goal is to allow users to schedule their time more efficiently in order to get the most out of their daily routines.Our project focuses on teenagers, but can impact any person who needs a simple method to manage their time.

### how it works
Through our application, users will be able to easily input their tasks and goals, which will then be converted into a schedule for users to use. Blossom will take in feedback to ensure the schedule is best fit to the user’s preferences. Blossom’s main goal is to calculate an efficient schedule based off of the user’s input and it’s default weighting system. However, as the user continues to give more feedback to the function, the program improves its weighting system to create the best possible schedule and continues doing so until the reward is maximized, creating a schedule perfectly adapted to the user’s preferences just by learning from its own experience

### key features
1. Customize your schedule to fit your needs; Blossom helps you fit work around your events and daily life. Tell what you’ve already got planned and it’ll find time in your day.
2. Add tasks whenever and reschedule with ease; This application can recreate your schedule for you whenever you need to add something new, don’t worry.
3. Simple to use w/ chat bot option; Connect Blossom to your messages to easily add events. We’ll do our best to understand your texts in when you’re in a rush.
4. Helps you complete long-term goals; Use Blossom to find the moments in every day to learn that language, and finish that project. We find time for you to do even with a busy schedule.
5. Notifications alerting you when to switch tasks; Know exactly when to switch over to the next project or event. Want to spend more time on what you’re doing? We’ve got that covered too.
6. Adjusts to your preferences and needs; Using Machine Learning, our application adjusts itself to suit your preferences when arranging your schedule.

### app layouts
![image 1](https://taikai.azureedge.net/79Wpt-cR6HzzDPd8Tt7VXSj1IlzI97pzC39geH5u1QA/rs:fit:800:0:0/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3RhaWthaS1zdG9yYWdlL2ltYWdlcy9kY2Y4Mzk5MC1iNzg1LTExZWEtODhlNy0xOWQyYTcwMTgwMmJCbG9zc29tIF8gQml0SGFja3MgMjAyMC5wbmc)
![image 2](https://taikai.azureedge.net/ALaQYHSZt6P1iODqXMwNt2rTDhO6gpaHuGafPVlhFsc/rs:fit:800:0:0/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3RhaWthaS1zdG9yYWdlL2ltYWdlcy9lMTVlMmJjMC1iNzg1LTExZWEtODhlNy0xOWQyYTcwMTgwMmJCbG9zc29tIF8gQml0SGFja3MgMjAyMCAoMSkucG5n)

### sms (twilio) chatbot
![image 3](https://taikai.azureedge.net/21K_eqXZaPSgCj4hehYg190h04DDX1yTKAUST1rZdys/rs:fit:800:0:0/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3RhaWthaS1zdG9yYWdlL2ltYWdlcy9jODIyOGU3MC1iNzg2LTExZWEtOWQxOC1kZmZiNDNmOGNkOGVCbG9zc29tIF8gQml0SGFja3MgMjAyMCAoMykucG5n)

### ai workflow
![image 4](https://taikai.azureedge.net/dl6S63pS0DfiHH-iDzWM3nlUEuS36JsmWsMcumR7Jmw/rs:fit:800:0:0/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3RhaWthaS1zdG9yYWdlL2ltYWdlcy82ZGE5YTBkMC1iNzg4LTExZWEtOWQxOC1kZmZiNDNmOGNkOGVCbG9zc29tIF8gQml0SGFja3MgMjAyMCAoNCkucG5n)

### code
We wrote a application to be a prototype of how the application would work. The program takes in certain input (in the future we'd use Natural Language Processing to improve upon this), and based on that creates a schedule based on tasks inputted. The AI/ML section happens when the user enters the 'feedback' command, and that processes the user's preferred version of the schedule and adjusts the weighting give to the three main attributes: duration, difficulty, and priority. We created two versions, one that runs in the console (blossom.py) which you can download and run, and one that works with Twilio/Flask to create a chat bot through messaging (blossom-text.py).

### twilio/flask/ngrok screenshots
![image 5](https://taikai.azureedge.net/Q8GQ62Qgo4EC_I0t_RYAIoxsIQiotnHtJ_xEJLagYfQ/rs:fit:800:0:0/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3RhaWthaS1zdG9yYWdlL2ltYWdlcy9hM2I2ZTg5MC1iNzg4LTExZWEtOWQxOC1kZmZiNDNmOGNkOGVCbG9zc29tIF8gQml0SGFja3MgMjAyMCAoNSkucG5n)

### how to run
Download or copy the Python script in the file ```blossom.py``` and run in on your local computer. Once you run the program:
- Use the command 'add' to create a new task to your to-do list.
- Use the command 'show' to display all your current tasks.
- Use the command 'schedule' to order your tasks based on your preferred priority.
- Use the command 'feedback' to give the program feedback on how it generated your schedule and help it align to your preferences.
- Use the command 'reset' to start from the beginning.

### contributers
Rida Faraz [@rfaraz](https://github.com/rfaraz)
Sahana Moogi [@ssmoogi](https://github.com/ssmoogi)


🌸 Thank you for checking out our project repo!!
