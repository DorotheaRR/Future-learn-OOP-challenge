from room import Room

kitchen = Room()
kitchen.set_name('Kitchen')
kitchen.set_description('Lots of devices in this room')
#kitchen.get_description()
#kitchen.describe()

dining_hall = Room()
dining_hall.set_name('Dining Hall')
dining_hall.set_description('Used thrice a day')
#dining_hall.describe()

ballroom= Room()
ballroom.set_name('Ballroom')
ballroom.set_description('Dont be surprised if empty')
#ballroom.describe()

kitchen.link_rooms(dining_hall,'south')
dining_hall.link_rooms(kitchen,'north')
dining_hall.link_rooms(ballroom,'west')
ballroom.link_rooms(dining_hall,'east')

dining_hall.get_details()
kitchen.get_details()
ballroom.get_details()


