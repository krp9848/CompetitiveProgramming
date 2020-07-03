def flipping_bits(n:int) -> int:
    """Flip the bits of the unsigned integer and return the 
    result as an unsigned integer

    Args:
        n (int): Given Integer

    Returns:
        int: Integer on reversing the bits
    """
    #Can also be solvied very concisely using bit operators (0xffffffff & ~n)
    #let's convert the given integer into 32-bit binary number 
    binary_n = [0 for i in range(32)]
    size = 31
    while n:
        rem = n % 2 
        n = n // 2
        binary_n[size] = rem
        size = size -1 
    
    #flipping the bits 
    binary_n = [0 if i else 1 for i in binary_n]

    #converting the binary back to integer 
    reverse_n = 0
    size_n = len(binary_n)
    for i in range(size_n):
        reverse_n += binary_n[i] * 2 ** (size_n - i - 1)

    return reverse_n

