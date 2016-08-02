from turtle import *
import Tkinter


setup(400,627,0,0)
bgpic("350px-Argentina.gif") 



penup() 

goto(-23,-34.5) #rio negro
dot(10, "blue")
pendown()
speed(1)


pencolor("lightblue")
pensize(3)
print("Lista de ciudades"
          " 1- Buenos Aires \n 2- San S. de Jujuy \n 3-Salta \n 4- S.M. de Tucuman\n"
          " 5- Sgo. del Estero \n 6- Formosa \n 7-Resistencia \n 8- Santa Fe\n"
          " 9- Corrientes \n 10- Posadas \n 11- Parana \n 12- Cordoba \n 13- La Rioja \n"
          " 14- San Juan \n 15- San Luis \n 16- Catamarca \n 17- Mendoza \n 18- Santa Rosa \n"
          " 19- Neuquen \n 20- Viedma \n 21- Rawson \n 22- Rio Gallegos \n 23- Ushuaia ")
puntos.append([36,69.5],[-56,239.5],[-57.1,228.5],[-54,194.5],[-44,180.5],[50,206.5],[34,189.5],[9,118.5],[42,187.5],[85,184.5],[14,115.5],[-40,123.5])
puntos.append([-77,150.5],[-101,118.5],[-68,88.5],[-64,171.5],[-103,96.5],[-39,35.5],[-91,-4.5],[-23,-34.5],[-50,-71.5],[-86,-210.5],[-70,-258.5])


goto(85,184.5) #misiones
dot(10, "blue")
goto(50,206.5) #formosa
dot(10, "blue")
goto(-56,239.5) #jujuy
dot(10, "blue")
goto(-57.1,228.5) #salta
dot(10, "blue")
goto(-54,194.5) #tucuman
dot(10, "blue")
goto(36,69.5) #baires
dot(10, "blue")
goto(34,189.5)   #chaco
dot(10, "blue")
goto(42,187.5) #corrientes
dot(10, "blue")
goto(14,115.5) #entre rios
dot(10, "blue")
goto(9,118.5) #santa fe
dot(10, "blue")
goto(-40,123.5) #cordoba
dot(10, "blue")
goto(-64,171.5) #caramarca
dot(10, "blue")
goto(-77,150.5) #la rioja
dot(10, "blue")
goto(-101,118.5) #san juan
dot(10, "blue")
goto(-103,96.5) #mendoza
dot(10, "blue")
goto(-44,180.5) #sgo estero
dot(10, "blue")
goto(-39,35.5) #la pampa
dot(10, "blue")
goto(-91,-4.5) #neuquen
dot(10, "blue")
goto(-68,88.5) #san luis
dot(10, "blue")
goto(-50,-71.5) #chubut
dot(10, "blue")
goto(-86,-210.5) #santa cruz
dot(10, "blue")
goto(-70,-258.5) #tiera del fuego
dot(10, "blue")
done()


