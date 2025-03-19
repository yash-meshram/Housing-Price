from abc import ABC, abstractmethod


# step 1: defining the strategy interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# step 2: defining the concrete strategies
class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} Rs. using Credit Card"


class DebitCard(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} Rs. using Debit Card"


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} Rs. using PayPal"


# step 3: defining the context
class ShoppingCart:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def checkout(self, amount):
        return self.payment_method.pay(amount)


# step 4: using the context to use the strategy
if __name__ == "__main__":
    payment_methods = {1: CreditCard, 2: DebitCard, 3: PayPalPayment}

    while True:
        try:
            amount = float(input("Enter the amount to pay (in Rs.): "))
            break
        except ValueError:
            print("Invalid amount, Try again.")

    while True:
        try:
            payment_method = int(
                input(
                    "1 = Credit Card, 2 = Debit Card, 3 = PayPal\nEnter the payment method: "
                )
            )
            if payment_method in [1, 2, 3]:
                shopping_cart = ShoppingCart(payment_methods[payment_method]())
                print(shopping_cart.checkout(amount))
                break
            else:
                print("Invalid payment method, Try again.")
        except ValueError:
            print("Invalid payment method, Try again.")
