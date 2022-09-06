# celular = '123'
# figurinha = '456'

# carts = [['123', '1', 800.00, 1], ['456', '1', 40.00, 2]]

# for cart in carts:
#     if cart[0] == celular:
#         print('item ->', cart)

#id produto, id usuario, preço, quantidade

carts = [['123', '1', 100.00, 2], ['456', '1', 899.00, 1]]

new_lista = []
for item in carts:
#    print(item)
    if item[0] == '123':
        new_lista.append(item)

print(new_lista)

new_list = [item[2] for item in carts if item[0] == '123']
print(new_list[0])

def filtra_item(item, product):
    if item[0] == product:
        return item

n_list = filter(lambda elem: elem[0] == '123', carts)
print(list(n_list))