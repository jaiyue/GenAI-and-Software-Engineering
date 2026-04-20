Here's a simple implementation — it eats as much as needed but not more than remaining, then returns [total_eaten, remaining_after]:

def eat(number, need, remaining):
    eaten = min(need, remaining)
    return [number + eaten, remaining - eaten]

