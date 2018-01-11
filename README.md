---------
Python Module for managing [financier](https://financier.io/)

DISCLAIMER: not a official API from financier
============

That module allows you insert transactions and payee on financier.

Install
------------------
```console
$ pip install python-financier
```

USAGE
----------------

```js
from pythonfinancier.financier import Financier

f= Financier('https://app.financier.io/db/', EMAIL, PASSWORD)

f.connect_budget('Personal')

f.save_transaction('nubank', '1031b19e-a165-4aea-afd1-gggg4b2a00000', 400, '2017-10-10', 'Carrefour', 'teste memo') #acount, id, value, date, payee, memo

```

Notes: 
- If payee doesn't exists, it will create a new one.
- That script will use the suggest_category on payee, so will automatically import transactions using the previously category set for thath payee

FINDING ALL ACCOUNTS AVAILABLE
----------------


```js
from pythonfinancier.financier import Financier

f= Financier('https://app.financier.io/db/', EMAIL, PASSWORD)

print(f.get_all_budgets())


```

**ENJOY!!**
