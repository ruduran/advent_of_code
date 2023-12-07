from collections import defaultdict
from typing import Set, Tuple, Dict
from aoc2020.common import get_file_name


def read_food_info() -> Tuple[Dict[str, int], Dict[str, Set[str]], Dict[str, Set[str]]]:
    all_ingredients = defaultdict(int)
    allergen_ingredients = {}
    with open(get_file_name()) as file:
        for line in file:
            line = line.strip()
            line_split = line.split(' (contains ')
            ingredients = line_split[0].split(' ')
            allergens = line_split[1][:-1].split(', ')

            for ingredient in ingredients:
                all_ingredients[ingredient] += 1

            for allergen in allergens:
                if allergen in allergen_ingredients:
                    allergen_ingredients[allergen] &= set(ingredients)
                else:
                    allergen_ingredients[allergen] = set(ingredients)

    ingredient_possible_allergens = defaultdict(set)
    for allergen, ingredients in allergen_ingredients.items():
        for ingredient in ingredients:
            ingredient_possible_allergens[ingredient].add(allergen)

    return all_ingredients, allergen_ingredients, ingredient_possible_allergens


def refine_ingredient_allergens(ingredient_possible_allergens: Dict[str, Set[str]]) -> Dict[str, str]:
    found_allergens = set()
    while not len(found_allergens) == len(ingredient_possible_allergens):
        for ingredient, allergens in sorted(ingredient_possible_allergens.items(), key=lambda i: len(i[1])):
            if len(allergens) > 1:
                allergens -= found_allergens

            if len(allergens) == 1:
                found_allergens |= allergens

    return {ingredient: list(allergens)[0] for ingredient, allergens in ingredient_possible_allergens.items()}


def main():
    ingredients, allergen_ingredients, ingredient_possible_allergens = read_food_info()

    ingredients_without_allergens_occurrences = 0
    for ingredient, occurrences in ingredients.items():
        if ingredient not in ingredient_possible_allergens:
            ingredients_without_allergens_occurrences += occurrences

    print(ingredients_without_allergens_occurrences)

    ingredient_allergens = refine_ingredient_allergens(ingredient_possible_allergens)
    print(','.join(t[0] for t in sorted(ingredient_allergens.items(), key=lambda i: i[1])))


if __name__ == '__main__':
    main()
