from financier import Financier

class Downloader:
    URL = 'https://app.financier.io/db/'

    def __init__(self, email, password):
        self.f = Financier(self.URL, email, password)
        self.budgets = []
        self.budget = ''
        self.data = {}

    def fetch_budgets(self):
        self.budgets = self.f.get_all_budgets()
        print('budgets downloaded')
        return self.budgets

    def connect_budget(self,name):
        self.f.connect_budget(name)
        self.budget = name
        self.data = {}
        print('connected on budget "{}"'.format(name))

    def fetch_accounts(self):
        self.data['accounts'] = self.f.get_all_accounts()
        print('accounts downloaded')
        return self.data['accounts']

    def fetch_categories(self):
        self.data['categories'] = self.f.get_all_master_categories()
        print('categories downloaded')
        return self.data['categories']

    def fetch_subcategories(self):
        self.data['subcategories'] = self.f.get_all_categories()
        print('sub-categories downloaded')
        return self.data['subcategories']

    def fetch_month_categories(self):
        self.data['month_categories'] = self.f.get_all_month_categories()
        print('monthly budget amounts downloaded')
        return self.data['month_categories']

    def fetch_transactions(self):
        self.data['transactions'] = self.f.get_all_transactions()
        print('transactions downloaded')
        return self.data['transactions']

    def fetch_all(self):
        if self.budget == '':
            print('no budget connected\nfetch aborted')
            return None
        else:
            self.fetch_accounts()
            self.fetch_categories()
            self.fetch_subcategories()
            self.fetch_month_categories()
            self.fetch_transactions()
            return self.data


class Budget:

    def __init__(self,data):
        self.data = data

    def __getattr__(self, key):
        if key not in self.data:
            raise AttributeError("'{}' object has no attribute '{}'".format(
                self.__class__.__name__, key))
        return self.data[key]

    def __setattr__(self, key, value):
        self.data[key] = value

    