import threading  # Parallel processing module


class Messenger(threading.Thread):
    def run(self):  # Calls run() whenever we create a thread
        # Underline convention when I want to loop with range but dont want to use the incremented numbers
        for _ in range(10):
            print(threading.currentThread().getName())


messenger_sender = Messenger(name='Send out messages')
messenger_receiver = Messenger(name='Receives messages')

messenger_sender.start()  # Looks for the function run and runs it, loops 10 times
messenger_receiver.start()  # Looks for the function run and runs it, loops 10 times

# With threads both run at the same time in parallel
