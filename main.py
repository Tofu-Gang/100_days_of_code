from os import getcwd, sep, listdir


def run_program() -> None:
    cwd = getcwd()
    day = input("What day's challenge do you want to run?\n")
    day = "day_" + (3 - len(day)) * "0" + day
    directories = listdir(cwd + sep + "src")
    directory = next(filter(lambda dir_name: day in dir_name, directories))
    filename = directory[8:]
    module = __import__("src." + directory + "." + filename, fromlist=[""])
    module.run_program()


if __name__ == "__main__":
    print("100 Days of Code")
    print("The Complete Python Pro Bootcamp")
    run_program()
