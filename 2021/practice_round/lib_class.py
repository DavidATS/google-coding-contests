from datetime import datetime
from typing import List

from tqdm import tqdm


class Pizza:
    def __init__(self, ingredients, index):
        self.ingredients = set(ingredients)
        self.index = index

    def __repr__(self):
        return f"Pizza {self.index}"


class Team:
    def __init__(self, size: int):
        self.size = size
        self.order = []
        self.ingredients = set()

    @property
    def remaining_pizzas(self):
        return self.size - len(self.order)

    @property
    def is_complete(self):
        return self.remaining_pizzas == 0

    def add_pizza(self, pizza: Pizza):
        self.order.append(pizza)
        for ingredient in pizza.ingredients:
            self.ingredients.add(ingredient)

    def __repr__(self):
        return f"Team size {self.size} | {str(self.order)}"


class ObjectBuilder:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.teams = []
        self.pizzas = []

    def run(self):

        first_line = True

        with open(self.file_name, "r") as file:
            c = 0
            for line in tqdm(file):
                if first_line:
                    teams_data = line.split(" ")
                    teams_data.pop(0)
                    size = 2
                    for team_data in teams_data:
                        team_data = int(team_data)
                        for i in range(team_data):
                            self.teams.append(Team(size))
                        size += 1
                    first_line = False
                else:
                    pizza_data = line.split(" ")
                    pizza_data.pop(0)
                    self.pizzas.append(Pizza(pizza_data, c))
                    c += 1


class PizzaProvider:
    def __init__(self, pizzas: List[Pizza], teams: List[Team]):
        self.pizzas = pizzas
        self.teams = teams
        self.dispatched_teams = []

    def run(self):
        while self._can_dispatch:
            current_team = self._choose_team()
            while not current_team.is_complete:
                pizza_to_add = self._dispatch(current_team)
                current_team.add_pizza(pizza_to_add)
            self.dispatched_teams.append(current_team)

    @property
    def _can_dispatch(self):
        return len(self.pizzas) >= min(self.teams, key=lambda t: t.size).size

    def _choose_team(self):
        # ToDo: hash teams by size to make this method constant
        remaining_pizzas = len(self.pizzas)
        for index, team in enumerate(self.teams):
            if not team.is_complete:
                if team.size <= remaining_pizzas:
                    return self.teams.pop(index)

    def _dispatch(self, team: Team):
        """
        We choose the pizza with the max number of
        different ingredients each time
        """

        best_pizza = self.pizzas[0]
        best_pizza_index = 0
        same_ingredients = best_pizza.ingredients.intersection(
            team.ingredients
        )
        max_new_ingredients = len(
            best_pizza.ingredients.symmetric_difference(same_ingredients)
        )

        for index, c_pizza in enumerate(self.pizzas):
            # intersection and then symmetric_difference
            same_ingredients = c_pizza.ingredients.intersection(
                team.ingredients
            )
            new_ingredients = c_pizza.ingredients.symmetric_difference(
                same_ingredients
            )
            if len(new_ingredients) >= max_new_ingredients:
                best_pizza = c_pizza
                max_new_ingredients = len(new_ingredients)
                best_pizza_index = index

        return self.pizzas.pop(best_pizza_index)


class SolutionFileBuilder:
    def __init__(self, teams: List[Team], input_file_data: str):
        self.teams = teams
        self.input_file_data = input_file_data
        self.FOLDER_PATH = "solutions/"

    def run(self):
        solution_file_n = (
            self.FOLDER_PATH
            + self.input_file_data
            + "_"
            + "solution_"
            + str(datetime.now())
        )
        with open(solution_file_n, "a") as file:
            file.write(f"{len(self.teams)}\n")
            for team in self.teams:
                print(team)
                team_data = f"{team.size}"
                for pizza in team.order:
                    team_data += f" {pizza.index}"
                file.write(team_data + "\n")
