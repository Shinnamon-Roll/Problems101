def calculate_total_cost(fried_eggs: int, omelets: int, boiled_eggs: int) -> int:
    return (fried_eggs * 7) + (omelets * 10) + (boiled_eggs * 5)

def main():
    fried_eggs = int(input("Enter the number of Fried Eggs: "))
    omelets = int(input("Enter the number of Omelets: "))
    boiled_eggs = int(input("Enter the number of Boiled Eggs: "))
    
    total_cost = calculate_total_cost(fried_eggs, omelets, boiled_eggs)
    print(f"Total cost: {total_cost} Baht")

main()
