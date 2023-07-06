from sympy import nextprime, isprime

def find_smarandache_wellin(start_index, max_index, target_length):
    prime = nextprime(1)  # Start from the first prime number
    smarandache_wellin = str(prime)
    index = 1

    print(f"Starting from index {index} with SW: {smarandache_wellin}")

    while index < max_index:
        index += 1
        prime = nextprime(prime)
        smarandache_wellin += str(prime)

        if len(smarandache_wellin) > target_length:
            smarandache_wellin = smarandache_wellin[:target_length]  # Trim to target length
            if index >= start_index and isprime(int(smarandache_wellin)):
                print(f"Found probable SW prime at index {index}: {smarandache_wellin}")
                print(f"Number of digits: {len(smarandache_wellin)}")
                return int(smarandache_wellin), index

        if index % 1000 == 0:  # Print progress every 1000 steps
            print(f"Reached index {index} with SW: {smarandache_wellin[:10]}...{smarandache_wellin[-10:]}")

    print("No SW prime found within the range.")
    return None, None

# Usage:
sw_prime, index = find_smarandache_wellin(22077, 50000, 5719)
if sw_prime is not None:
    print(f"Found SW prime at index {index}: {sw_prime}")
    print(f"Number of digits: {len(str(sw_prime))}")

print("Program completed.")
