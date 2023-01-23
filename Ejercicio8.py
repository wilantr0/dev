pointer = [0, 0]
coords_x = [0]
coords_y = [0]

stop = int(input('How many stops do you want to do? \n'))

for i in range(stop):
    coord_x, coord_y = input('').split(' ')
    coords_x.append(int(coord_x))
    coords_y.append(int(coord_y))



for i in range(stop):
    while True:
        if coords_x[i] == coords_x[i-1] and coords_y[i] == coords_y[i-1]:
            continue
        elif coords_x[i] > coords_x[i-1] and coords_x[i] != 0:
            x= coords_x[i]-coords_x[i-1]
            print(f'Walk {x} steps East')
            continue
        elif coords_x[i] < coords_x[i-1] and coords_x[i] != 0:
            x= coords_x[i]-coords_x[i-1]+(coords_x[i-1]*2)
            print(f'Walk {x} steps West')
            continue
        elif coords_y[i] > coords_y[i-1] and coords_y[i] != 0:
            y= coords_y[i]-coords_y[i-1]
            print(f'Walk {y} steps North')
            continue
        elif coords_y[i] < coords_y[i-1] and coords_y[i] != 0:
            x= coords_y[i]-coords_y[i-1]+(coords_y[i-1]*2)
            print(f'Walk {y} steps South')
            print
            continue
        else:

            print(f'Walk {coords_x[i+1]} steps West')
            continue
