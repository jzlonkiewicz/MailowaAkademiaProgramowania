# sieve of Eratosthenes

a = int(input("How many numbers do you want to check? "))
range_list = [*range(2, a + 1)]
non_prime_list = []
prime_list = []

for i in range(2, a + 1):
    n = 2
    if i not in non_prime_list:
        while i * n <= a:
            if i * n not in non_prime_list:
                non_prime_list.append(i * n)
            n += 1

# print(non_prime_list)
# print(len(non_prime_list))
range_list = list(set(range_list) - set(non_prime_list))
# print(len(range_list))
range_list.sort()
print("These are prime numbers\n", range_list)
