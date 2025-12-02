current = 50
results = 0

'''
# Original Code
with open("input.txt") as lines:
    for line in lines:
        line = line.strip()
        direction = line[0]
        turns = int(line[1:])

        if direction == 'L':
            total = current - (turns % 100)

            if (total < 0):
                current = 100 + total
            else:
                if (total == 0):
                    results += 1
                current = total
        else:
            total = current + (turns % 100)

            if (total == 100):
                current = 0
                results += 1
            else:
                if (total > 100):
                    current = total % 100
                else:
                    current = total

print(results)
'''

# ChatGpt Generated
current = 50          # starting position on the dial
results = 0           # times the dial ends up at 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue   # skip empty lines, just in case

        direction = line[0]       # 'L' or 'R'
        turns = int(line[1:])     # rest of the line is the number
        steps = turns % 100       # effective movement on a 0–99 dial

        if direction == 'L':
            current = (current - steps) % 100
        else:  # assume 'R'
            current = (current + steps) % 100

        if current == 0:
            results += 1

print(results)
