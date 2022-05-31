#!/usr/bin/python3
for k in range(ord('z'), ord('a') - 1, -1):
    if k % 2 != 0:
        k = k - 32
    print("{:k}".format(k), end='')
