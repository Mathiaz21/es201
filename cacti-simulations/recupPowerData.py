import re

def extract_power_values(file_path):
    # Définition des expressions régulières pour rechercher les valeurs mW
    regex_leakage_closed = r'Leakage Power Closed Page \(mW\): ([\d.]+)'
    regex_leakage_open = r'Leakage Power Open Page \(mW\): ([\d.]+)'
    regex_leakage_io = r'Leakage Power I/O \(mW\): ([\d.]+)'
    regex_refresh_power = r'Refresh power \(mW\): ([\d.e-]+)'
    regex_data_array = r'Total leakage read/write power of a bank \(mW\): ([\d.]+)'
    regex_tag_array = r'Total leakage read/write power of a bank \(mW\): ([\d.]+)'

    power_values = {}

    with open(file_path, 'r') as file:
        data = file.read()

        # Recherche des valeurs correspondantes aux expressions régulières
        power_values['Leakage Power Closed Page'] = float(re.search(regex_leakage_closed, data).group(1))
        power_values['Leakage Power Open Page'] = float(re.search(regex_leakage_open, data).group(1))
        power_values['Leakage Power I/O'] = float(re.search(regex_leakage_io, data).group(1))
        power_values['Refresh Power'] = float(re.search(regex_refresh_power, data).group(1))
        power_values['Data Array Power'] = float(re.search(regex_data_array, data).group(1))
        
        # Recherche de la deuxième occurrence pour Tag Array Power
        tag_array_match = re.findall(regex_tag_array, data)
        if len(tag_array_match) > 1:
            power_values['Tag Array Power'] = float(tag_array_match[1])

    return power_values


def sum_power_values(power_values):
    total_power = 0.0
    for key, value in power_values.items():
        total_power += value
    return total_power


# Utilisation du script
file_path = "A7L1output.txt"
power_values = extract_power_values(file_path)
print(power_values)
print(sum_power_values(power_values))

file_path = "A15L1output.txt"
power_values = extract_power_values(file_path)
print(power_values)
print(sum_power_values(power_values))