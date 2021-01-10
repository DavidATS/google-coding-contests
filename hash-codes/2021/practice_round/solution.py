import logging

from lib_class import ObjectBuilder
from lib_class import PizzaProvider
from lib_class import SolutionFileBuilder


def solution(file_name, initial):

    logging.basicConfig(level="INFO")

    logging.info("Processing File")
    objects = ObjectBuilder(file_name)
    objects.run()
    # print(objects.pizzas)
    # print(objects.teams)

    logging.info("Finding pizzas for the teams")
    pizza_manager = PizzaProvider(objects.pizzas, objects.teams)
    pizza_manager.run()
    # print((pizza_manager.teams))
    # print((pizza_manager.dispatched_teams))
    # print((pizza_manager.pizzas))

    logging.info("Building solution file")
    solution_builder = SolutionFileBuilder(
        pizza_manager.dispatched_teams, initial
    )
    solution_builder.run()
