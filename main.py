config = {}
with open("config/config.txt") as f:
    for line in f:
        key, value = line.strip().split("=")
        config[key] = int(value)

print("interval -- ", config["interval"])
