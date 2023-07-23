from .models import Product

Product.delete_expired_instances(repeat=60)  # Repeat  seconds
