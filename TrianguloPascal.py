dimension=int(input("ingresa el numero de dimensiones: "))
triangulo = []
def pascal(n):
    row = [1]
    k = [0]
    for x in range(max(n, 0)):
        triangulo.append(row)
        row = [l + r for l, r in zip(row + k, k + row)]
    return n >= 1
def print_pascals_triangle(triangle):
    largest_element = triangle[-1][len(triangle[-1]) // 2]
    element_width = len(str(largest_element))
    def format_row(row):
        return ' '.join([str(element).center(element_width) for element in row])
    triangle_width = len(format_row(triangle[-1]))
    for row in triangle:
        print(format_row(row).center(triangle_width))
pascal(dimension)
print_pascals_triangle(triangulo)