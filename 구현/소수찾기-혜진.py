def solution(numbers):
    numbers = list(numbers)
    numbers.sort(reverse=True)
    max_num = int("".join(numbers))
    
    prime = [True] * (max_num + 1)
    
    for i in range(2, int(max_num**0.5) + 2):
        if prime[i]:
            for j in range(i*2,max_num + 1,i):
                prime[j] = False

    ans = 0
    for idx, val in enumerate(prime):
        if val and idx > 1:
            prime_nums = list(str(idx))
            for num in prime_nums:
                if num not in numbers or numbers.count(num) < prime_nums.count(num):
                    break
            else:
                ans += 1
    return ans