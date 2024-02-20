import json
from dataclasses import dataclass
from datetime import datetime

import requests

ALPHAVANTAGE_API_KEY = "LF4MQ3MEGDSC7LQV"
MIDDLE_CURRENCY = "CHF"
logs = []


@dataclass
class Price:
    value: float
    currency: str

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(
                value=(self.value + other.value), currency=self.currency
            )

        left_in_middle: float = convert(
            value=self.value,
            currency_from=self.currency,
            currency_to=MIDDLE_CURRENCY,
        )
        right_in_middle: float = convert(
            value=other.value,
            currency_from=other.currency,
            currency_to=MIDDLE_CURRENCY,
        )

        total_in_middle: float = left_in_middle + right_in_middle
        total_in_left_currency: float = convert(
            value=total_in_middle,
            currency_from=MIDDLE_CURRENCY,
            currency_to=self.currency,
        )

        return Price(value=total_in_left_currency, currency=self.currency)


def convert(value: float, currency_from: str, currency_to: str) -> float:
    response: requests.Response = requests.get(
        f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={ALPHAVANTAGE_API_KEY}"
    )
    result: dict = response.json()
    coefficient: float = float(
        result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    )

    logs.append(
        {
            "currency_from": result["Realtime Currency Exchange Rate"][
                "1. From_Currency Code"
            ],
            "currency_to": result["Realtime Currency Exchange Rate"][
                "3. To_Currency Code"
            ],
            "rate": result["Realtime Currency Exchange Rate"][
                "5. Exchange Rate"
            ],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

    return value * coefficient


flight = Price(value=200, currency="UAH")
hotel = Price(value=1000, currency="USD")

total: Price = flight + hotel
print(total)

with open("logs.json", "a") as file:
    json.dump({"results": logs}, file, indent=2)
