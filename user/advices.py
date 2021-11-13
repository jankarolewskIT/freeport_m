import requests

from errors.validators import NotValidInput


class UserAdvices:
    def __init__(self):
        self.number = int(input("Number: "))
        self.advices = set()
        self.advices_dict = {}

    def validate_input(self) -> bool:
        """
        Check if given input is lower then 5 and greater then 20
        :return: bool
        """
        if not 5 <= self.number <= 20:
            raise NotValidInput("Your input is not valid")
        return True

    def create_advices(self, url: str) -> None:
        """
        Adds advices pulled from API to self.advices set.
        If given advice already existed in self.advices
        repeat the process

        :param url: API's url
        :return: None
        """
        prev_len = len(self.advices)
        response = requests.request("GET", url).json().get("slip")
        self.advices.add((response.get("id"), response.get("advice")))
        if prev_len == len(self.advices):
            self.create_advices(url)

    def serialize_advice(self) -> dict:
        """
        Create a dict from self.advices set.
        :return: dict
        """
        for advice in self.advices:
            self.advices_dict[advice[0]] = advice[1]

        return self.advices_dict
