class Startup:
    def __init__(self):
        self.title = [
            "Hi there! \n My name is Paca.",
            "Feel comfotable sharing with me whatever is on your mind",
            "What is your name?",
        ]
        self.sub_title = [
            "I'm your listening companion 😊",
            " ",
            # "It will never be shared without your consent! So worry not 😁",
            " ",
        ]
        self.is_button = [True, True, False]
        self.button_count = [1, 1, 0]
        self.button_text = ["Talk to Paca 😊", "Ok 😁", ""]
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
