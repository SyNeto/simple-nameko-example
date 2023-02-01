from nameko.rpc import rpc, RpcProxy


class Waiter:
    name = 'waiter'
    bar = RpcProxy('bar')

    @rpc
    def get_menu(self):
        return self.bar.get_menu()

    @rpc
    def get_a_drink(self, drink):
        return self.bar.get_a_drink(drink)