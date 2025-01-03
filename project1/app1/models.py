
from django.db import models
# Reservation model
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time} ({self.guests} guests)"


from django.db import models

# Menu model
class Menu(models.Model):
    Item_name = models.CharField(max_length=155)
    Item_prize = models.IntegerField()  # Price of the item
    Item_image = models.ImageField(upload_to='menu', default='default_image.jpg')
    

    def __str__(self):
        return f"{self.Item_name} - {self.Item_prize}"

# Order model
class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_contact = models.CharField(max_length=20)
    items = models.ManyToManyField(Menu, through='OrderItem')
    total_price = models.IntegerField(default=0)
    order_time = models.DateTimeField(auto_now_add=True)

    def calculate_total_price(self):
        # Calculate the total price by summing up the price of each ordered item
        self.total_price = sum(order_item.quantity * order_item.menu_item.Item_prize 
                                for order_item in self.orderitem_set.all())
        self.save()

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"

# OrderItem model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.Item_name}"
