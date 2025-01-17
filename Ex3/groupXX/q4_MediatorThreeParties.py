class Mediator:
    def __init__(self):
        self.parties = {}  # A dictionary to hold all parties

    def add_party(self, party):
        """Add a party to the mediator."""
        self.parties[party.name] = party

    def send_message(self, message, sender_name, receiver_name=None):
        if receiver_name:
            receiver = self.parties.get(receiver_name)
            if receiver:
                receiver.receive_message(message, sender_name)
            else:
                print(f"Message from {sender_name} could not be delivered. {receiver_name} not found.")
        else:
            for name, party in self.parties.items():
                if name != sender_name:
                    party.receive_message(message, sender_name)


class Party:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.add_party(self)  # Register this party with the mediator

    def send_message(self, message, receiver_name=None):
        if receiver_name:
            print(f"{self.name} sends to {receiver_name}: {message}")
        else:
            print(f"{self.name} broadcasts: {message}")
        self.mediator.send_message(message, self.name, receiver_name)

    def receive_message(self, message, sender_name):
        print(f"{self.name} receives a message from {sender_name}: {message}")


if __name__ == '__main__':

    mediator = Mediator()

    country_a = Party("CountryA", mediator)
    country_b = Party("CountryB", mediator)
    country_c = Party("CountryC", mediator)

    country_a.send_message("We propose a ceasefire agreement", country_b.name)
    country_b.send_message("We agree to the ceasefire. Let's involve CountryC.",country_c.name)
    country_c.send_message("We support the ceasefire. Let's finalize the terms.")
    country_a.send_message("Thank you all. Let's sign the agreement and ensure peace.")