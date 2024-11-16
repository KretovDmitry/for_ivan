from datetime import date


class NoSuchRoomError(Exception):
    def __init__(self, room: int):
        super().__init__('No such room', dict([("room", room)]))


class RoomIsAlreadyOccupied(Exception):
    def __init__(self, room: int):
        super().__init__('Room is already occupied', dict([("room", room)]))


class RoomIsAlreadyBooked(Exception):
    def __init__(self, room: int):
        super().__init__('Room is already booked', dict([("room", room)]))


class CannotOccupyRoom(Exception):
    def __init__(self, room: int, d: date):
        super().__init__('Cannot occupy room', dict([("room", room), ("date", d.isoformat())]))


class InvalidCost(Exception):
    def __init__(self, cost: float):
        super().__init__('Invalid cost', dict([("cost", cost)]))
