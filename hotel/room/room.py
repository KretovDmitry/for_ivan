from datetime import date
from hotel.exceptions import RoomIsAlreadyOccupied, RoomIsAlreadyBooked, InvalidCost
from typing import Dict


class RoomStates:
    FREE = 0
    OCCUPIED = 1
    BOOKED = 2


DEFAULT_COST = 200


class Room:
    def __init__(self, room_number: int, cost: float = DEFAULT_COST):
        self.__room_number: int = room_number
        self.__cost: float = cost
        self.dates: Dict = dict()

    def occupy(self, d: date = date.today()):
        if self.is_booked(d):
            raise RoomIsAlreadyBooked(self.__room_number)

        if self.is_occupied(d):
            raise RoomIsAlreadyOccupied(self.__room_number)

        self.dates[d.isoformat()] = RoomStates.OCCUPIED

    def is_occupied(self, d: date = date.today()) -> bool:
        if d.isoformat() not in self.dates:
            return False

        return self.dates[d.isoformat()] == RoomStates.OCCUPIED

    def book(self, d: date = date.today()):
        if d.day == date.today().day and self.is_occupied(d):
            raise RoomIsAlreadyOccupied(self.__room_number)

        if self.is_booked(d):
            raise RoomIsAlreadyBooked(self.__room_number)

        self.dates[d.isoformat()] = RoomStates.BOOKED

    def is_booked(self, d: date = date.today()) -> bool:
        if d.isoformat() not in self.dates:
            return False

        return self.dates[d.isoformat()] == RoomStates.BOOKED

    def free(self, d: date = date.today()):
        if d.isoformat() in self.dates:
            self.dates[d.isoformat()] = RoomStates.FREE

    def get_cost(self) -> float:
        return self.__cost

    def set_cost(self, cost: float):
        if cost < 0:
            raise InvalidCost(cost)

        self.__cost = cost

    def get_number(self) -> int:
        return self.__room_number
