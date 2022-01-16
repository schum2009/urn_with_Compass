def direction(facing: str, turn: int):
    side_world = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    try:
        if turn > 1080 or turn < -1080:
            raise ValueError
        return side_world[(side_world.index(facing) + turn // 45) % 8]
    except ValueError:
        print("Turn must be between 1080 and -1080 degrees")


print(direction("E", -90))
