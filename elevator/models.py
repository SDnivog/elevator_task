from django.db import models

class Elevator(models.Model):
    is_running = models.BooleanField(default=False)
    is_door_open = models.BooleanField(default=False)
    current_floor = models.IntegerField(default=0)
    is_operational = models.BooleanField(default=True)

    def move_up(self):
        self.current_floor += 1

    def move_down(self):
        self.current_floor -= 1

    def open_door(self):
        self.is_door_open = True

    def close_door(self):
        self.is_door_open = False

    def start_running(self):
        self.is_running = True

    def stop_running(self):
        self.is_running = False

    def display_status(self):
        print(f"Current floor: {self.current_floor}")
        print(f"Is door open: {self.is_door_open}")
        print(f"Is running: {self.is_running}")

class ElevatorSystem(models.Model):
    elevators = models.ManyToManyField(Elevator)
    floors = models.IntegerField(default=0)

    def assign_elevator_to_floor(self, floor):
        # Assign the closest available elevator to the floor
        available_elevators = self.elevators.filter(is_operational=True, is_running=False)
        if not available_elevators:
            return None

        closest_elevator = min(available_elevators, key=lambda e: abs(e.current_floor - floor))
        closest_elevator.start_running()
        return closest_elevator

    def assign_optimal_elevator_to_user(self, floor, direction):
        # Assign the most optimal elevator to the user according to their request
        available_elevators = self.elevators.filter(is_operational=True, is_running=False)
        if not available_elevators:
            return None

        # Find elevators that are on the same floor and going in the same direction as the user
        same_direction_elevators = [e for e in available_elevators if (e.current_floor == floor and ((direction == "up" and e.move_up) or (direction == "down" and e.move_down)))]
        if same_direction_elevators:
            return min(same_direction_elevators, key=lambda e: abs(e.current_floor - floor))

        # Find elevators that are on the same floor but going in the opposite direction as the user
        opposite_direction_elevators = [e for e in available_elevators if (e.current_floor == floor and ((direction == "up" and e.move_down) or (direction == "down" and e.move_up)))]
        if opposite_direction_elevators:
            return min(opposite_direction_elevators, key=lambda e: abs(e.current_floor - floor))

        # Find elevators that are not on the same floor but going in the same direction as the user
        same_direction_not_on_same_floor_elevators = [e for e in available_elevators if ((direction == "up" and e.move_up) or (direction == "down" and e.move_down))]
        if same_direction_not_on_same_floor_elevators:
            return min(same_direction_not_on_same_floor_elevators, key=lambda e: abs(e.current_floor - floor))

        # Find elevators that are not on the same floor but going in the opposite direction as the user
        opposite_direction_not_on_same_floor_elevators = [e for e in available_elevators if ((direction == "up" and e.move_down) or (direction == "down" and e.move_up))]
        if opposite_direction_not_on_same_floor_elevators:
            return min(opposite_direction_not_on_same_floor_elevators, key=lambda e: abs(e.current_floor - floor))

        return None
