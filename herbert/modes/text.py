import os


def main():
    show_start_screen()
    raw_input("Press enter to begin. ")
    show_background_story()
    raw_input("Press enter to play. ")
    play_game()


def show_start_screen():
    with open(os.path.join("..", "data", "text_welcome.txt")) as welcome:
        print welcome.read()


def show_background_story():
    with open(os.path.join("..", "data", "intro.txt")) as background_story:
        import time
        for line in background_story:
            print line
            time.sleep(0.5)


def play_game():
    print "You wake up in a cold, metal cage. Around you, you can see a small tree with bananas growing on it."

