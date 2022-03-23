"""
While exploring an ancient tomb for treasure, you've come across a room with strange symbols on the floor. These symbols tell you which way you need to walk in order to pass through the room. However, you're not certain whether it's possible to follow these directions and reach the end of the room.

You will be given a grid of symbols like the following:

(start here --->)  >   >   >   >   v
                   v   ^   >   ^   v
                   >   ^   ^   >   E

You start on the square in the upper left, and need to reach the square marked "E". From each square you must follow the direction on the square. The directions are as follows:

 v : move down
 > : move right
 ^ : move up
 < : move left

In this case, you can reach the end square:

  [>] [>] [>] [>] [v]
   v   ^   >   ^  [v]
   >   ^   ^   >  [E]

However, the symbols may lead you off the edge.

  Right: off edge
   [>] [>] [v]
    v   ^  [>]
    <   >   E

Also, the end may not be at the bottom right.

 [>] [>] [v] [E]  v
  v   ^  [>] [^]  v
  >   ^   ^   >   >

The path is guaranteed not to loop.

Write a function that determines if it is possible to reach the end of the room from the start position in the upper left.

All Test Cases:
print(directed_march(floor1)   => True
directed_march(floor2)   => False
directed_march(floor3)   => True
directed_march(floor4)   => True
directed_march(floor5)   => False
directed_march(floor6)   => True
directed_march(floor7)   => False
directed_march(floor8)   => False
directed_march(floor9)   => True



"""

def directed_march(floors):
    row = 0
    col = 0
    while (row < len(floors) and row >= 0) and(col < len(floors[0]) and col >= 0):
                if floors[row][col] == "E":
                    return True
                elif floors[row][col] == ">":
                    col += 1
                elif floors[row][col] == "<":
                    col -= 1
                elif floors[row][col] == "^":
                    row -= 1
                elif floors[row][col] == "v":
                    row += 1            
    return False

floor0 = ['<', 'E']

floor1 = [
    ['>', '>', '>', '>', 'v'],
    ['v', '^', '>', '^', 'v'],
    ['>', '^', '^', '>', 'E']
]

floor2 = [
    ['v', '>', 'v'],
    ['v', '^', '>'],
    ['<', '>', 'E']
]

floor3 = [
    ['v', '>', '>', 'v', '>'],
    ['>', '>', 'v', '>', '^'],
    ['^', '>', '>', '>', 'E']
]

floor4 = [
    ['v', '>', '>', 'v'],
    ['v', '^', '>', '>'],
    ['v', '>', '>', 'v'],
    ['v', '^', '<', 'v'],
    ['>', '>', '^', 'E']
]

floor5 = [
    ['>', '>', '>', '>', '>', '>', '>', '>', '>', 'v'],
    ['v', '^', '>', 'v', '<', '>', 'v', '<', '<', '<'],
    ['>', '^', 'v', '<', '^', '<', '<', '^', '>', 'E']
]

floor6 = [
    ['>', '>', 'v', 'E', 'v'],
    ['v', '^', '>', '^', 'v'],
    ['>', '^', '^', '>', '>']
]

floor7 = [
    ['>', '>', 'v', '>', 'v'],
    ['v', '^', '>', '^', 'v'],
    ['>', 'E', '^', '>', '>']
]

floor8 = [
    ['>', '>', 'v', '>', '^'],
    ['v', '^', '>', '^', 'v'],
    ['>', 'E', '^', '>', '>']
]

floor9 = [
    ['>', 'v', '>', '>', 'v', '^'],
    ['v', '<', '^', 'v', '<', 'E'],
    ['>', '>', '^', '>', '>', '^']
]

print(directed_march(floor0)) # False
print(directed_march(floor1))   #=> True
print(directed_march(floor2))  #=> False
print(directed_march(floor3))   #=> True
print(directed_march(floor4))   #=> True
print(directed_march(floor5))   #=> False
print(directed_march(floor6))   #=> True
print(directed_march(floor7))   #=> False
print(directed_march(floor8))   #=> False
print(directed_march(floor9))   #=> True