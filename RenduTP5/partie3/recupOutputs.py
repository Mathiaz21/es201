import re
import matplotlib.pyplot as plt

def extract_cpu_cycles(filename):
    cpu_cycles = {}

    with open(filename, 'r') as file:
        for line in file:
            match = re.match(r'system\.cpu(\d+)?\.numCycles\s+(\d+)', line)
            if match:
                cpu_id = 0 if match.group(1) is None else int(match.group(1))
                num_cycles = int(match.group(2))
                cpu_cycles[cpu_id] = num_cycles

    return cpu_cycles

def extract_nb_instructions(filename):
    nb_insts = []

    with open(filename, 'r') as file:
        for line in file:
            match = re.match(r'sim_insts\s+(\d+)', line)
            if match:
                nb_insts.append(int(match.group(1)))

    return nb_insts

def format_markdown_row(cpu_cycles, max_cpus=16):
    row = ["| n={} ".format(len(cpu_cycles))]

    for i in range(max_cpus):
        cpu_id = "CPU{}".format(i)
        value = cpu_cycles.get(i, "x")
        row.append("| {} ".format(value))

    row.append("|")
    return "".join(row)


print("|     	| CPU0   	| CPU1   	| CPU2   	| CPU3   	| CPU4   	| CPU5   	| CPU6   	| CPU7   	| CPU8 	| CPU9 	| CPU10 	| CPU11 	| CPU12 	| CPU13 	| CPU14 	| CPU15 	|")
print("|-----	|--------	|--------	|--------	|--------	|--------	|--------	|--------	|--------	|------	|------	|-------	|-------	|-------	|-------	|-------	|-------	|")
nb_threads = []
nb_cycles_app = []
speedup = []
nb_insts = []
IPC = []
for i in range(5):
    filename = "stats" + str(2**i)+ ".txt"
    cpu_cycles = extract_cpu_cycles(filename)
    markdown_row = format_markdown_row(cpu_cycles)
    print(markdown_row)

    nb_threads.append(2**i)
    nb_cycles_app.append(cpu_cycles[0])

    speedup.append(nb_cycles_app[0]/cpu_cycles[0])
    nb_insts.append(extract_nb_instructions("stats1.txt")[0])

    IPC.append(nb_insts[i] / nb_cycles_app[i])


print("speedup : ", speedup)

print("IPC : ", IPC)

plt.plot(nb_threads, nb_cycles_app)

plt.xlabel("Nombre de threads")
plt.ylabel("Nombre de Cycles de l'application")

plt.legend()
plt.show()
