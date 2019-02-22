ledger-web-api
==============

I created this service to automate adding the
[Ledger](https://www.ledger-cli.org/) entries from my mobile phone via
Tasker.  The defaults may be opinionated and may need adjustment for
the needs of others, the default currency in particular.

LAUNCHING
---------

For development/testing purposes, it's sufficient to run:

    $ env LEDGER_PATH=/path/to/my/ledger.dat ./app.py

For actual deployment I use [gunicorn](https://gunicorn.org/).  Example:

    $ env LEDGER_PATH=/path/to/my/ledger.dat gunicorn3 -w 2 -b 127.0.0.1:1234 ledger:app
    
It's recommended to use some reverse proxy like Nginx on top of it,
possibly with added authentication.

COPYRIGHT
---------

Copyright (C) 2019  Wojciech Siewierski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
