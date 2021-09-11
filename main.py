#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"


world = {
  "uuid": "6B8FA446-2847-42CF-9CB0-A2C149533127",
  "name": "Project1Story",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631396746098,
  "passages": [
    {
      "name": "Storm",
      "tags": "",
      "id": "1",
      "text": "You awaken to a dark and dreary night, a storm rages overhead sending blankets of rain to the dirt below. The storm thrashes the trees and tosses everything in its path...\nYou notice a damp cave dead ahead, that could serve as protection against this violent storm.\n\n[[CAVE->Cave Entrance]]",
      "links": [
        {
          "linkText": "CAVE",
          "passageName": "Cave Entrance",
          "original": "[[CAVE->Cave Entrance]]"
        }
      ],
      "hooks": [],
      "cleanText": "You awaken to a dark and dreary night, a storm rages overhead sending blankets of rain to the dirt below. The storm thrashes the trees and tosses everything in its path...\nYou notice a damp cave dead ahead, that could serve as protection against this violent storm."
    },
    {
      "name": "Cave Entrance",
      "tags": "",
      "id": "2",
      "text": "The cave covers your head from the oncoming rain. Although the drops of condensation fall from overhead the cave is rather comfy...\nNow that your eyes have adjusted you notice the cave descends deeper, an old man also appears to be resting on the cave wall.\n\n[[TALK->Old Man]]\n[[DEEPER->Chamber1]]\n[[EXIT->Ending1]]",
      "links": [
        {
          "linkText": "TALK",
          "passageName": "Old Man",
          "original": "[[TALK->Old Man]]"
        },
        {
          "linkText": "DEEPER",
          "passageName": "Chamber1",
          "original": "[[DEEPER->Chamber1]]"
        },
        {
          "linkText": "EXIT",
          "passageName": "Ending1",
          "original": "[[EXIT->Ending1]]"
        }
      ],
      "hooks": [],
      "cleanText": "The cave covers your head from the oncoming rain. Although the drops of condensation fall from overhead the cave is rather comfy...\nNow that your eyes have adjusted you notice the cave descends deeper, an old man also appears to be resting on the cave wall."
    },
    {
      "name": "Old Man",
      "tags": "",
      "id": "3",
      "score":10,
      "text": "You approach the old man, his old sunken eyes display a deep sorrow. His voice rings off the cave walls. \"Listen close young one.. You would be better off dying in the storm than being in this cave. It is a harrowing journey, one you're better off not making.\"\n\n[[BENICE->Good Response]]\n[[BEMEAN->Bad Response]]",
      "links": [
        {
          "linkText": "BENICE",
          "passageName": "Good Response",
          "original": "[[BENICE->Good Response]]"
        },
        {
          "linkText": "BEMEAN",
          "passageName": "Bad Response",
          "original": "[[BEMEAN->Bad Response]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the old man, his old sunken eyes display a deep sorrow. His voice rings off the cave walls. \"Listen close young one.. You would be better off dying in the storm than being in this cave. It is a harrowing journey, one you're better off not making.\""
    },
    {
      "name": "Chamber1",
      "tags": "",
      "id": "4",
      "score":4,
      "text": "As you descend deeper the darkness closes in around you. The walls of the cave just barely being visible. A low ominious whistle squeaks from further down. As you press forward you come to a fork in the cave. The whistle appears to be coming from the right, perhaps you should avoid it...\n\n[[LEFT->Left Path]]\n[[RIGHT->Right Path]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Left Path",
          "original": "[[LEFT->Left Path]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Right Path",
          "original": "[[RIGHT->Right Path]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you descend deeper the darkness closes in around you. The walls of the cave just barely being visible. A low ominious whistle squeaks from further down. As you press forward you come to a fork in the cave. The whistle appears to be coming from the right, perhaps you should avoid it..."
    },
    {
      "name": "Bad Response",
      "tags": "",
      "id": "5",
      "score":-20,
      "text": "The shadows on the old man's face distort, his brow furrows and he says \"The warning I gave was true and clear, you should leave the cave and die. It would be preferable than what waits below.\" The old man slumps back down and turns his head away from you. It's clear this conversation is over.\n\n[[LEAVE->Cave Entrance]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "Cave Entrance",
          "original": "[[LEAVE->Cave Entrance]]"
        }
      ],
      "hooks": [],
      "cleanText": "The shadows on the old man's face distort, his brow furrows and he says \"The warning I gave was true and clear, you should leave the cave and die. It would be preferable than what waits below.\" The old man slumps back down and turns his head away from you. It's clear this conversation is over."
    },
    {
      "name": "Good Response",
      "tags": "",
      "id": "6",
      "score":20,
      "text": "The old man's hand wavers. \"You would do well to leave..\" After barely getting his sentence out he slumps back down into the rocks.\n\n[[LEAVE->Cave Entrance]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "Cave Entrance",
          "original": "[[LEAVE->Cave Entrance]]"
        }
      ],
      "hooks": [],
      "cleanText": "The old man's hand wavers. \"You would do well to leave..\" After barely getting his sentence out he slumps back down into the rocks."
    },
    {
      "name": "Left Path",
      "tags": "",
      "id": "7",
      "score":5,
      "text": "Proceeding forward the whistling becomes more distant. Whatever its from its becoming more distant. As you walk deeper and deeper you discover a bright light. Perhaps the storm has ended and you're being greeted by the bright sun. \n\n[[LIGHT->Loop]]",
      "links": [
        {
          "linkText": "LIGHT",
          "passageName": "Loop",
          "original": "[[LIGHT->Loop]]"
        }
      ],
      "hooks": [],
      "cleanText": "Proceeding forward the whistling becomes more distant. Whatever its from its becoming more distant. As you walk deeper and deeper you discover a bright light. Perhaps the storm has ended and you're being greeted by the bright sun."
    },
    {
      "name": "Right Path",
      "tags": "",
      "id": "8",
      "score":15,
      "text": "The whistling grows louder, piercing your ears. The roof of the cave seems to get damper and damper. The drops of water are more frequent. It appears that you're approaching the storm? Somehow you've ended up at the entrance of the cave... The old man gestures for you to sit next to him. As you do he seems to give up the last of his life. Leaving you alone...\n\n\nThe storm is rather terrible tonight...\nSuddenly a young man walks into the entrance of the cave. Sitting up to speak with him you tell him \"You would be better off dying in the storm than being in this cave.\"\n\n''THE END''\n\n[[RESTART->Storm]]",
      "links": [
        {
          "linkText": "RESTART",
          "passageName": "Storm",
          "original": "[[RESTART->Storm]]"
        }
      ],
      "hooks": [],
      "cleanText": "The whistling grows louder, piercing your ears. The roof of the cave seems to get damper and damper. The drops of water are more frequent. It appears that you're approaching the storm? Somehow you've ended up at the entrance of the cave... The old man gestures for you to sit next to him. As you do he seems to give up the last of his life. Leaving you alone...\n\n\nThe storm is rather terrible tonight...\nSuddenly a young man walks into the entrance of the cave. Sitting up to speak with him you tell him \"You would be better off dying in the storm than being in this cave.\"\n\n''THE END''"
    },
    {
      "name": "Loop",
      "tags": "",
      "id": "9",
      "score":10,
      "text": "Walking into the light you end up at a fairly well lit cave entrance, the storm still crashes overhead, but at at least you're sheltered. You notice the cave descends deeper, an old man also appears to be resting on the cave wall.\n\n[[TALK->Old Man2]]\n[[DESCEND->Chamber1]]\n[[LEAVECAVE->Ending1]]",
      "links": [
        {
          "linkText": "TALK",
          "passageName": "Old Man2",
          "original": "[[TALK->Old Man2]]"
        },
        {
          "linkText": "DESCEND",
          "passageName": "Chamber1",
          "original": "[[DESCEND->Chamber1]]"
        },
        {
          "linkText": "LEAVECAVE",
          "passageName": "Ending1",
          "original": "[[LEAVECAVE->Ending1]]"
        }
      ],
      "hooks": [],
      "cleanText": "Walking into the light you end up at a fairly well lit cave entrance, the storm still crashes overhead, but at at least you're sheltered. You notice the cave descends deeper, an old man also appears to be resting on the cave wall."
    },
    {
      "name": "Old Man2",
      "tags": "",
      "id": "10",
      "score":5,
      "text": "You approach the old man, his old sunken eyes display a deep sorrow. His voice rings off the cave walls. \"You should have listened, now you're already apart of the system here. I shall pray for your journey, in hopes one day you don't return here.\"\n\n[[BEMEAN->Bad Response]]",
      "links": [
        {
          "linkText": "BEMEAN",
          "passageName": "Bad Response",
          "original": "[[BEMEAN->Bad Response]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the old man, his old sunken eyes display a deep sorrow. His voice rings off the cave walls. \"You should have listened, now you're already apart of the system here. I shall pray for your journey, in hopes one day you don't return here.\""
    },
    {
      "name": "Ending1",
      "tags": "",
      "id": "11",
      "text": "The rain overhead has worsened, it seems the storm won't let up soon. A sudden flash topples a tree, sending it crashing upon you. Stuck under the tree, all you can do is wait...\n\n''THE END''\n\n[[RESTART->Storm]]",
      "links": [
        {
          "linkText": "RESTART",
          "passageName": "Storm",
          "original": "[[RESTART->Storm]]"
        }
      ],
      "hooks": [],
      "cleanText": "The rain overhead has worsened, it seems the storm won't let up soon. A sudden flash topples a tree, sending it crashing upon you. Stuck under the tree, all you can do is wait...\n\n''THE END''"
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	print("You are at the " + current_location["name"])
	print(current_location["cleanText"])
	print(moves, score)

def get_input():
	response = input("where would you like to go?")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	for link in current_location["links"]:
		if link["linkText"] == response:
			return link["passageName"]
	print("I didn't understand that. Please try again.")
	return location_label
 

# ----------------------------------------------------------------

location_label = "Storm"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	render(current_location, score, moves)
	response = get_input()
score = score + current_location["score"]
print("Moves: {}, Score: {}".format[moves,score])


print("Thanks for playing!")