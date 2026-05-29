# Placing Premades class
p = Premades() # code on https://github.com/javersoncleidinato-afk/Learm/blob/main/Premades.py

# 1. print
p.print("10 times!", 10)
# prints it 10 times, if amount = None print it only 1 time

# 2. wait
print("2 seconds")
p.wait(2)
print("end, 1 second")
p.wait()
print("end")
# wait(num), wait 'num' seconds, if None waits 1 second