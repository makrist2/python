from .invoice import Invoice


class SuperShop:

    def __init__(self):
        self.total_income = 0
        self._storage_facilities = None
        self.invoices = []
        self.customers = []

    def __str__(self):
        items_dict = {}
        if self._storage_facilities:
            for item in self._storage_facilities.get_item():
                if item.__class__.__name__ not in items_dict:
                    items_dict[item.__class__.__name__] = 0
                items_dict[item.__class__.__name__] += 1

        invoice_dict = {}
        for invoice in self.invoices:
            if invoice.product.__class__.__name__ not in invoice_dict:
                invoice_dict[invoice.product.__class__.__name__] = 0
            invoice_dict[invoice.product.__class__.__name__] += invoice.income

        output = ""
        output += "Customers: %i\n" % len(self.customers)
        output += "Total income: %i\n" % self.total_income
        output += "Income per product:\n"
        for inv in invoice_dict:
            output += "    %s: %i\n" % (inv, invoice_dict[inv])
        output += "Goods left:\n"
        for item in items_dict:
            output += "    %s| %i\n" % (item, items_dict[item])

        return output

    def add_store(self, store):
        self._storage_facilities = store

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def sell(self, customer_id, item_id):
        in_number = len(self.invoices) + 1
        items = self._storage_facilities.get_item()
        invoice = Invoice(in_number, self.customers[customer_id], items[item_id])
        self.add_invoice(invoice)
        self.total_income += invoice.income
        self._storage_facilities.remove_item(items[item_id])