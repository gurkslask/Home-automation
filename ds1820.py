
with open('/sys/bus/w1/devices/28-00000523a1cb/w1_slave', 'r') as tempfile:
    data = sum(1 for line in tempfile)
    #print tempfile.readline(10)
    for x in range(0,data):
        print(tempfile.readline(x)value)