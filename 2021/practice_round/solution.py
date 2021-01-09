from lib_class import ObjectBuilder
from lib_class import PizzaProvider
from lib_class import SolutionFileBuilder


def solution(file_name):
    objects = ObjectBuilder(file_name)
    objects.run()
    # print(objects.pizzas)
    # print(objects.teams)
    pizza_manager = PizzaProvider(objects.pizzas, objects.teams)
    pizza_manager.run()
    # print((pizza_manager.teams))
    # print((pizza_manager.dispatched_teams))
    # print((pizza_manager.pizzas))
    solution_builder = SolutionFileBuilder(
        pizza_manager.dispatched_teams, file_name
    )
    solution_builder.run()
