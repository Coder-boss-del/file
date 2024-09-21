# create a class for  currency exchanges for 

# GBD
# USD
# EUR
# AUG
# CAD
# JPY

class CurrencyExchange:
    def __init__(self):
        # Initial exchange rates (base: USD)
        self.rates = {
            'GBP': 0.75,
            'USD': 1.00,
            'EUR': 0.85,
            'AUD': 1.35,
            'CAD': 1.25,
            'JPY': 110.00
        }

    def set_rate(self, currency, rate):
        """Set the exchange rate for a specific currency."""
        if currency in self.rates:
            self.rates[currency] = rate
        else:
            raise ValueError(f"Unsupported currency: {currency}")

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount from one currency to another."""
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Unsupported currency for conversion.")

        # Convert amount to USD first
        amount_in_usd = amount / self.rates[from_currency]
        # Convert from USD to the target currency
        converted_amount = amount_in_usd * self.rates[to_currency]
        return converted_amount

    def list_rates(self):
        """Return a list of current exchange rates."""
        return self.rates

# Example usage
if __name__ == "__main__":
    exchange = CurrencyExchange()
    
    print("Current exchange rates:")
    print(exchange.list_rates())
    
    # Convert 100 USD to EUR
    amount = 100
    converted = exchange.convert(amount, 'USD', 'EUR')
    print(f"{amount} USD is {converted:.2f} EUR")
    
    # Set a new exchange rate for JPY
    exchange.set_rate('JPY', 115.00)
    print("Updated exchange rates:")
    print(exchange.list_rates())
