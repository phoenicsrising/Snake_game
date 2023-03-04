import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="My Snake Game",
    options={"build_exe": {"packages":["pygame"], "include_files":["snake.py", "food.py", "scoreboard.py"]}},
    executables=executables
)
