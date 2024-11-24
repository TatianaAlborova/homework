class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        try:
            file = open(self.__file_name, 'r')
            existing_products = [line.strip() for line in file.readlines()]
            file.close()
        except FileNotFoundError:
            existing_products = []

        for product in products:
            product_str = str(product)
            if product_str in existing_products:
                print(f'Продукт {product_str} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f"{product_str}\n")
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
