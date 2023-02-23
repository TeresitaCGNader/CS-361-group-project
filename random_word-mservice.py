import random
import zmq
import time 

def generate_random_slang():
    #Gen Z Slang Generator 
    word_list = []
    with open("gen_z_slang_words.txt","r") as file:
        for line in file:
            word_list.append(line)
    random_word = random.choice(word_list)
    return str(random_word)



context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

rand_word = generate_random_slang()



while True:

    message = socket.recv()
    print(message)
    socket.send_string(rand_word)






