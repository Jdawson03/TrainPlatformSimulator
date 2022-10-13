import random as rand


class Station:
    def __init__(self):
        self.TheStation = []    # Creates a list of lists that can be used as the grid for a station map
        self.NoOfPlatforms = 0
        self.NoOfCarriages = 0  # Variables that help define the size of the map when it is created
        self.scale = 0  # kind of the zoom level, again to help with map creation
        self.StationName = ""
        self.StationCode = ""

    def ChooseStationStyle(self):
        choice = input("Would you like a single platform or double platform station layout? ")
        if choice[0].lower() == "s":
            self.BuildDefaultSinglePlatform()
        elif choice[0].lower() == "d":
            self.BuildDefaultDoublePlatform()
        elif choice[0].lower() == "c":
            self.BuildCustomPlatform()
        else:
            print("please try again naming the type of station you would like")
            self.ChooseStationStyle()

    def BuildDefaultSinglePlatform(self):
        self.StationName = "Chandlers Ford"
        self.StationCode = "CFR"
        self.NoOfPlatforms = 1
        self.NoOfCarriages = 6
        self.scale = 2
        for i in range(0, (self.scale * 2 * self.NoOfPlatforms)):
            row = []
            for j in range(0, (self.NoOfCarriages * self.scale) + 1):
                if i == (self.scale * 2) - 1:  # and j != (self.NoOfCarriages * self.scale) and j != 0:
                    row.append(Exit(i, j))
                elif j == 7 and i == 0:
                    row.append(Entrance(i, j))
                # row.append(Wall(i, j))
                elif (j == 3 and i == 1) or (j == 2 and i == 1) or (j == 2 and i == 0) or (j == 3 and i == 0):
                    row.append(Bench(i, j))
                elif j == 9 and (i == 1 or i == 0):
                    row.append(TicketMachine(i, j))
                else:
                    row.append(Cell(i, j))
            self.TheStation.append(row)
        self.BleedValues()
        return self

    def BuildDefaultDoublePlatform(self):
        self.StationName = "Whitchurch"
        self.StationCode = "WCH"
        self.NoOfPlatforms = 2
        self.NoOfCarriages = 8
        self.scale = 2
        for i in range(0, (self.scale * 2 * self.NoOfPlatforms)):  # determines height
            row = []
            for j in range(0, (self.NoOfCarriages * self.scale) + 1):  # determines length
                if i == (self.scale * 2) - 1 or i == (self.scale * 2):
                    row.append(Exit(i, j))
                elif (j == 7 and i == 0) or (j == 7 and i == (self.scale * 2 * self.NoOfPlatforms) - 1):
                    row.append(Entrance(i, j))
                elif (j == 3 and i == 1) or (j == 2 and i == 1) or (j == 2 and i == 0) or (j == 3 and i == 0):
                    row.append(Bench(i, j))
                elif j == 9 and (i == 1 or i == 0):
                    row.append(TicketMachine(i, j))
                elif j == 9 and (i == 6 or i == 7):
                    row.append(TicketMachine(i, j))
                elif (j == 3 and i == 6) or (j == 2 and i == 6) or (j == 2 and i == 7) or (j == 3 and i == 7):
                    row.append(Bench(i, j))
                else:
                    row.append(Cell(i, j))
            self.TheStation.append(row)
            self.BleedValues()

        return self

    def BuildCustomPlatform(self):
        self.StationName = input("What is this Station called? ")
        self.StationCode = input("What is this Station's 3 letter code? ")
        self.NoOfPlatforms = int(input("How many platforms does your station have?"))
        self.NoOfCarriages = int(input("How many carriages long are the platforms?"))
        self.scale = int(input("What scale would you like the simulation to be? 2 is considered normal."))
        for i in range(0, (self.scale * 2 * self.NoOfPlatforms)):  # determines height
            row = []
            n = 1
            for j in range(0, (self.NoOfCarriages * self.scale) + 1):  # determines length
                print(((2 * self.scale * n) - (self.scale + 1)), ((2 * self.scale * n) - self.scale))
                if i == ((2 * self.scale * n) - (self.scale + 1)) or i == ((2 * self.scale * n) - self.scale):
                    n += 1
                    print("oh no")
                    row.append(Exit(i, j))
                # elif i == (self.scale * 2) - 1 or i == (self.scale * 2):
                # row.append(Exit(i, j))
                elif (j == 7 and i == 0) or (j == 7 and i == (self.scale * 2 * self.NoOfPlatforms) - 1):
                    row.append(Entrance(i, j))
                elif (j == 3 and i == 1) or (j == 2 and i == 1) or (j == 2 and i == 0) or (j == 3 and i == 0):
                    row.append(Bench(i, j))
                elif j == 9 and (i == 1 or i == 0):
                    row.append(TicketMachine(i, j))

                elif j == 9 and (i == 6 or i == 7):
                    row.append(TicketMachine(i, j))

                elif (j == 3 and i == 6) or (j == 2 and i == 6) or (j == 2 and i == 7) or (j == 3 and i == 7):
                    row.append(Bench(i, j))
                else:
                    row.append(Cell(i, j))

            self.TheStation.append(row)
            self.BleedValues()
        return self


    def BleedValues(self):
        for item in self.TheStation:
            for items in item:
                if not items.name == "Entrance":
                    for i in self.TheStation:
                        for j in i:
                            if j.unique:
                                x = (((items.x - j.x) ** 2) ** 0.5)
                                y = (((items.y - j.y) ** 2) ** 0.5)
                                distance = x + y
                                if distance > 0:
                                    items.weight = items.weight + int(j.bleed / distance)
                                    # print(x, y, distance, j.bleed, j, items.weight)
        return self

    def UpdateExitStatus(self):
        pass

    def PrintGrid(self):
        for row in self.TheStation:
            for cell in row:
                print(cell.character, end=",")
            print("\n")
        print("\n")

    def PrintGridWeights(self):
        for row in self.TheStation:
            print("\n")
            for cell in row:
                print(cell.weight, end=",")
        print("\n")

    def PrintGridCoords(self):
        for row in self.TheStation:
            print("\n")
            for cell in row:
                print("(" + str(cell.y) + "," + str(cell.x) + ")", end=",")
        print("\n")

    def PrintGridOccupied(self):
        for row in self.TheStation:
            print("\n")
            for cell in row:
                print(cell.occupied, end=",")
        print("\n")

    def SaveStation(self):
        lines = [self.StationName, self.StationCode, str(self.NoOfPlatforms), str(self.NoOfCarriages), str(self.scale)]
        with open('Stations.txt', 'a') as f:
            for line in lines:
                f.write(line)
                f.write(',')
            for item in self.TheStation:
                f.write(str(item))

    def OpenPreviousStation(self):
        pass


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = self.x, self.y
        self.name = "Path"
        self.character = "\033[1;50;40m _ \033[0;0m"
        self.weight = 25
        self.bleed = 0
        self.unique = False
        self.occupied = False
        self.IsExit = False


