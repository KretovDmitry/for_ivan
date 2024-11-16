from hotel import Hotel

if __name__ == '__main__':
    hotel = Hotel('Four Seasons', 10)
    hotel.greeting()

    hotel.occupy(1)
    hotel.occupy(2)
    hotel.occupy(3)
    hotel.occupy(4)
    hotel.occupy(5)
    hotel.occupy(6)
    hotel.occupy(7)
    hotel.occupy(8)
    hotel.occupy(9)
    hotel.occupy(10)

    print(hotel.occupancy_rate())
    print(hotel.income())

    hotel.close()

    print(hotel.occupancy_rate())
    print(hotel.income())
