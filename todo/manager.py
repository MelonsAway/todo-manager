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
        target.write(f"\n{line1}")
        target.close()
