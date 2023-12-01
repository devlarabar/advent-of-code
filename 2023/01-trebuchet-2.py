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

# Part Two

from os import path


class Solution():
    word_nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    def __init__(self):
        self.input = []
        with open(path.join(path.dirname(__file__), "01-trebuchet-input.txt")) as f:
            for line in f:
                line = line.strip()
                self.input.append(line)

    def get_line_sums(self):
        self.line_sums = []

        for i in range(len(self.input)):
            indexes = []
            for num in self.word_nums.keys():
                if num in self.input[i]:
                    indexes.append(self.input[i].index(num))
                    indexes.append(self.input[i].rindex(num))
                if str(self.word_nums[num]) in self.input[i]:
                    indexes.append(self.input[i].index(
                        str(self.word_nums[num])))
                    indexes.append(self.input[i].rindex(
                        str(self.word_nums[num])))
            indexes = sorted(indexes)

            first_digit = self.input[i][indexes[0]]
            if not first_digit.isdigit():
                j = indexes[0]
                temp_str = ""
                while not temp_str in self.word_nums:
                    temp_str += self.input[i][j]
                    j += 1
                first_digit = self.word_nums[temp_str]

            last_digit = self.input[i][indexes[-1]]
            if not last_digit.isdigit():
                j = indexes[-1]
                temp_str = ""
                while not temp_str in self.word_nums:
                    temp_str += self.input[i][j]
                    j += 1
                last_digit = self.word_nums[temp_str]

            line_sum = int(str(first_digit) + str(last_digit))

            self.line_sums.append(line_sum)

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
