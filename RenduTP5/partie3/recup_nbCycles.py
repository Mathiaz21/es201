import re

def extract_cpu_cycles(filename):
    cpu_cycles = {}

    with open(filename, 'r') as file:
        for line in file:
            match = re.match(r'system\.cpu(\d+)\.numCycles\s+(\d+)', line)
            if match:
                cpu_id = int(match.group(1))
                num_cycles = int(match.group(2))
                cpu_cycles[cpu_id] = num_cycles
    return cpu_cycles

filename = "stats8.txt"
cpu_cycles = extract_cpu_cycles(filename)

for cpu_id, num_cycles in cpu_cycles.items():
    print(f"CPU {cpu_id} : {num_cycles} cycles")
