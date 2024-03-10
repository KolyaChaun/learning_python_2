import time

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class Currency(BaseModel):
    from_currency: str
    to_currency: str


last_response = None
last_request_time = 0


@app.post("/fetch-exchange-rate")
async def get_current_market_state(currency: Currency):
    global last_response, last_request_time

    current_time = time.time()
    if current_time - last_request_time < 10 and last_response is not None:
        return last_response

    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency.from_currency}&to_currency={currency.to_currency}&apikey=V2V43QAQ8RILGBOW"

    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)

    rate: str = response.json()["Realtime Currency Exchange Rate"][
        "5. Exchange Rate"
    ]

    last_response = {
        "from_currency": currency.from_currency,
        "to_currency": currency.to_currency,
        "rate": rate,
    }
    last_request_time = current_time

    return last_response
