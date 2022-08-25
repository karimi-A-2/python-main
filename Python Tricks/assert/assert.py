def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Fancy Shoes', 'price': 14900}
print(apply_discount(shoes, 0.25))
print(apply_discount(shoes, 2.0))

# assert_stmt ::= "assert" expression1 ["," expression2]

# if __debug__:
#     if not expression1:
#         raise AssertionError(expression2)

# if cond == 'x':
#     do_x()
# elif cond == 'y':
#     do_y()
# else:
#     assert False, (
#         'This should never happen, but it does '
#         'occasionally. We are currently trying to '
#         'figure out why. Email dbader if you '
#         'encounter this in the wild. Thanks!')

# wrong:
# def delete_product(prod_id, user):
#     assert user.is_admin(), 'Must be admin'
#     assert store.has_product(prod_id), 'Unknown product'
#     store.get_product(prod_id).delete()

# correct:
# def delete_product(product_id, user):
#     if not user.is_admin():
#         raise AuthError('Must be admin to delete')
#     if not store.has_product(product_id):
#         raise ValueError('Unknown product id')
#     store.get_product(product_id).delete()

# assert (1 == 2, 'This should fail')

# counter = 10
# assert (
#     counter == 10,
#     'It should have counted all the items'
# )
