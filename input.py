
def int_input(message, min, max):
    """Asks user to enter an integer between min and max."""
    while True:
        n = input(message)
        if n.isdigit():
            n = int(n)
        else:
            continue

        if min <= n <= max:
            return n
        
user_input = int_input("Entrez un nombre entre 10 et 20: ", 10, 20)
print("L'utilisateur a choisi le nombre:", user_input)