import zmq
import random

context = zmq.Context()


def random_word():
    word_list = []
    with open('gen_z_slang_words.txt', "r", encoding="utf-8-sig") as file:
        for line in file:
            word_list.append(line.strip('\n'))
    word = random.choice(word_list)
    return word

rand_word = random_word()

#Socket to talk to server
#print("Connecting to server…")
print("\nDisclosure: Your information is private and will not be recorded")
print("(If the generator is not working you can also go to https://dadjokegenerator.com/)\n")
print("Your Random Dad Joke is:")
#print(dad_joke)
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

from dadjokes import Dadjoke
dadjoke = Dadjoke()
print(dadjoke.joke)

socket.send_string(rand_word)

# Get the reply.
message = socket.recv()







