import concurrent.futures

import multiprocessing

def compute(n):
    a = 'b' * 1 * (1024 * 1024 * 1024)
    while True:
        x = 42/3.

def main():
    print('cores', multiprocessing.cpu_count())
    with concurrent.futures.ProcessPoolExecutor(2) as executor:
        for prime in zip(range(40), executor.map(compute, range(40))):
            print('%d is prime: %s' % (prime, prime))

if __name__ == '__main__':
    main()
