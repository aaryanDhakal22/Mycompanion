class Startup:
    def __init__(self):
        self.title = [
            "Hi there! My name is Bo",
            "Whatever you share with me will always be private",
            "What should I call you",
        ]
        self.sub_title = [
            "I can be you listening companion if you would like 😊",
            "It will never be shared without your consent! So worry not 😁",
            "Create you unique username",
        ]
        self.is_button = [True, True, False]
        self.button_count = [1, 1, 0]
        self.button_text = ["Sure 😊", "Oki😁", ""]
        self.is_done = False
        self.pos = 0
        self.name = None

    def return_info(self):
        index = self.pos
        return {
            "title": self.title[index],
            "subtitle": self.sub_title[index],
            "is_button": self.is_button[index],
            "button_count": self.button_count[index],
            "button_text": self.button_text[index],
            "name": self.name,
        }


starter = Startup()
