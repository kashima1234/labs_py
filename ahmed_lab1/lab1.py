# Кашима Aхмед, иу7и-13б
# Лабораторная работа №1

import math
# Ввод исходных данных
edge_length = float(input("Enter the length cube edge :\n"))
if edge_length < 0:
    print("Hello world! ")
    exit(-1)
# Вывод результата
surface = 6 * edge_length * edge_length  # плошадь поверхности
volume = math.pow(surface, 3) / math.pow(edge_length, 3)  # объём
space_diagonal = edge_length * math.sqrt(3)  # космическая диагональ куба
face_diagonal = edge_length * math.sqrt(2)  # гранная диагональ куба
radius_of_circumscribed_sphere = math.sqrt(3) / 2 * edge_length  # радиус описанной сферы
radius_of_inscribed_sphere = edge_length / 2  # радиус вписанной сферы

print("edge length {:.4f}" .format(edge_length))
print("surface {:.4f}". format(surface))
print("volume {:.4f}" .format(volume))
print("space diagonal {:.4f}".format(space_diagonal))
print("face diagonal {:.4f}".format(face_diagonal))
print("radius of circumscribed sphere {:.4f}". format(radius_of_circumscribed_sphere))
print("radius of inscribed sphere {:.4f}" .format(radius_of_inscribed_sphere))