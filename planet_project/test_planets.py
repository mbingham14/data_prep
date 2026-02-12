from planet_classes import *
import pytest

earth = planet(name = "Earth", color = "blue", radius = 1)
saturn = planet(name = "Saturn", color = "yellow", radius = 0.4)
jupitar = planet(name = "Jupitar", color = "red", radius = 0.02)

luna = moon(name = "Moon", color = "White", radius = 1, tidally_locked = True, planet_companion = earth)
europa = moon(name = "Europa", color = "White", radius = 1, tidally_locked = True, planet_companion = jupitar)
hyperion = moon(name = "Hyperion", color = "White", radius = 1, tidally_locked = False, planet_companion = saturn)
