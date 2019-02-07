class Manager(object):
    def __init__(self):
#    filename = "testing.txt"
        pass
    def show():
        txt = open("testing.txt")
#        print(f"Here's your file {txt}:")
        print(txt.read())
        txt.close()
    def add():
        target = open("testing.txt", 'a')
        line1 = input()
        target.write(f"{inputdate}\n")
        if Item.done == True:
            target.write("it's done")
        else:
            target.write("it's not done")
        target.write(f"\n{line1}")
        target.close()
    def complete():
        Item.done = True
