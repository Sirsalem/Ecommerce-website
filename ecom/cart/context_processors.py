from .cart import Cart

# lets create a context_processor so our cart can work on all pages

def cart(request):
    #  return the default data from our cart
    return {'cart':Cart(request)}