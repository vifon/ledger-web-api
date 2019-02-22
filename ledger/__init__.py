#!/usr/bin/env python3

from flask import Flask, Response
from flask_api import status
import os

import ledger.api

app = Flask(__name__)

LEDGER_PATH = os.environ['LEDGER_PATH']


@app.route("/account_from/<account_from>/account_to/<account_to>/payee/<payee>/amount/<amount>", methods=['POST'])
def add_payment(account_from, account_to, payee, amount):
    amount = amount.replace(",", ".").strip()
    entry = ledger.api.Entry(
        payee=payee,
        account_from=account_from,
        account_to=account_to,
        amount=amount,
    )
    entry.store(LEDGER_PATH)
    return str(entry), status.HTTP_201_CREATED


@app.route("/accounts", methods=['GET'])
def list_accounts():
    body = "\n".join(ledger.api.accounts(LEDGER_PATH))
    return Response(body, mimetype="text/plain")
