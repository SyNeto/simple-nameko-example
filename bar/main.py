from nameko.rpc import rpc


class Bar:
    name = 'bar'
    drinks = ['modelo', 'xx', 'mezcal montelobos', 'ultra']

    @rpc
    def get_menu(self):
        return self.drinks

    @rpc
    def get_a_drink(self, drink):
        if drink in self.drinks:
            return f'Toma tu bebida {drink}'
        else:
            return f'No se la manejo joven'