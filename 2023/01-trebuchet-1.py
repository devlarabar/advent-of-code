# https://adventofcode.com/2023/day/1
# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

# Part One

from os import path


class Solution():
    def __init__(self):
        self.input = []
        with open(path.join(path.dirname(__file__), "01-trebuchet-input.txt")) as f:
            for line in f:
                line = line.strip()
                self.input.append(line)

    def get_line_sums(self):
        self.line_sums = []
        for line in self.input:
            digits = list(filter(lambda char: char.isdigit(), line))
            if len(digits) >= 2:
                line_sum = int(digits[0] + digits[-1])
            else:
                line_sum = int(2 * digits[0])
            self.line_sums.append(line_sum)
            print(line_sum)

    def get_sum(self):
        answer = sum(self.line_sums)
        print(answer)
        return answer


def get_solution():
    solution = Solution()
    solution.get_line_sums()
    solution.get_sum()


if __name__ == '__main__':
    get_solution()
