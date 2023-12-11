# https://adventofcode.com/2023/day/9
# --- Day 9: Mirage Maintenance ---
# Of course, it would be nice to have even more history included in your report. Surely it's safe to just extrapolate backwards as well, right?

# For each history, repeat the process of finding differences until the sequence of differences is entirely zero. Then, rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

# In particular, here is what the third example history looks like when extrapolating back in time:

# 5  10  13  16  21  30  45
#   5   3   3   5   9  15
#    -2   0   2   4   6
#       2   2   2   2
#         0   0   0
# Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: 5.

# Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the second history. Adding all three new values together produces 2.

# Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these extrapolated values?

# Part Two

from os import path


class Solution():
    def __init__(self):
        self.input = []
        with open(path.join(path.dirname(__file__), "09-mirage-maintenance-input.txt")) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split(" ")
                integers = []
                for num in line:
                    integers.append(int(num))
                self.input.append(integers)

    def get_diffs(self):
        diffs = []
        for history in self.input:
            all_diffs = [history]
            read_diffs = history
            while read_diffs.count(0) < len(read_diffs):
                write_diffs = []
                i = 0
                while i < len(read_diffs) - 1:
                    this_diff = int(read_diffs[i+1]) - int(read_diffs[i])
                    write_diffs.append(this_diff)
                    i += 1
                read_diffs = write_diffs
                all_diffs.append(read_diffs)
            diffs.append(all_diffs)
        return diffs

    def predict_next_values(self, diffs):
        predictions = []
        for all_diffs in diffs:
            i = len(all_diffs) - 1
            prediction = 0
            while i >= 0:
                prediction += all_diffs[i][-1]
                i -= 1
            predictions.append(prediction)
        return predictions

    def predict_prev_values(self, diffs):
        predictions = []
        for all_diffs in diffs:
            i = len(all_diffs) - 1
            prediction = 0
            while i > 0:
                prediction = all_diffs[i-1][0] - prediction
                i -= 1
            predictions.append(prediction)
        return predictions

    def get_answer(self):
        diffs = self.get_diffs()
        predictions = self.predict_prev_values(diffs)
        print(sum(predictions))


def get_solution():
    solution = Solution()
    solution.get_answer()


if __name__ == '__main__':
    get_solution()
