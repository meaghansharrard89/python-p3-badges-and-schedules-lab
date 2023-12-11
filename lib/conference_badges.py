def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]


def assign_rooms(names):
    room_assignments = []
    for index, item in enumerate(names):
        room_number = index + 1
        room_assignments.append(
            f"Hello, {item}! You'll be assigned to room {room_number}!"
        )
    return room_assignments


def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for name in badges:
        print(name)

    for name in rooms:
        print(name)
