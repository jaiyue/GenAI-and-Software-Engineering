def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        i, j = planets.index(planet1), planets.index(planet2)
    except ValueError:
        return ()
    if i == j:
        return ()
    start, end = min(i, j), max(i, j)
    return tuple(planets[start + 1:end])

