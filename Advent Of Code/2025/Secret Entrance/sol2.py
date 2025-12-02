current = 50
results = 0

'''
Original Solution

with open("input.txt") as lines:
    for line in lines:
        line = line.strip()
        direction = line[0]
        turns = int(line[1:])

        # Extra turns are garaunteed to have hit 0 at least once
        extra_turns = turns // 100
        # Remaining turns
        remaining_turns = turns % 100
        # Since extra turns are garaunteed to hit 0 once, add it
        results += extra_turns

        print(current)
        if direction == 'L':
            # Remaining turns is 100% < 100, it can only go past 0 once more
            if (remaining_turns > 0):
                # It will go past or land on 0
                if (remaining_turns >= current and current != 0):
                    print("Additional turn (L)")
                    results += 1
                    current = (100 + current - remaining_turns) % 100
                elif (remaining_turns >= current and current == 0):
                    current = (100 + current - remaining_turns) % 100
                else:
                    current = current - remaining_turns
        else:
            # Remaining turns is 100% < 100, it can only go past 0 once more
            if (remaining_turns > 0):
                # 
                if (remaining_turns + current >= 100):
                    print("Additional turn (R)")
                    results += 1
                    current = (remaining_turns + current) % 100
                else:
                    current += remaining_turns
print(current)
print("=" * 40)
print(results)
'''

current = 50
results = 0

with open("input.txt") as lines:
    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]       # 'L' or 'R'
        turns = int(line[1:])     # always >= 0

        # Each full 100-step rotation hits 0 exactly once
        full_rotations, remaining = divmod(turns, 100)
        results += full_rotations

        if direction == 'L':
            # Going left: positions visited are current-1, current-2, ... (mod 100)
            # In the remaining (<100) steps, we hit 0 iff:
            #   - we start above 0, and
            #   - we move at least `current` steps.
            if remaining > 0 and 0 < current <= remaining:
                results += 1

            current = (current - remaining) % 100

        else:  # direction == 'R'
            # Going right: positions visited are current+1, current+2, ... (mod 100)
            # In the remaining (<100) steps, we hit 0 iff:
            #   - we start above 0, and
            #   - current + remaining >= 100 (we wrap past 99 -> 0).
            if remaining > 0 and current > 0 and current + remaining >= 100:
                results += 1

            current = (current + remaining) % 100

print(results)
