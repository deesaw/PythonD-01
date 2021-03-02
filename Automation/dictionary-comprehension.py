#dictionary comprehension
j={x:x*x for x in range(1,100,3)}

#how to read a config file into a dictionary

k=dict([line.rstrip().split('#') for line in open('c:/users/tring/desktop/words.txt')])