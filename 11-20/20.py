def transposeMatrix(matrix: list[list[int]]) -> list[list[int]]:
    for i in matrix:
        for j in matrix[0]:
            print([i][j])

def main():
   matrix1 = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]

    results = transposeMatrix(matrix1)
    print(results)
main()
