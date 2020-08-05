class DivByZero:
    @staticmethod
    def div_by_zero(devider, denominator):
        try:
            return f'Результат деления: {devider / denominator}'
        except:
            return 'Ошибка деления на ноль'


print(DivByZero.div_by_zero(64, 8))
print(DivByZero.div_by_zero(32, 0))
div = DivByZero()
print(div.div_by_zero(10, 4))
print(div.div_by_zero(10, 0))
