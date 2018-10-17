import time

b = 'a' * 1024 * 1024 * 1024
c = 42.
while True:
    c /= 4
    time.sleep(200)
