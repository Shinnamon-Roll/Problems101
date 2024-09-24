def calculateParkingFee(hours: int, minutes: int) -> int:
    if minutes >= 1:
        return hours * 50
    elif minutes == 0:
        return (hours - 1) * 50
def main():
    hours, minutes = input("Enter hours and minutes : ").split('.')
    hours = int(hours)
    minutes = int(minutes)
    
    result = (calculateParkingFee(hours, minutes))
    print(result)

main()