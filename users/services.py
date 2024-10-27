import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

def create_stripe_product(payment):
    """ Создает новый продукт в stripe. """
    tmp = payment.paid_course if payment.paid_course else payment.paid_lesson
    product = stripe.Product.create(name=tmp.name)
    return product.id

def create_stripe_price(product_id, payment):
    """ Создает цену в stripe. """
    price = stripe.Price.create(
      currency="usd",
      unit_amount=int(payment.amount) * 100,
      product=product_id,
    )
    return price.id

def create_stripe_session(price_id):
    """ Создает сессию в stripe. """
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url