class TicketMachine(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "TicketMachine"
        self.character = "\033[2;32;43m $ \033[0;0m"
        self.weight = 100
        self.bleed = 25
        self.unique = True


class Bench(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Bench"
        self.character = "\033[2;35;40m B \033[0;0m"
        self.weight = 50
        self.bleed = 13
        self.unique = True


class Entrance(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Entrance"
        self.character = "\033[1;36;40m : \033[0;0m"
        self.weight = 0
        self.unique = True


class Wall(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Wall"
        self.character = "X"
        self.weight = 0
        self.unique = True


class Exit(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Rail"
        self.character = "\033[5;31;40m = \033[0;0m"
        self.unique = True
        self.IsExit = True
        if self.IsExit:
            self.weight = 400
            self.bleed = 80
        else:
            self.weight = 0
            self.bleed = 20


class Customer:
    def __init__(self):
        self.recentlyVisited = []
        self.RouteTaken = []
        self.BenchPreference = rand.randrange(-80, 250)
        self.TicketMachinePreference = rand.randrange(-80, 250)
        self.currentx = int
        self.currenty = int
        self.location = object

    def SaveCustomer(self):
        pass

    def LoadCustomer(self):
        pass

    def WhereToStart(self, lst):
        entrances = []
        for i in lst:
            for j in i:
                if j.name == "Entrance":
                    entrances.append([j.x, j.y])
        N = rand.randint(0, len(entrances)) - 1
        choice = entrances.pop(N)
        self.currentx = choice[1]
        self.currenty = choice[0]

    def CalcRecentlyVisited(self, lst):
        if len(self.recentlyVisited) < 2:  # a number bigger allows the customer to get stuck and permaently loop
            self.recentlyVisited.append(lst[self.currenty][self.currentx])
        else:
            self.recentlyVisited.pop(0)
            self.recentlyVisited.append(lst[self.currenty][self.currentx])
        #print(self.recentlyVisited)

    def CalcRouteTaken(self, lst):
        self.RouteTaken.append(lst[self.currenty][self.currentx])
        self.DisplayRouteTaken()

    def DisplayRouteTaken(self):
        for i in self.RouteTaken:
            i.character = "\033[3;30;42m V \033[0;0m"

    def Move(self, lst):
        self.WhereToStart(lst)
        while self.StopMoving():
            total = 0
            try:
                if not lst[self.currenty - 1][self.currentx].occupied and self.currenty - 1 != -1:
                    n = lst[self.currenty - 1][self.currentx].weight
                    #print("n = ", n)
                    if lst[self.currenty - 1][self.currentx].name == "Bench":
                        n = n + self.BenchPreference
                    elif lst[self.currenty - 1][self.currentx].name == "TicketMachine":
                        n = n + self.TicketMachinePreference
                    #print(n)
                    total = total + n
                else:
                    n = 0
                    total = total + 0
            except IndexError:
                n = 0
                total = total + 0
            try:
                if not lst[self.currenty][self.currentx + 1].occupied and self.currentx + 1 != -1:
                    e = lst[self.currenty][self.currentx + 1].weight
                    if lst[self.currenty][self.currentx + 1].name == "Bench":
                        e = e + self.BenchPreference
                    elif lst[self.currenty][self.currentx + 1].name == "TicketMachine":
                        e = e + self.TicketMachinePreference
                    total = total + e
                else:
                    e = 0
                    total = total + 0
            except IndexError:
                e = 0
                total = total + 0
            try:
                if not lst[self.currenty + 1][self.currentx].occupied and self.currenty + 1 != -1:
                    s = lst[self.currenty + 1][self.currentx].weight
                    if lst[self.currenty + 1][self.currentx].name == "Bench":
                        s = s + self.BenchPreference
                    elif lst[self.currenty + 1][self.currentx].name == "TicketMachine":
                        s = s + self.TicketMachinePreference
                    total = total + s
                else:
                    s = 0
                    total = total + 0
            except IndexError:
                s = 0
                total = total + 0
            try:
                if not lst[self.currenty][self.currentx - 1].occupied and self.currentx - 1 != -1:
                    w = lst[self.currenty][self.currentx - 1].weight
                    if lst[self.currenty][self.currentx - 1].name == "Bench":
                        w = w + self.BenchPreference
                    elif lst[self.currenty][self.currentx - 1].name == "TicketMachine":
                        w = w + self.TicketMachinePreference
                    total = total + w
                else:
                    pass
            except IndexError:
                pass

            num = rand.randint(1, total)
            if 0 < num <= n:  # North
                if lst[self.currenty - 1][self.currentx] not in self.recentlyVisited:
                    self.CalcRecentlyVisited(lst)
                    self.CalcRouteTaken(lst)
                    lst[self.currenty][self.currentx].weight = (lst[self.currenty][self.currentx].weight // 3) + 1
                    self.currenty = self.currenty - 1
                    self.location = lst[self.currenty][self.currentx]
            elif n < num <= (n + e):  # East
                if lst[self.currenty][self.currentx + 1] not in self.recentlyVisited:
                    self.CalcRecentlyVisited(lst)
                    self.CalcRouteTaken(lst)
                    lst[self.currenty][self.currentx].weight = (lst[self.currenty][self.currentx].weight // 3) + 1
                    self.currentx = self.currentx + 1
                    self.location = lst[self.currenty][self.currentx]
            elif (n + e) < num <= (n + e + s):  # South
                if lst[self.currenty + 1][self.currentx] not in self.recentlyVisited:
                    self.CalcRecentlyVisited(lst)
                    self.CalcRouteTaken(lst)
                    lst[self.currenty][self.currentx].weight = (lst[self.currenty][self.currentx].weight // 3) + 1
                    self.currenty = self.currenty + 1
                    self.location = lst[self.currenty][self.currentx]
            elif (n + e + s) < num <= total:  # West
                if lst[self.currenty][self.currentx - 1] not in self.recentlyVisited:
                    self.CalcRecentlyVisited(lst)
                    self.CalcRouteTaken(lst)
                    lst[self.currenty][self.currentx].weight = (lst[self.currenty][self.currentx].weight // 3) + 1
                    self.currentx = self.currentx - 1
                    self.location = lst[self.currenty][self.currentx]

    def StopMoving(self):
        try:
            if self.location.IsExit:
                #print("Onboard")
                self.PrintPosition()
                return False
            else:
                return True
        except AttributeError:
            return True

    def PrintPosition(self):
        print("Customer is located at: ", "x = ", self.currentx, "y = ", self.currenty)


def Menu(self):
    while input("Do you want to continue") == "y":
        print("1. Station Stuff \n 2. Customer Stuff")
        choice = int(input("what number option will you choose?"))
        if choice == 1:
            Station = Station()
            Station.ChooseStationStyle()
            Station.PrintGrid()
            print("Station Created")

        elif choice == 2:
            Joe = Customer()


        else:
            print("Please choose a number")


if __name__ == "__main__":
    Station = Station()
    Station.ChooseStationStyle()

    Joe = Customer()
    Joe.Move(Station.TheStation)

    Station.PrintGrid()
