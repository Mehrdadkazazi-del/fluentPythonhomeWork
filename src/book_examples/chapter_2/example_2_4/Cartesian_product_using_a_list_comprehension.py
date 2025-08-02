colors = ['red', 'green', 'blue', 'yellow']
sizes = ['small', 'medium', 'large']

t_shirts = [(color, size) for color in colors for size in sizes]

print(t_shirts)

for color in colors:
    for size in sizes:
        obj =  (color, size)
        print(obj)

t_shirts = [(color, size) for color in colors for size in sizes]
print(t_shirts)
