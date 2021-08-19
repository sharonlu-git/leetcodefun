class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Hypothesis: If robot doesn't make it back to starting point within 4 iterations of instructions, then it is not bound
        # Create initial values
        position = [0, 0]
        direction = 90 # In degrees 90-N, 0-E, 270-S, 180-W
        for iterations in range(4):
            # Loop through the instructions one time
            for instruction in instructions:
                if instruction == 'G': #Move Direction
                    if direction == 90: #North Moves the robot up the y axis by 1
                        position[1] += 1
                    elif direction == 0: #East Moves the robot up the x axis by 1
                        position[0] += 1
                    elif direction == 270:
                        position[1] -= 1
                    elif direction == 180:
                        position[0] -= 1
                elif instruction == 'L':
                    direction += 90
                    if direction > 270:
                        direction = 0
                else:
                    direction -= 90
                    if direction < 0:
                        direction = 270
            if position == [0, 0]:
                return True
        return False

