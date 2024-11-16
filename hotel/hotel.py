from datetime import date
from hotel.exceptions import NoSuchRoomError
from hotel.room import Room
from hotel.currency import Dollar
from typing import List

DEFAULT_COST = 200


class Hotel:
    def __init__(self, name: str, num_of_rooms: int):
        self.__name: str = name
        self.__num_of_rooms: int = num_of_rooms
        self.__rooms: List[Room] = []
        self.open()

    def occupy(self, room: int, d: date = date.today()):
        self.validate_room(room)
        self.__rooms[room - 1].occupy(d)

    def book(self, room: int, d: date = date.today()):
        self.validate_room(room)
        self.__rooms[room - 1].book(d)

    def free(self, room: int, d: date = date.today()):
        self.validate_room(room)
        self.__rooms[room - 1].free(d)

    def occupancy_rate(self, d: date = date.today()) -> float:
        if len(self.__rooms) == 0:
            return 0.0

        return len([0 for room in self.__rooms if room.is_occupied(d)]) / len(self.__rooms)

    def open(self):
        self.__rooms = [Room(room_id + 1, DEFAULT_COST) for room_id in range(self.__num_of_rooms)]

    def close(self):
        self.__rooms = []

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_num_of_rooms(self) -> int:
        return self.__num_of_rooms

    def set_room_cost(self, room: int, cost: float):
        self.validate_room(room)
        self.__rooms[room - 1].set_cost(cost)

    def income(self, d: date = date.today()) -> Dollar:
        return Dollar(sum([room.get_cost() for room in self.__rooms if room.is_occupied(d)]))

    def validate_room(self, room: int):
        if room <= 0 or room > self.__num_of_rooms:
            raise NoSuchRoomError(room)

    def greeting(self):
        print(f'Welcome to the {self.get_name()} hotel!!!')
        print(f'We have {self.get_num_of_rooms()} rooms in total.')
