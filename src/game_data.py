
rooms = {
    'Foyer': {
        'description': 'You are in the foyer. There is a door to the north.',
        'north': 'Library',
        'south': 'Dining Room',
        'items': ['key']
    },
    'Library': {
        'description': 'You are in the library. There is a door to the south.',
        'south': 'Foyer',
        'items': ['book']
    },
    'Dining Room': {
        'description': 'You are in the dining room. There is a door to the north.',
        'north': 'Foyer',
        'items': ['food']
    },
    'Kitchen': {
        'description': 'You are in the kitchen. There is a door to the east.',
        'east': 'Dining Room',
        'items': ['knife']
    }
}

initial_game_state = {
    'current_room': 'Foyer',
    'inventory': set(),
    'health': 100,
    'monster': False
}

""" Monster would be in one room"""

if __name__ == "__main__":
    test_game_state = initial_game_state.copy()
    print(test_game_state)
    print(rooms)
