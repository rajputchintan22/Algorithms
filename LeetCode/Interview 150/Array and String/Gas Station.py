'''if you start at a gas station and at any point your gas drops below zero, you cannot start from any gas station 
between your starting point and the point you ran out of gas. This is because the total gas gained minus the total cost to 
get to each next station was not enough to keep you going, meaning starting closer to your failure point won't help.'''
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1  # Not enough gas to complete the circuit
        start, tank = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1  # Reset start to the next station
                tank = 0  # Reset tank for the new starting point

        return start 
        