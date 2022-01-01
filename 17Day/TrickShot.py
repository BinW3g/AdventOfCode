area_x = [248, 285]
area_y = [-85, -56]
# example values
# area_x = [20, 30]
# area_y = [-10, -5]


def calc_max_height():
    max_y = 0
    max_y_vel = 0
    start_velocity = 0
    no_hit = 0
    max_no_hits = 1000
    while no_hit < max_no_hits:
        velocity = start_velocity
        y = 0
        current_max_y = 0
        while not y < area_y[1]:
            velocity += -1
            y += velocity
            if velocity == 0:
                current_max_y = y
        if y < area_y[0]:
            no_hit += 1
        elif current_max_y > max_y:
            max_y = current_max_y
            max_y_vel = start_velocity-1
        start_velocity += 1
    return max_y, max_y_vel


def calc_smallest_x():
    x = 0
    velocity = 0
    while not area_x[0] < x < area_x[1]:
        velocity += 1
        x += velocity
    return velocity


def see_if_hits(x_velocity, y_velocity):
    x = 0
    y = 0
    while (x+x_velocity) <= area_x[1] and (y+y_velocity) >= area_y[0]:
        x += x_velocity
        y += y_velocity
        if x_velocity != 0:
            x_velocity -= 1
        y_velocity -= 1
    return area_x[0] <= x <= area_x[1] and area_y[1] >= y >= area_y[0]


def count_possible_values(max_y):
    smallest_x = calc_smallest_x()
    y_vel = area_y[0]
    hits = 0
    while y_vel <= max_y:
        x_vel = smallest_x
        while x_vel <= area_x[1]:
            if see_if_hits(x_vel, y_vel):
                hits += 1
                print(str(x_vel) + ";" + str(y_vel))
            x_vel += 1
        y_vel += 1
    return hits


m_y = calc_max_height()
print(see_if_hits(11, -1))
print(m_y[0])
print(count_possible_values(m_y[1]))
