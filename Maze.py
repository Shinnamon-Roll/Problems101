from collections import deque

def maze_solver(maze, portals):
    # ค้นหาตำแหน่ง 'S' และ 'E'
    start, end = None, None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'E':
                end = (i, j)
    
    # ถ้าไม่เจอ 'S' หรือ 'E' ให้คืนค่า -1
    if not start or not end:
        return -1, []
    
    # BFS setup
    queue = deque([(start[0], start[1], 0, [start])])  # queue เก็บ (x, y, distance, path)
    visited = set()
    visited.add(start)

    # การเคลื่อนที่ใน 4 ทิศทาง
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS loop
    while queue:
        x, y, dist, path = queue.popleft()

        # ถ้าถึงจุด 'E' ให้คืนค่าระยะทางและเส้นทาง
        if (x, y) == end:
            return dist, path

        # สำรวจ 4 ทิศทาง
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and (nx, ny) not in visited:
                if maze[nx][ny] == '.' or maze[nx][ny] == 'E':
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1, path + [(nx, ny)]))

        # ตรวจสอบพอร์ทัล
        portal_key = f'({x}, {y})'
        if portal_key in portals:
            px, py = portals[portal_key]
            if (px, py) not in visited:
                visited.add((px, py))
                queue.append((px, py, dist, path + [(px, py)]))  # เทเลพอร์ตโดยไม่เพิ่มระยะทาง

    # ถ้าหาไม่เจอเส้นทาง
    return -1, []

# ตัวอย่างที่ 1
maze1 = [
    ['S', '.', '.', 'P'],
    ['#', '#', '.', '#'],
    ['P', '.', '.', 'E'],
    ['#', '#', '#', '#']
]
portals1 = {
    '(0, 3)': (2, 0),
    '(2, 0)': (0, 3)
}
distance1, path1 = maze_solver(maze1, portals1)
print(f"Distance: {distance1}, Path: {path1}")

# ตัวอย่างที่ 2
maze2 = [
    ['S', '.', '#', 'P', '#', 'P'],
    ['#', '.', '#', '.', '#', '.'],
    ['#', '.', 'P', '.', '.', 'E'],
    ['P', '#', '#', '#', '#', '#'],
    ['#', '.', '.', 'P', '.', '.']
]
portals2 = {
    '(0, 3)': (3, 0),
    '(3, 0)': (0, 3),
    '(0, 5)': (2, 2),
    '(2, 2)': (0, 5)
}
distance2, path2 = maze_solver(maze2, portals2)
print(f"Distance: {distance2}, Path: {path2}")

# ตัวอย่างที่ 3
maze3 = [
    ['S', 'P', '.', '.', 'E'],
    ['#', '#', '#', '#', '#'],
    ['P', '.', '.', '.', 'P']
]
portals3 = {
    '(0, 1)': (2, 0),
    '(2, 0)': (0, 1),
    '(2, 4)': (0, 1)
}
distance3, path3 = maze_solver(maze3, portals3)
print(f"Distance: {distance3}, Path: {path3}")
