#!/usr/bin/env python3

from flask import Flask
from flask_api import status
import os

import ledger.api

app = Flask(__name__)

@app.route("/amount/<amount>", methods=['POST'])
def add_basic_payment(amount):
    amount = amount.replace(",", ".").strip()
    entry = ledger.api.create_entry(
        payee="AUTOMATIC",
        account_from="Liabilities:Karta kredytowa",
        account_to="Uncategorized",
        amount=amount,
    )
    with open(os.environ['LEDGER_PATH'], 'a') as ledger_file:
        print(entry, file=ledger_file)
    return "", status.HTTP_201_CREATED
