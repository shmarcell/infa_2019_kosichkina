# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):


    line = line.lower()
    line_parsed = line.split()
    star.type = line_parsed[0]
    star.R = int(line_parsed[1])
    star.color = line_parsed[2]
    star.m = float(line_parsed[3])
    star.x = float(line_parsed[4])
    star.y = float(line_parsed[5])
    star.Vx = float(line_parsed[6])
    star.Vy = float(line_parsed[7])
    return

def parse_planet_parameters(line, planet):

    line = line.lower()
    line_parsed = line.split()
    planet.type = line_parsed[0]
    planet.R = int(line_parsed[1])
    planet.color = line_parsed[2]
    planet.m = float(line_parsed[3])
    planet.x = float(line_parsed[4])
    planet.y = float(line_parsed[5])
    planet.Vx = float(line_parsed[6])
    planet.Vy = float(line_parsed[7])
    return


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """

    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            Fout = open(output_filename, "w")
            if obj.type= "star":
                temp= "Star"
            else obj.type= "planet"
                temp= "Planet"

            Fout.write(temp+str(R)+str(color)+str(m)+str(x)+str(y)+str(Vx)+str(Vy))
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME: should store real values

Fout.close()

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")