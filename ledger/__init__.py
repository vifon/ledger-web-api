#!/usr/bin/env python3

from flask import Flask
from flask_api import status

import ledger.api

app = Flask(__name__)


@app.route("/amount/<amount>", methods=['POST'])
def add_basic_payment(amount):
    return add_complex_payment(
        payee="AUTOMATIC",
        account_from="Liabilities:Karta kredytowa",
        account_to="Uncategorized",
        amount=amount,
    )


@app.route("/account_from/<account_from>/account_to/<account_to>/payee/<payee>/amount/<amount>", methods=['POST'])
def add_complex_payment(account_from, account_to, payee, amount):
    amount = amount.replace(",", ".").strip()
    entry = ledger.api.Entry(
        payee=payee,
        account_from=account_from,
        account_to=account_to,
        amount=amount,
    )
    entry.store()
    return str(entry), status.HTTP_201_CREATED
