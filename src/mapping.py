from room import Room, Thunder_Dome
from item import Item, Container, SlingShot, Rocks, Berries

# Declare rooms in rooms dict.
rooms = {
    'empty_highway': Room("\nYou see an empty highway.",
                      "To the North, you see a puppy trotting along a narrow trail. \nTo the South, your see a parking lot"),

    'parking_lot': Room("You head towards the lot trying to remember how you got there.",
                "All of a sudden you see this horrific scene of a six car pile up.\nYou must return back North"),

    'narrow_trail': Room("The trail has lead you to still lake.",
                         "You hear in the North a rapid river running \nTo the East of you there is a stone path.\nTo the West is an old trail overgrown with plant life. \nTo the south you see a dark parking lot and remember you have a parking_lot."),

    'river_bank': Room("You come to a raging river that is quite wide.",
                       "Attempt to ford the river by heading North \nHead upstream to the East \nMove toward the "
                       "Puget Sound by heading downstream, to the West. \nGo back toward the start by moving South"),

    'stone_path': Thunder_Dome("A chill fills the air... as you come to an opening and are at the foot of a steep mountian",
                        "Continue east and climb the mountain. \nCross rickety suspension bridge to the North. \nSouth you see a long abandoned road that is in disarray. \nThe narrow path is to your west"),

    'old_trail': Room("The trail forks at a granite outcropping.",
                       "A short climb West looks like the entrance to a cave. \nThe trail continues both North and "
                       "South. \nGo back to the narrow to the East"),

    'suspension_bridge': Room("You just barely made it across the bridge and start to feel the earth shake beneath you feet.",
                           "All of a sudden you see an avalanche and quickly move just missing certian doom. \nYou must return to the South"),

    'abandoned_road': Room("This difficult trail seems to go on forever.",
                      "Continue into the unknown up another steep climb to the South. \nGive up and return to easier "
                      "territory by heading North"),

    'mountain_east': Room("You feel on top of the world, while enjoying the view and the accomplishment of the climb.",
                          "Only way down is to the West"),

    'valley': Room("The forest starts to part ways as you come to a majestic valley.",
                     "The trail ends here. \nYou must head back South"),

    'dense_forest': Room("The forest start to darken as you begin to hear creepy forest sounds.",
                         "You start to realize that you will never find your way out if you go any further. \nYour only choice is to turn back to the North"),

    'cave': Room("The cave seems endless and you are afraid of what could be living in it",
                 "Go East to climb back down"),

    'choppy_waters': Room("The river is moving much faster than you expected",
                         "You better head back south before you die"),

    'small_pond': Room("The water is extremely cold but you forge through. You loose 10 health.",
                             "Head East to reach a bridge. \nGo West to return to the river bank."),

    'steel_bridge': Room("You come to a steel bridge that appears to be in great condition. Just then you see the puppy you saw at the start of your journey "
                            "rest-stop!",
                            "Go North to approach the puppy. \nReturn South to the steel bridge you just crossed"),

    'rapid_river': Room("You smell the crisp air of a clean flowing river.",
                        "As you come to the river you realize that you must go back east. \nThe river is far to wide to cross"),

    'road_block': Room("You have come to end of the road and cannot go any further",
                         "You must go back North"),

    'puppy_dog': Room("You approach the puppy and it starts to wag its tail \n You are happy but...",
                  "South is the only way to go.")

}

# Connect rooms.
rooms['empty_highway'].to_s = rooms['parking_lot']
rooms['empty_highway'].to_n = rooms['narrow_trail']

rooms['parking_lot'].to_n = rooms['empty_highway']


rooms['narrow_trail'].to_n = rooms['river_bank']
rooms['narrow_trail'].to_e = rooms['stone_path']
rooms['narrow_trail'].to_w = rooms['old_trail']
rooms['narrow_trail'].to_s = rooms['empty_highway']

rooms['stone_path'].to_n = rooms['suspension_bridge']
rooms['stone_path'].to_e = rooms['mountain_east']
rooms['stone_path'].to_s = rooms['abandoned_road']
rooms['stone_path'].to_w = rooms['narrow_trail']

rooms['old_trail'].to_n = rooms['valley']
rooms['old_trail'].to_w = rooms['cave']
rooms['old_trail'].to_s = rooms['dense_forest']
rooms['old_trail'].to_e = rooms['narrow_trail']

rooms['suspension_bridge'].to_s = rooms['stone_path']

rooms['abandoned_road'].to_n = rooms['stone_path']
rooms['abandoned_road'].to_s = rooms['road_block']

rooms['road_block'].to_n = rooms['abandoned_road']

rooms['mountain_east'].to_w = rooms['stone_path']

rooms['valley'].to_s = rooms['old_trail']

rooms['dense_forest'].to_n = rooms['old_trail']

rooms['cave'].to_e = rooms['old_trail']
# Turn out the lights.
rooms['cave'].light = False

rooms['river_bank'].to_n = rooms['choppy_waters']
rooms['river_bank'].to_s = rooms['narrow_trail']
rooms['river_bank'].to_e = rooms['small_pond']
rooms['river_bank'].to_w = rooms['rapid_river']

rooms['small_pond'].to_w = rooms['river_bank']
rooms['small_pond'].to_e = rooms['steel_bridge']

rooms['rapid_river'].to_e = rooms['river_bank']

rooms['puppy_dog'].to_s = rooms['steel_bridge']
rooms['steel_bridge'].to_n = rooms['puppy_dog']

# light sources flashlight
flashlight = Item('flashlight',
                  'Useful to light your way in the dark.',
                  weight=5)
flashlight.is_light = True
rooms['empty_highway'].items_[flashlight.name] = flashlight

# Hide an item in a box in the dark in a cave.
# Make a Container.
square_lock = Container('square_lock',
                           'A sturdy, locked box. It is square',
                           weight=50)


sling_shot = SlingShot('sling_shot',
                       'A rock is propelled forward.',
                       weight=5)

# Do the same with a red box.
round_lock = Container('round_lock',
                         'A round chest is locked.',
                         weight=50)
round_key = Item('round_key',
               'A round key must open something',
               weight=1)

# connects lock and key
round_lock.key = round_key
treats = Item('treats',
                  'If you find the puppy you can give them to him',
                  weight=2)
round_lock.items_[treats.name] = treats

# location lock and key.
rooms['road_block'].items_[round_key.name] = round_key
rooms['rapid_river'].items_[round_lock.name] = round_lock


# Put the item in the box.
square_lock.items_[sling_shot.name] = sling_shot

# Locks vox
square_lock.locked = True

# Be sure to make a key.
square_key = Item('square_key',
                 'A square key must open something.',
                 weight=1)

# connects lock and keys
square_lock.key = square_key

# location lock and key.
rooms['cave'].items_[square_lock.name] = square_lock
rooms['dense_forest'].items_[square_key.name] = square_key


# Make rocks and berries.
rocks = Rocks('rocks',
                  'Small round stones',
                  weight=2)
rooms['valley'].items_[rocks.name] = rocks

huckleberries = Berries('huckleberries',
                 'Huckleberries are sweet and yummy')
rooms['old_trail'].items_[huckleberries.name] = huckleberries

blue_berries = Berries('blue_berries',
                 'Blue berries sweet and savory')

rooms['suspension_bridge'].items_[blue_berries.name] = blue_berries

black_berries = Berries('black_berries',
                 'Black berries tart and sour')

rooms['rapid_river'].items_[black_berries.name] = black_berries
