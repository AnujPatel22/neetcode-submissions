class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_positions = sorted([(p,s) for p,s in zip(position, speed)], key= lambda t: -t[0])
        individual_times = [(target - p) / s for p, s in sorted_positions]

        num_fleets = 0
        last_fleet_time = 0

        for time in individual_times:

            if time > last_fleet_time:
                #new fleet
                num_fleets += 1
                last_fleet_time = time
            
        return num_fleets 