#!/usr/bin/env python3

import os
import time


class Entry:
    """A single Ledger entry.

    >>> entry = Entry(
    ...    payee="Burger King",
    ...    account_from="Liabilities:Credit Card",
    ...    account_to="Expenses:Food",
    ...    amount="19.99 PLN",
    ...    date="2019-02-15",
    ... )

    >>> print(entry)
    <BLANKLINE>
    2019-02-15 Burger King
        Expenses:Food                              19.99 PLN
        Liabilities:Credit Card
    """

    template = """
{date} {payee}
    {account_to:<34s}  {amount:>12.2f} PLN
    {account_from}
""".rstrip()

    def __init__(self, **kwargs):
        self.payee = kwargs['payee']
        self.account_from = kwargs['account_from']
        self.account_to = kwargs['account_to']
        self.amount = float(kwargs['amount'].split()[0])
        self.date = kwargs.get('date', time.strftime("%F"))

    def __str__(self):
        return self.template.format(**vars(self))

    def store(self, ledger_path=None):
        if ledger_path is None:
            ledger_path = os.environ['LEDGER_PATH']
        with open(ledger_path, 'a') as ledger_file:
            print(self, file=ledger_file)


if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
