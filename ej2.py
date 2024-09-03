# Input
# customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.

# Output
# The function should return an integer, the total time required.

# Examples:
# queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

# queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

# queue_time([2,3,10], 2)
# should return 12
def queue_time(customers, n):
    tills = [0]*n
    
    for tiempo in customers:
        tiempo_minimo = 0
        for i in range(1, n):
            if tills[i] < tills[tiempo_minimo]:
                tiempo_minimo = i
        tills[tiempo_minimo] += tiempo
    return max(tills)

def main():
    a = queue_time([5,3,4], 1)
    b = queue_time([10,2,3], 2)
    c = queue_time([2,3,10], 2)
    print(a)  # deberia imprimir 12
    print(b)  # deberia imprimir 10
    print(c)  # deberia imprimir 12

if __name__ == "__main__":
    main()
