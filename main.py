import time

class main():

    def __init__(self, TV_Status="OFF", TV_Volume=0, Channel_List=["BBC1"], Channel="BBC1"):
        print("Creating a remote controller")
        self.TV_Status = TV_Status
        self.TV_Volume = TV_Volume
        self.Channel_List = Channel_List
        self.Channel = Channel

    def TV_On(self):
        if self.TV_Status == "ON":
            print("TV is already on")
        else:
            print("TV is turning on")
            self.TV_Status = "ON"

    def TV_OFF(self):
        if self.TV_Status == "OFF":
            print("TV is already off")
        else:
            print("TV is turning OFF")
            self.TV_Status = "OFF"

    def Volume_Adjustment(self):
        while True:
            Answer = input("Volume Down: '-' \nVolume Up: '+' \nExit: 'exit'")
            if Answer == "-":
                if self.TV_Volume != 0:
                    self.TV_Volume -= 1
                    print("Volume: ", self.TV_Volume)
            elif Answer == "+":
                if self.TV_Volume != 50:
                    self.TV_Volume += 1
                    print("Volume", self.TV_Volume)
                else:
                    print("The sound level has reached the maximum.")
            elif Answer == "exit":
                break

    def Add_Channel(self, Channel_Name):
        print("Adding channel....")
        time.sleep(1)
        self.Channel_List.append(Channel_Name)
        print("Channel added")

    def __len__(self):
        return len(self.Channel_List)

    def __str__(self):
        return "TV Status: {}\nTV Volume: {}\nChannel List: {}\nWatching Channel: {}".format(self.TV_Status, self.TV_Volume, self.Channel_List, self.Channel)

Remote_Controller_1 = main()

print("""

    Remote Controller
      
      1. Turn on TV
      2. Turn off TV
      3. Volume Adjustment
      4. Add Channel
      5. Number of Channels
      6. TV Info

      for exit press Q


"""
)

while True:
    Operation = input("Choose the operation you want: ")

    if Operation == "Q" or Operation == "q":
        print("Program closing..")
        break

    elif Operation == "1":
        Remote_Controller_1.TV_On()

    elif Operation == "2":
        Remote_Controller_1.TV_OFF()
    
    elif Operation == "3":
        Remote_Controller_1.Volume_Adjustment()

    elif Operation == "4":
        Channel_Name = input("input channel name")
        Channel_List = Channel_Name.split(",")
        for adding in Channel_List:
            Remote_Controller_1.Add_Channel(adding)

    elif Operation == "5":
        print("Number of Channel: ", len(Remote_Controller_1))

    elif Operation == "6":
        print(Remote_Controller_1)

    else:
        print("Invalid operation")