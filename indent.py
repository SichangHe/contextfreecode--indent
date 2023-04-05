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


def main():
    places = [
        Place(name="Nuevo Progreso", population=2_704),
        Place(name="San Marcos", population=47_063),
        Place(name="Xela", population=180_706),
    ]

    categorized_places = [
        *map(
            lambda place: Categorized(
                name=place.name,
                category=(
                    "village"
                    if place.population < 5_000
                    else "town"
                    if place.population < 100_000
                    else "city"
                ),
            ),
            places,
        )
    ]

    ############################################################################
    ############################# Using function. ##############################
    ############################################################################

    # def categorize(place: Place) -> Categorized:
    #     population = place.population
    #     # Branch on population.
    #     if population < 5_000:
    #         category = "village"
    #     elif population < 100_000:
    #         category = "town"
    #     else:
    #         category = "city"
    #     return Categorized(name=place.name, category=category)
    #
    # categorized_places = [*map(categorize, places)]

    ############################################################################
    ######################### Using walrus operator. ###########################
    ############################################################################

    # categorized_places = [
    #     *map(
    #         lambda place: (population := place.population)
    #         and (
    #             category := (
    #                 "village"
    #                 if population < 5_000
    #                 else "town"
    #                 if population < 100_000
    #                 else "city"
    #             )
    #         )
    #         and Categorized(name=place.name, category=category),
    #         places,
    #     )
    # ]
    pprint(categorized_places)


if __name__ == "__main__":
    main()
