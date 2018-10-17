import concurrent.futures

def compute(n):
    while True:
        x = 42/3.

def main():
    with concurrent.futures.ProcessPoolExecutor(10) as executor:
        for number, prime in zip(range(20), executor.map(compute, range(20))):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()
