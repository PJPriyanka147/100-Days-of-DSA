#Brute Force --
def canShip(weights, days, capacity):
    current_weight = 0
    day_count = 1

    for weight in weights:
        if current_weight + weight > capacity:
            day_count += 1
            current_weight = 0
        current_weight += weight

        if day_count > days:
            return False
    return True

def shipWithinDays(weights, days):
    min_capacity = max(weights)
    max_capacity = sum(weights)

    for capacity in range(min_capacity , max_capacity + 1):
        if canShip(weights, days, capacity):
            return capacity
        

weights = list(map(int, input("Enter weights: ").split()))
days = int(input("Enter days: "))
result = shipWithinDays(weights, days)
print(result)

#Optimized solutin(Binary Search)
def canShip(weights, days, capacity):
    current_weight = 0
    day_count = 1

    for weight in weights:
        if current_weight + weight > capacity:
            day_count += 1
            current_weight = 0
        current_weight += weight

        if day_count > days:
            return False
    return True

def shipWithinDays(weights, days):
    min_capacity = max(weights)
    max_capacity = sum(weights)

    left, right = min_capacity, max_capacity + 1

    while left < right:
        mid  = (left + right) // 2

        if canShip(weights, days, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

weights = list(map(int, input("Enter weights: ").split()))
days = int(input("Enter days: "))
result = shipWithinDays(weights, days)
print(result)