# https://adventofcode.com/2023/day/3
# --- Day 3: Gear Ratios ---
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

# Your puzzle answer was 521515.

# The first half of this puzzle is complete! It provides one gold star: *

# Part One:

from os import path


class Solution():

    not_symbols = ".0123456789"

    def __init__(self):
        self.input = []
        self.coords = {}
        self.sum_part_numbers = 0
        self.line_length = 0
        with open(path.join(path.dirname(__file__), "03-gear-ratios-input.txt")) as f:
            for line in f:
                line = line.strip()
                self.input.append(line)
        self.get_line_length()

    def get_line_length(self):
        self.line_length = len(self.input[0])
        return len(self.input[0])

    def get_digits(self):
        i = 0
        for line_num, line in enumerate(self.input):
            temp_str = ""
            indexes = []
            for index, char in enumerate(line):
                if char.isdigit():
                    temp_str += char
                    indexes.append(index)
                    if index == self.line_length-1:
                        self.coords[f"{temp_str}-{i}"] = [line_num, min(
                            indexes), max(indexes)]  # Line, start, end
                        temp_str = ""
                        indexes = []
                        i += 1
                else:
                    if len(temp_str) > 0:
                        self.coords[f"{temp_str}-{i}"] = [line_num, min(
                            indexes), max(indexes)]  # Line, start, end
                        temp_str = ""
                        indexes = []
                        i += 1

    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[0] > len(self.input) - 1:
            return False
        if coord[1] < 0 or coord[1] > self.line_length - 1:
            return False
        return True

    def check_adjacency(self):
        self.adjacent_coords = {}
        for num, coord in self.coords.items():
            adjacency_range = [coord[1]-1, coord[2]+1]
            left = [coord[0], coord[1]-1]
            right = [coord[0], coord[2]+1]
            all_coords = []
            for x in range(adjacency_range[0], adjacency_range[1]+1):
                all_coords.append([coord[0]-1, x])
                all_coords.append([coord[0]+1, x])
            all_coords.append(left)
            all_coords.append(right)

            valid_coords = [
                c for c in all_coords if self.is_valid_coord(c)]
            self.adjacent_coords[num] = valid_coords

    def get_answer(self):
        nums_to_sum = []
        for num, coords in self.adjacent_coords.items():
            for coord in coords:
                if self.input[coord[0]][coord[1]] not in self.not_symbols:
                    num_actual = num.split("-")[0]
                    nums_to_sum.append(num_actual)
                    self.sum_part_numbers += int(num_actual)
        print("Answer: ", self.sum_part_numbers)

    def print_input(self):
        print(self.input)


def get_solution():
    solution = Solution()
    solution.get_digits()
    solution.check_adjacency()
    solution.get_answer()


if __name__ == '__main__':
    get_solution()
