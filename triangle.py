def third_ang_of_triangle(first_ang=0, sec_angle=0):
    sum = first_ang + sec_angle

    if sum > 180:
        return 'Error, open triangle'
    elif first_ang<0 or sec_angle<0:
        return 'Error, angles negative'
    else:
        return str(180 - sum)

if __name__=='__main__':
    first_ang=float(input('Enter first angle: '))
    sec_ang=float(input('Second angle'))
    print(f'Third angle: {third_ang_of_triangle(first_ang,sec_ang)}')
