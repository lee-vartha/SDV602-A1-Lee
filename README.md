# SDV602-A1-Lee
# SDV602-A1-Lee
Haunted house is a text=based adventure game where players go around a haunted house till they find the monster.
This is the link to the language comparison video: https://livenmitac-my.sharepoint.com/:v:/g/personal/lee-vartha_live_nmit_ac_nz/ERgnLQNDA4lBoePEY9hpKC0BFOGBowWQvUsKJ3GB0o2eSQ
prerequesites:
- python 3.x
- venv

installation:
- clone the repo
- setup the virtual environment (python -m venv venv)
- install required packages (pip install -r requirements.txt)
- make sure the directory is in 'modules' (cd modules)
- Run this using 'python main.py'

folders:
1. images: provides all images for the game
2. modules: provides all the files

A DISCLAIMER IS THAT THE IMAGES ARE NOT MINE - THEY ARE SOURCED AS **AI GENERATED IMAGES** THROUGH A WEBSITE : https://deepai.org/machine-learning-model/text2img
I ACKNOWLEDGE THIS - I ALSO MADE A TXT FILE WITHIN THE 'IMAGES' FOLDER


file structure:
1. main.py: the main entry point of the game - has rooms, directions etc.
2. inventory.py: manages the inventory
3. status.py: tracks the players status
4. monster_fight.py: has logic for fighting monsters
5. requirements.txt: lists the required python packages




cheat sheet:

1. directions: forward, left, right, behind
2. to fight: fight
3. to go inside the house: yes/no

theres the following rooms:
- house
- foyer
- dining room
- kitchen
- hallway
- library
- bathroom
- bedroom

kitchen has a 'teaspoon' (weapon) -- enter through dining room (left door in foyer)
library has the monster -- enter through right door in foyer
hallway has 'lint' (weapon) -- enter by saying 'forward' in foyer
bedroom has 'pillow' (weapon) -- enter through hallway (left door in hallway)

the library is the first door on the right when you enter the haunted house - must have supplies or you will be defeated



