# Named Parameters
# helpful when we have many parameters and want to
# send arguments in any order


def total_marks(physics, maths, science, english, hindi):
    print(f"Your marks in physics = {physics}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in science = {science}")
    print(f"Your marks in english (english)")
    print(f"Your marks in hindi = {hindi}")
    total = physics + maths + science + english + hindi
    print(f"Your total marks = {total}")


# deafualt ordered parameters are to be declared first
total_marks(56, 98, hindi=85, english=23, science=98)
# when naming specific parameters order does not matter
total_marks(science=98, hindi=43, maths=89, physics=94, english=73)
