from dataclasses import dataclass
from pprint import pprint


@dataclass
class Place:
    name: str
    population: int


@dataclass
class Categorized:
    name: str
    category: str


main = (
    lambda: (
        places := [
            Place(name="Nuevo Progreso", population=2_704),
            Place(name="San Marcos", population=47_063),
            Place(name="Xela", population=180_706),
        ]
    )
    and (
        categorized_places := [
            *map(
                lambda place: (population := place.population)
                and (
                    category := (
                        "village"
                        if population < 5_000
                        else "town"
                        if population < 100_000
                        else "city"
                    )
                )
                and Categorized(name=place.name, category=category),
                places,
            )
        ]
    )
    and pprint(categorized_places)
)


main() if __name__ == "__main__" else None
