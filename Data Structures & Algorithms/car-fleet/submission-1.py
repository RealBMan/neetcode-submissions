class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = {}

        for i in range(len(position)):
            pos_speed[position[i]] = speed[i]
        
        position.sort(reverse=True)
        speed_stack = []

        for i in range(len(position)):
            time = (target - position[i]) / pos_speed[position[i]]
            if len(speed_stack) == 0:
                speed_stack.append(time)
            elif speed_stack[-1] < time:
                speed_stack.append(time)
        print(speed_stack)
        
        return len(speed_stack)