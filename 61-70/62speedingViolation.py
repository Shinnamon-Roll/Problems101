def calculateSpeedingFine(speed: float, speedLimit: float) -> str:
    mySpeedLimit = {90: 500, 121: 1000, 141: 1500, 160: 2000}
    for speeds, fine in reversed(sorted(mySpeedLimit.items())):
        if speed >= speeds:
            return fine
        elif speed < speeds:
            return "no fine"
            

def main():

    speed = float(input("Enter your speed : "))

    result = calculateSpeedingFine(speed, None)
    print(f"your fine is : {result}")

main()