cart = []

id_user = input("Insira o id do usuário:")
id_produto = input("Insira o id do produto:")
price_product = float(input("Insira o preço do produto:"))
quantity_product = int(input("Insira a quantidade de produto:"))

item = [id_produto, id_user, price_product, quantity_product]

def add_item_cart():
    cart.append(item)
    return cart





# def get_all_items_cart():
#     #return todos os itens do carrinho
#     pass

# def get_item_cart_by_id(id_product):
#     pass

# def remove_item_id(id_product):
#     #remover o item do carrinho que tem esse produto
#     pass