def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
test_function()
# inner_function нельзя вызвать вне функции test_function,
# тк inner_function находится в локальной области видимости test_function.
