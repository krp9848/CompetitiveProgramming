def divisibleSumPairs(n: int, k: int, ar: list) -> int:
    """Return the number of pairs (i, j) where ar[i] + ar[j] % k == 0 
    given that i < j 

    Args:
        n (int): size of the given array
        k (int): divisor
        ar (list): given list 

    Returns:
        int: count of the number of pairs that satisfy the above mentioned condition
    """
    return sum([True for i in range(n) for j in range(i) if (ar[j] + ar[i]) % k == 0])


if __name__ == '__main__':
    #Provide the size of the array and divisor
    n, k = map(int, input().split())

    #Provide the array of size n
    ar = list(map(int, input().split()))
    
    #Return the number of desired pairs
    print(divisibleSumPairs(n, k, ar))
    