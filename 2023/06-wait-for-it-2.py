# https://adventofcode.com/2023/day/6
# --- Day 6: Wait For It ---
# As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

# So, the example from before:

# Time:      7  15   30
# Distance:  9  40  200
# ...now instead means this:

# Time:      71530
# Distance:  940200
# Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

# How many ways can you beat the record in this one much longer race?

# Part Two

from os import path


class Solution():
    def __init__(self):
        self.input = {}
        with open(path.join(path.dirname(__file__), "06-wait-for-it-input.txt")) as f:
            lines = "".join(f.readlines()).split("\n")
            self.input["time"] = int(lines[0].split(":")[1].replace(" ", ""))
            self.input["distance"] = int(
                lines[1].split(":")[1].replace(" ", ""))
            print(self.input)

    def find_ways(self):
        time = self.input["time"]
        record_distance = self.input["distance"]
        ms = 1
        self.ways_to_win = 0
        while ms < time:
            time_remaining = time - ms
            distance_traveled = ms * time_remaining
            if distance_traveled > record_distance:
                self.ways_to_win += 1
            ms += 1

    def get_answer(self):
        self.find_ways()
        print(self.ways_to_win)


def get_solution():
    solution = Solution()
    solution.get_answer()


if __name__ == '__main__':
    get_solution()
