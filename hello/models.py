from django.db import models

#Model for Product
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/') # For cosmetic photos

    def __str__(self):
        return self.name

#Model for Feedback
class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.IntegerField() # Numeric rating (e.g., 1-5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating: {self.rating} for {self.product.name}"
    
#Model for Contact Message
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, default="Product Request")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"