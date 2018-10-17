import concurrent.futures


def compute(n):
    a = 'b' * 1 * (1024 * 1024 * 1024)
    while True:
        x = 42/3.

def main():
    with concurrent.futures.ProcessPoolExecutor(20) as executor:
        for prime in zip(range(40), executor.map(compute, range(40))):
            print('%d is prime: %s' % (prime, prime))

if __name__ == '__main__':
    main()
