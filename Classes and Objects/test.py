class Cookie:
#class attributes
    def __init__(self, color, shape='star'):
        self.color = color
        self.shape = shape

#class methods
    def __del__(self):
        print("A cookie has been eaten")

cookie1 = Cookie("blue") 
print(cookie1.color)
print(cookie1.shape)
cookie2 = Cookie("red", "circle")
print(cookie2.color)
print(cookie2.shape)
del cookie1