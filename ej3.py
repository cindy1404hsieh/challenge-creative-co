# Goal
# Rearrange the boxes in the factory to form stacks of equal height.
# Rules
# You work in an automated factory. The factory uses a simple robotic arm to move boxes around. The arm is capable of picking a box from a stack, and placing it on another stack. All boxes are on one of a given number of stacks. Your objective is to rearrange the stacks in order to have an equal number of boxes on each stack. If this is not possible, any excess box must be stacked from left to right. Your code will periodically receive the current state of the arm and the number of boxes on each stack. In order to succeed, your function must return one command per turn up until the boxes are correctly positioned.
# The available commands are: 
# RIGHT : the arm moves one stack to the right. 
# LEFT : the arm moves one stack to the left. 
# PICK : the arm grabs a box from the stack directly below it. 
# PLACE : the arm places a box onto the stack directly below it. Warning, you may execute a maximum of 100 commands, but it is not necessary to minimize the amount of instructions.
# Implementation
# Implement the function solve(clawPos, boxes, boxInClaw) that takes as arguments: an integer clawPos for the index of the stack the arm is currently above. boxes an array of integers for the size of each stack. The integer boxInClaw which will be equal to 1 if the arm is carrying a box, 0 otherwise. Each stack can have up to 5 boxes to prevent stack collapse, boxes should be stacked until further stacking is no longer possible and in this case the function should return the WARNING command.
# Victory Conditions
# All stacks have been smoothed from left to right. It should look like this for the example above.

# Lose Conditions
# Your function returns an incorrect command. The stacks still aren't smooth after 100 turns.
# Constraints
# 2 ≤ number of stacks ≤ 8
# 1 ≤ number of boxes ≤ 16

def solve(clawPos, boxes, boxInClaw):
    cant_pilas = len(boxes)
    sum_total_caja = sum(boxes)
    altura_ideal = sum_total_caja // cant_pilas
    caja_de_sobra = sum_total_caja % cant_pilas

    altura_target = [altura_ideal] * cant_pilas

    for i in range(cant_pilas):
        if caja_de_sobra > 0:
            altura_target[i] += 1
            caja_de_sobra -= 1

    # RIGHT : the arm moves one stack to the right. 
    # LEFT : the arm moves one stack to the left. 
    # PICK : the arm grabs a box from the stack directly below it. 
    # PLACE : the arm places a box onto the stack directly below it. 
    if boxInClaw == 1:
        for i in range(cant_pilas):
            if boxes[i] < altura_target[i]:
                if clawPos < i:
                    return "RIGHT"
                elif clawPos > i:
                    return "LEFT"
                else:
                    return "PLACE"
        
    elif boxInClaw == 0:
        for i in range(cant_pilas):
            if boxes[i] > altura_target[i]:
                if clawPos < i:
                    return "RIGHT"
                elif clawPos > i:
                    return "LEFT"
                else:
                    return "PICK"   
    return "WARNING" 

