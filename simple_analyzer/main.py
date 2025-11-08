import time
import random 
from analyzer import Analyzer


config = {}
with open("config/config.txt") as f:
    for line in f:
        key, value = line.strip().split("=")
        config[key] = int(value)

interval = config["interval"]
sequence_length = config["sequence_length"]

print("interval:", interval)
print("sequence length:", sequence_length)

analyzer = Analyzer()

while True:
    number = random.randint(1, 100)
    analyzer.add_number(number)

    print("##################################################")
    print("numbers:", analyzer.numbers)
    print("even count:", analyzer.even_count())
    print("odd count:", analyzer.odd_count())
    print("highest:", analyzer.highest_number())
    print("increasing pairs:", analyzer.increasing_pairs())
    print("##################################################")

    if len(analyzer.numbers) >= sequence_length and time.localtime().tm_sec == 0:
        break

    time.sleep(interval)

	print("experimental text")
