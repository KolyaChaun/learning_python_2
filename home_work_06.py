currency_exchange = {
    "EUR_to_CHF": 0.94,
    "USD_to_CHF": 1.14,
    "UAH_to_CHF": 0.02,
    "CHF_to_EUR": 1.027,
    "CHF_to_USD": 1.116,
    "CHF_to_UAH": 42.42,
}


class Price:
    def __init__(self, value: float, currency: str) -> None:
        self.value: float = value
        self.currency: str = currency

    def __add__(self, other) -> "Price":
        if self.currency == other.currency:
            total: float = round(self.value + other.value, 2)
            return Price(value=total, currency=self.currency)
        else:
            if self.currency == "EUR":
                first_value: float = (
                    self.value * currency_exchange["EUR_to_CHF"]
                )
                if other.currency == "USD":
                    second_value: float = (
                        other.value * currency_exchange["USD_to_CHF"]
                    )
                if other.currency == "UAH":
                    second_value: float = (
                        other.value * currency_exchange["UAH_to_CHF"]
                    )
                total_in_CHF: float = first_value + second_value
                total = round(
                    total_in_CHF * currency_exchange["CHF_to_EUR"], 2
                )
                return Price(value=total, currency=self.currency)
            if self.currency == "USD":
                first_value: float = (
                    self.value * currency_exchange["USD_to_CHF"]
                )
                if other.currency == "EUR":
                    second_value: float = (
                        other.value * currency_exchange["EUR_to_CHF"]
                    )
                if other.currency == "UAH":
                    second_value: float = (
                        other.value * currency_exchange["UAH_to_CHF"]
                    )
                total_in_CHF: float = first_value + second_value
                total = round(
                    total_in_CHF * currency_exchange["CHF_to_USD"], 2
                )
                return Price(value=total, currency=self.currency)
            if self.currency == "UAH":
                first_value: float = (
                    self.value * currency_exchange["UAH_to_CHF"]
                )
                if other.currency == "EUR":
                    second_value: float = (
                        other.value * currency_exchange["EUR_to_CHF"]
                    )
                if other.currency == "USD":
                    second_value: float = (
                        other.value * currency_exchange["USD_to_CHF"]
                    )
                total_in_CHF: float = first_value + second_value
                total = round(
                    total_in_CHF * currency_exchange["CHF_to_UAH"], 2
                )
                return Price(value=total, currency=self.currency)

    # Operations with minus only for the same currencies
    def __sub__(self, other) -> "Price":
        if self.currency == other.currency:
            sub: float = round(self.value - other.value, 2)
            return Price(value=sub, currency=self.currency)
        else:
            notice: str = "Operations with minus only for the same currencies"
            return notice

    def __str__(self):
        return f"{self.value} in {self.currency}"


flight = Price(value=395, currency="UAH")
hotel = Price(value=950.5, currency="EUR")


add = flight + hotel
print(add)

sub = hotel - flight
print(sub)
