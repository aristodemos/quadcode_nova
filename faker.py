import random

class Faker:
    def __init__(self):
        # List of sample cryptocurrency names and codes
        self.cryptocurrencies = [
            "Bitcoin",
            "Ethereum",
            "Litecoin",
            "Cardano",
            "Polkadot",
            "Ripple",
            "Chainlink",
            "Binance Coin",
            "Tezos",
            "Monero"
        ]
        self.codes = [
            "BTC",
            "ETH",
            "LTC",
            "ADA",
            "DOT",
            "XRP",
            "LINK",
            "BNB",
            "XTZ",
            "XMR"
        ]
        # List of lorem ipsum sentences
        self.lorem_ipsum_sentences = [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
            "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "Curabitur pretium tincidunt lacus.",
            "Nulla gravida orci a odio.",
            "Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris.",
            "Integer in mauris eu nibh euismod gravida.",
            "Duis ac tellus et risus vulputate vehicula."
        ]

    def cryptocurrency_name(self):
        return random.choice(self.cryptocurrencies)

    def cryptocurrency_code(self):
        return random.choice(self.codes)

    def sentences(self, number_of_sentences=1):
        # Randomly select the specified number of sentences from the lorem ipsum list
        return ' '.join(random.choices(self.lorem_ipsum_sentences, k=number_of_sentences))

# Example usage:
# faker = Faker()
# print(faker.cryptocurrency_name())  # Prints a random cryptocurrency name
# print(faker.cryptocurrency_code())  # Prints a random cryptocurrency ticker code
# print(faker.sentences(3))  # Prints 3 random lorem ipsum sentences
