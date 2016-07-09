from sys import argv
from random import choice
from collections import defaultdict


class Maze(object):
    def __init__(self, width, height):
        """
        Init the maze

        Args:
            width (int): the maze width
            height (int): the maze height
        """
        self.width = width
        self.height = height
        self.maze, self.solution = self._generate()

    def _generate(self):
        """
        Generate the maze
        """
        maze = defaultdict(list)
        solution = None
        stack = [(0, 0)]

        while stack:
            x, y = stack[-1]

            if (x, y) == (self.width - 1, self.height - 1):
                solution = len(stack)

            # Pick only the sides inside the maze and with less than two open doors
            sides = [(_x, _y) for _x, _y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                     if _x >= 0 and _y >= 0 and _x < self.width and _y < self.height and len(maze[(_x, _y)]) < 2]

            # If there is no such side, pop the stack and keep looking and we're back at the start
            if not sides:
                stack.pop()
                continue

            # Open the door leading to the picked side both way
            side = choice(sides)
            maze[(x, y)].append(side)
            maze[side].append((x, y))

            # Add the picked side to the stack
            stack.append(side)

        return maze, solution

    def __str__(self):
        """
        Compute the string representation of the maze
        """
        output = ''

        for y in xrange(-1, self.height):
            for x in xrange(-1, self.width):
                if (x, y + 1) in self.maze[(x, y)] or x < 0:
                    output += ' '
                else:
                    output += '_'

                if (x + 1, y) in self.maze[(x, y)] or y < 0:
                    output += ' '
                else:
                    output += '|'

            output += '\n'

        output += '\nCan be solved in {} moves.'.format(self.solution)

        return output


def main(width, height):
    maze = Maze(width, height)

    print maze

if __name__ == "__main__":
    main(int(argv[1]) if len(argv) > 1 else 3, int(argv[2]) if len(argv) > 2 else 3)
