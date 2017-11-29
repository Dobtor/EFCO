class TestModelA(common.TransactionCase):
    def test_some_action(self):
        self._cr.execute(
            'select "FKClass" FKClass from dobtor_products_extend_products_relational'
        )
        res = []
        for item in self._cr.fetchall():
            print item
        #     res = res + [{
        #         "classType": item.FKClass
        #     }]
        # return res
