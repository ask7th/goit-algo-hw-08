import heapq
import random

def min_cost_connect_cables(lengths):
    if not lengths:
        return 0

    heapq.heapify(lengths)
    total_cost = 0
    step = 0

    print("\nПочаткова купа: ",lengths)
    

    while len(lengths) > 1:
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        cost = first + second
        total_cost += cost

        heapq.heappush(lengths, cost)

        step += 1
        print(f"\nКрок {step}:")
        print("Обʼєднання:", first, "+", second, "=", cost)
        print("Нова купа:", lengths)
        print("Загальна вартість на цьому кроці:", total_cost)

    return total_cost


cables = random.sample(range(10), 5)
print("Довжина кабелів: ", cables)
print("\nМінімальна вартість загальних витрат: ", min_cost_connect_cables(cables))