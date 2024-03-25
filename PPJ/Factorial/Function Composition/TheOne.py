class TheOne:
    def __init__(self, value):
        self.value = value
    
    def bind(self, func):
        self.value = func(self.value)
        return self
    
    def unwrap(self):
        return self.value

def get_user_input(_):  # Modified to accept an unused argument
    user_input = input("Unesite binarni niz (niz nula i jedinica): ")
    return user_input

def find_ones_indices(binary_string):
    indices = [i for i, bit in enumerate(binary_string) if bit == '1']
    return indices

def display_binary_string(binary_string, indices):
    output = ['X' if i in indices else '_' for i in range(len(binary_string))]
    return ''.join(output)

# Korak 1: Unos korisnika
binary_input = TheOne(None) \
    .bind(get_user_input) \
    .unwrap()

# Korak 2: Izračun pozicija jedinica
ones_indices = TheOne(binary_input) \
    .bind(find_ones_indices) \
    .unwrap()

# Korak 3: Ispis niza sa "_" za nule i "X" za jedinice
output_string = TheOne((binary_input, ones_indices)) \
    .bind(lambda x: display_binary_string(x[0], x[1])) \
    .unwrap()

print("Ispis niza sa '_' za nule i 'X' za jedinice:")
print(output_string)
