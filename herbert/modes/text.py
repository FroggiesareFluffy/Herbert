import os
import sys
import time
from xml.etree import ElementTree


def main():
    story = ElementTree.parse(os.path.join('..', 'data', 'script.xml'))
    show_start_screen(story)
    raw_input("Press enter to begin. ")
    show_background_story(story)
    raw_input("Press enter to play. ")
    play_game(story)


def show_start_screen(story):
    print story.find('start-screen').text


def show_background_story(story):
    import time
    background_story = story.find('intro')
    for line in background_story:
        print line
        time.sleep(0.5)


def play_game(story):
    for element in story.getroot():
        if element.tag == "scene" and element.get("first") == "1":
            next_scene = run_scene(element)
            break
    while next_scene:
        for element in story.getroot():
            if element.tag == "scene" and element.get("name") == next_scene:
                next_scene = run_scene(element)
                break


def run_scene(scene):
    for element in scene:
        if element.tag == "line":
            print element.text
        elif element.tag == "wait":
            time.sleep(2)
        elif element.tag == "choice":
            do = None
            while not do:
                do = run_choice(element)
            if do.startswith("SCENE: "):
                print do[7:]
                return do[7:]
        elif element.tag == "goto":
            return element.get("scene")
    return None


def run_choice(choice):
    print "What do you do:"
    number = 0
    for option in choice:
        if option.tag == "option":
            print chr(number+97)+") "+option.get("text")
            number += 1
    decision = raw_input()
    if len(decision) == 1:
        number = ord(decision)-97
        for option in choice:
            if option.tag == "option":
                if number == 0:
                    return run_option(option)
                number -= 1
    return None


def run_option(option):
    for element in option:
        if element.tag == "line":
            print element.text
        elif element.tag == "wait":
            time.sleep(2)
        elif element.tag == "continue":
            return "continue"
        elif element.tag == "goto":
            return "SCENE: "+element.get("scene")
    return False


if sys.version_info.major == 3:
    raw_input = input