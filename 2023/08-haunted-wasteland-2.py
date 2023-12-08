# https://adventofcode.com/2023/day/8
# --- Day 8: Haunted Wasteland ---
# The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

# What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

# After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

# For example:

# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
# Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

# Step 0: You are at 11A and 22A.
# Step 1: You choose all of the left paths, leading you to 11B and 22B.
# Step 2: You choose all of the right paths, leading you to 11Z and 22C.
# Step 3: You choose all of the left paths, leading you to 11B and 22Z.
# Step 4: You choose all of the right paths, leading you to 11Z and 22B.
# Step 5: You choose all of the left paths, leading you to 11B and 22C.
# Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
# So, in this example, you end up entirely on nodes that end in Z after 6 steps.

# Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?

# Part Two

from os import path
import math


class Solution():
    def __init__(self):
        self.input = {}
        self.directions = []
        self.a = []
        self.z = []
        with open(path.join(path.dirname(__file__), "08-haunted-wasteland-input.txt")) as f:
            lines = f.readlines()
            for line in lines:
                if "=" in line:
                    line_pretty = line.replace(" = ", ", ").replace(
                        "(", "").replace(")", "").replace("\n", "").split(", ")
                    key = line_pretty[0]
                    self.input[key] = [
                        line_pretty[1], line_pretty[2]]
                    if key[-1] == "A":
                        self.a.append(key)
                    elif key[-1] == "Z":
                        self.z.append(key)
                else:
                    if line != "\n":
                        self.directions = list(line)[0:len(line)-1]
            print("All A's: ", self.a)
            print("All Z's: ", self.z)

    def get_answer(self):
        steps = 0
        dir_index = {
            "L": 0,
            "R": 1
        }
        all_steps = []
        for i in range(len(self.a)):
            steps = 0
            while self.a[i][-1] != "Z":
                current_key = self.a[i]
                next_key = self.input[current_key][dir_index[self.directions[steps]]]
                self.a[i] = next_key
                self.directions.append(self.directions[steps])
                steps += 1
            all_steps.append(steps)
        print("Answer: ", math.lcm(*all_steps))


def get_solution():
    solution = Solution()
    solution.get_answer()


if __name__ == '__main__':
    get_solution()
