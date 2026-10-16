def T(probabilities, i):
    result = 0
    for p in probabilities:
        result += (p / (1-p))**i
    return result

def PB(probabilities, k):
    if k == 0:
        product = 1
        for p in probabilities:
            product *= (1-p)
        return product
    
    result = 0
    for i in range(1,k+1):
        prev = PB(probabilities, k-i)
        result += (-1)**(i-1) * prev * T(probabilities, i)
    return result / k

def ChanceOfSucess(dice_pool, dice_target, total_target):
    if dice_target == 1:
        return 1

    probabilities = []
    for dice in dice_pool:
        if dice_target > dice:
            probabilities.append(0)
        else:
            probabilities.append(1 - (dice_target-1)/dice)


    chance_of_failure = 0
    for target in range(0, total_target):
        chance_of_failure += PB(probabilities, target)
    return 1-chance_of_failure

def PoolToList(pool):
    return list(map(lambda x: int(x), pool.split(',')))
