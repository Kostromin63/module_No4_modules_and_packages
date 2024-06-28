def test_function():

    def inner_function():
        print('"Я в области видимости функции test_function"')

    inner_function()


test_function()
# inner_function() вызывает ошибку, т.к. фукция в недоступном пространстве из текущего контекста
