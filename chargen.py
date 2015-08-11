# import
import generate
# init
print "RPGStuck Character Helper."
print "Run \"help\" for a list of commands."

genRunning = True
while genRunning:
    command = raw_input("> ")
    command = command.lower()
    if command == "help":
        print "Available Commands are:"
        print "generate"
        print "view"
        print "exit"
    elif command == "generate":
        print "Initializing Character Generator..."
        generate.main()
    elif command == "view":
        print "Sorry! \"view\" isn't ready yet."
    elif command == "exit":
        genRunning = False
    else:
        print command + " is an invalid command. Type \"help\" for help."

print "Thank you for using the RPGStuck Character Helper."
