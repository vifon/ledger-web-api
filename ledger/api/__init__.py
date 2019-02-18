#!/usr/bin/env python3

import time

template = """
{date} {payee}
    {account_to:<34s}  {amount:>16}
    {account_from}
""".rstrip()

def create_entry(payee, account_from, account_to, amount):
    date = time.strftime("%F")
    return template.format(**locals())
