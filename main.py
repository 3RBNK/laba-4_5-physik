from math import cos, radians
from matplotlib import pyplot as plt


def print_float_array(a: list):
    for elem in a:
        print(f"{elem:.3f}", end=" ")
    print()


def print_int_array(a: list):
    for elem in a:
        print(elem, end=" ")
    print()


def main():
    amper_value = [0.0, 0.8, 1.8, 3.1, 4.3, 6.1, 8.2, 10.3, 11.1, 12.2]

    cos_value = []
    angle_value = []

    for angle in range(90, -2, -10):
        angle_value.append(angle)
        cos_value.append(cos(radians(angle)))

    square_cos_value = [value ** 2 for value in cos_value]


    print("amper: ")
    print_float_array(amper_value)
    print()

    print("angle: ")
    print_float_array(angle_value)
    print()

    print("cos a:")
    print_float_array(cos_value)
    print()

    print("cos^2 a:")
    print_float_array(square_cos_value)
    print()

    # оси координат
    plt.axhline(0, color="black", linestyle="--")
    plt.axvline(0, color="black", linestyle="--")

    # подписи осей
    plt.xlabel("Cos^2 alpha (безразмерная величина)")
    plt.ylabel("I сила тока (в микро амперах)")

    # значения
    plt.plot(square_cos_value, amper_value, color="red")
    plt.scatter(square_cos_value, amper_value, color="red")

    plt.show()


main()
