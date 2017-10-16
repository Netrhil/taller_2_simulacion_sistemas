from cx_Freeze import setup, Executable

base = None


executables = [Executable("simulacion_gregory-leibniz.py", base=base)]

packages = ["idna"]

setup(
    name = "Simulacion_Montecarlo",
    version = "1",
    description = 'Empaquetado desde python de la simulacion de montecarlo',
    executables = executables
)
