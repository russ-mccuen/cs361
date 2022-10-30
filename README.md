# cs361

# Communication Contract
This microservice provides a random dad joke when the user requests a dad joke.

## Instructions on how to REQUEST data:
* Have a dad-joke.txt file in your program that writes the keyword "dad" when the user requests a dad joke
* All you have to do is request the joke. Jokes will be kept on my end and a joke will be picked at random

EXAMPLE CODE:

while True:
        choice = input("Enter 1 for a dad joke, 2 to quit: ")

        if choice =='1':
            file = open('dad-joke.txt', 'w')
            file.write('dad')
            file.close()
            
## Instructions on how to RECEIVE data:
* Read the same file, dad-joke.txt
* The microservice will overwrite "dad" with the dad joke, so all that will be in the file is the joke
* The code below is an example of how you could receive and print the joke and is not meant to represent the final code in your project

EXAMPLE CODE:

        file = open('dad-joke.txt', 'r')
        line = file.readline()
        print(line, '\n')
        file.close()
        
## UML Sequence Diagram:

![image](https://user-images.githubusercontent.com/24654928/198897060-1708682e-2f6a-4d91-bc9a-3e004e528ed0.png)
