"""diffie hellman primitive root function calculator"""

# function to check if a number is a primitive root for a given prime number
def is_primitive_root(root, prime):
    powers = set()
    # iterate through powers from 1 to (prime - 2)
    for i in range(1, prime - 1):
        # calculate (root ^ i) % prime
        power = pow(root, i, prime)
        # if the result is already in the set, this is not a primitive root
        if power in powers:
            return False
        # add the result to the set
        powers.add(power)
    # if all results are unique, this is a primitive root
    return True

# function to find all primitive roots of a given prime number
def find_primitive_roots(prime):
    primitive_roots = []
    # iterate through numbers from 2 to (prime - 1)
    for candidate_root in range(2, prime):
        # check if the current number is a primitive root
        if is_primitive_root(candidate_root, prime):
            # add the primitive root to the list
            primitive_roots.append(candidate_root)
    return primitive_roots

# main function to run the program
def main(): # try 10007
    # get the prime number as input
    prime = int(input("Enter a prime number: "))
    # find all primitive roots for the given prime number
    primitive_roots = find_primitive_roots(prime)
    # calculate the smallest primitive root using the min() function
    smallest_primitive_root = min(primitive_roots)
    
    # print the list of all primitive roots
    print(f"All primitive roots of {prime}: {primitive_roots}")
    # print the smallest primitive root
    print()
    print(f"The smallest primitive root of {prime} is {smallest_primitive_root}")

# execute the main function
if __name__ == "__main__":
    main()
