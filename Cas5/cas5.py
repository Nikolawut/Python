# class Post:
#     def __init__(self,title,id,description="Default Description",author="Admin"):
#         self.author  = author 
#         self.__id = id
#         self.title = title
#         self.description = description
# post_a = Post("hello","None")
# print(isinstance(post_a, Post))

# class Circle:
#     pi = 3.14
#     def __init__(self, radius = 1):
#         self.radius = radius
#     def area(self):
#         return(self.radius**2)+ Circle.pi
#     def set_radius(self, new_radius):
#         self.__radius = new_radius
#     def get_radius(self):
#         return self.__radius
# c = Circle(10)
# print(c.area())

# class User:
#     def __init__(self):
#         print("User init")
#     def who(self):
#         print("hello")

# class Pavougaonik:
#     def __init__(self,len, w):
#         self.len = len
#         self.w = w
#     def area(self):
#         return self.len * self.w
#     def perimeter(self):
#         return 2*self.len + 2*self.w
# class Square(Pavougaonik):
#     def __init__(self, len):
#         super().__init__(len, len)

# class Book:
#     def __init__(self,title,author, pages):
#         self.title = title
#         self.author = pages
#         self.pages = pages
#     def __str__(self):
#         return f"Naslov {self.title}, Autor {self.author}, Stranice {self.pages}"
        
#     def __len__(self):
#         return self.pages
    
#     def __del__(self):
#         print("Obrisan objekat")

#     def __gt__(self, book2):
#         return self.pages > book2.pages
        
# book1 = Book("Uvod u veb programiranje","Marko markovic", 260)
# book2 = Book("Dizajn", "Miki", 201) 

# lista_knjiga = []
# lista_knjiga.append(book1)
# lista_knjiga.append(book2)
# for knjiga in lista_knjiga:
#     print(knjiga)
# print(book1 > book2)

# print(len(book1))
f = open("Domaci zadaci/Domaci2/Domaci2.txt")
print(f.read())
f.seek(0)
print(f.read())
f.close()
with open("Domaci zadaci/Domaci2/Domaci2.txt") as f:
    c = f.read()
    d = c.split("\n")
    print(d)
    max_kvadrat = 0
    povrsina = 0
    for i in d:
        (a,b) = i.split(",")
        if int(a) == int(b):
            povrsina = int(a) * int(b)
        if povrsina > max_kvadrat:
            max_kvadrat = povrsina
    print(max_kvadrat)