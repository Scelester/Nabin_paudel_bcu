#-------------------------------------------------------------------------#
#   scripted on Jun 2, 2022                                               |
#   by, Nabin Paudel                                                     |
#-------------------------------------------------------------------------#

def cal_distance(p1, p2):
    """find distance between two points or coordinate"""
    x1, y1 = p1
    x2, y2 = p2

    pre_Dist = (x2 - x1)**2 + (y2-y1)**2

    distance = pre_Dist ** 0.5

    return distance


def find_direction(p1, p2):
    """find direction of p2 with respect to p1"""
    x1, y1 = p1
    x2, y2 = p2

    dir = ""

    if y2 > y1:
        dir += "Top "
    elif y2 < y1:
        dir += "Bottom "

    if x2 > x1:
        dir += "Right "
    elif x2 < x1:
        dir += "Left "

    return dir


def main():
    print("------- Robot Program-----------")

    # count to track steps for user data
    count = 0

    # list to store all distance returned by cal_distance function
    distance_list = []

    # list to store all directions returned by find_direction
    direction_list = []

    # list to store all coordinate as tupel given by user, (0,0) being inital coordinate
    coordinate_tupel_list = [(0, 0)]

    while True:
        count += 1

        inp_x = float(input(f"\nInput x{count} coordinate:"))
        inp_y = float(input(f"\nInput y{count} coordinate:"))

        # stop code if both the given cordinate is 999
        if inp_x == 999 and inp_y == 999:
            break
        else:
            # get the last coordinate from tupel list
            prev_coordinate = coordinate_tupel_list.pop()

            # storing the returned-value(distance) from cal_distance function.
            found_dis = cal_distance(prev_coordinate, (inp_x, inp_y))

            # storing the retuned-value(direction) from find_direction.
            found_dir = find_direction(prev_coordinate, (inp_x, inp_y))

            # appending the new user given coordinate in the following list.
            coordinate_tupel_list.append((inp_x, inp_y))

            # appending the calculated distance in the following list.
            distance_list.append(found_dis)

            # appending the retuned direction in the following list.
            direction_list.append(found_dir)

    print("-"*10)

    # displaying the distances one by one as steps.
    for n in range(len(distance_list)):
        step_distance = "{:.2f}".format(distance_list[n])
        print(f"Step {n+1}: {step_distance} units.")

    print("-"*10)

    # variable to store the total distance.
    tots = 0

    # calculating total distance.
    for n in distance_list:
        tots += n

    tots = "{:.2f}".format(tots)

    print(f"Total distance travelled by the robot: {tots}")

    print("-"*10)
    print("-Direction-")

    # displaying the directions one by one as steps.
    for n in range(len(direction_list)):
        print(f"Step {n}: {direction_list[n]}")


if __name__ == "__main__":
    main()
