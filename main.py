#სავარჯიშო 1

def constant_op(data):
    """O(1): ციკლი ყოველთვის 1-ჯერ სრულდება, data-ს სიგრძე არ ზემოქმედებს."""
    operations = 0
    result = None
    for _ in range(1):
        result = data[0]          
        operations += 1
    return result, operations


def linear_op(data):
    """O(n): ყოველი ელემენტი მოწმდება ერთხელ."""
    operations = 0
    even_count = 0
    for x in data:
        operations += 1           
        if x % 2 == 0:
            even_count += 1
    return even_count, operations


def quadratic_op(data):
    """O(n²): ყოველი ელემენტი შედარდება ყველა ელემენტს."""
    operations = 0
    equal_pairs = 0
    for a in data:
        for b in data:
            operations += 1      
            if a == b:
                equal_pairs += 1
    return equal_pairs, operations


for n in (10, 100):
    data = list(range(1, n + 1))
    print(f"--- n = {n} ---")
    print("O(1)  ოპერაციები:", constant_op(data)[1])
    print("O(n)  ოპერაციები:", linear_op(data)[1])
    print("O(n²) ოპერაციები:", quadratic_op(data)[1])