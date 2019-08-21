class Room():
    #def __init__(self, room_name,room_description):
    # 2 arguments self and desc,in python we do not have to give self argument to the method
    def __init__(self):  # will require user to input room name
        # (self.name)we are referring to a piece of data within the object
        #self.name= room_name
        self.name= None
        self.description = None # that they will start off with no value.
        self.linked_rooms= {}
    def set_description(self,room_description):
        self.description= room_description
    def get_description(self):
        return self.description
    def set_name(self,room_name):
        self.name= room_name
    def get_name(self):
        return self.name
    def describe(self):
        print(self.description)
    def link_rooms(self, room_to_link,direction):
        self.linked_rooms[direction]= room_to_link
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )
    def get_details(self):
        print('The '+ self.name+ '\n'+ self.description)
        #print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print('The '+ room.get_name() + ' is ' + direction)
