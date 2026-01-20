def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def factors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result