def calculateNumberOfSongs(hours: float, avgSongLength: float = 3.5) -> int:
    return (hours * 60) / avgSongLength

def main():
    hours = int(input("Enter time : "))
    avgSongLength = int(input("Enter Average song length : "))

    result = calculateNumberOfSongs(hours, avgSongLength)
    print(f"You can listen {result:.0f} songs.")

main()