'''
You're writing code to control your town's traffic lights.
You need a function to handle each change from green, to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing the current state of the light
and returns a string representing the state the light should change to.

For example, when the input is green, output should be yellow.
'''


def update_light(current):
    light_list = ['green', 'yellow', 'red']
    for i in range(len(light_list)):
        if current == light_list[i]:
            return light_list[i - len(light_list) + 1]


def update_light1(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]


x = input()
print(update_light(x))