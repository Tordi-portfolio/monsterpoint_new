from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db import models
from django.contrib.auth.models import User

class Shipment(models.Model):
    SERVICE_CHOICES = [
        ('Express', 'Express'),
        ('Standard', 'Standard'),
        ('Economy', 'Economy'),
        ('Customs clearance (Bounded)', 'Customs clearance (Bounded)'),
        ('China to UAE as FCL and LCL', 'China to UAE as FCL and LCL'),
        ('Courier air Shipping to Lebanon', 'Courier air Shipping to Lebanon'),
        ('Transportation Service To All Over The World', 'Transportation Service To All Over The World'),
        ('Warehousing. Storage and handling services.', 'Warehousing. Storage and handling services.'),
        ('FCL & LCL Shipping by sea all over the world.', 'FCL & LCL Shipping by sea all over the world.'),
        ('Door to DOOR FTL land shipping to GCC Country', 'Door to DOOR FTL land shipping to GCC Country'),
    ]

    COMMODITY_CHOICES = [
        ('Platinum Fan', 'Platinum Fan'),
        ('Gold Fan', 'Gold Fan'),
        ('Silver Fan', 'Silver Fan'),
        ('Bronze Fan', 'Bronze Fan'),
        ('Vip Fan', 'Vip Fan'),
        ('Fertilizers', 'Fertilizers'),
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('books', 'Books'),
        ('home', 'Home'),
        ('toys', 'Toys'),
        ('car', 'Car'),
        ('bicycle', 'Bicycle'),
        ('clothe', 'Clothe'),
        ('shoe', 'Shoe'),
        ('bag', 'Bag'),
        ('gun', 'Gun'),
        ('cap', 'Cap'),
        ('house', 'House'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracking_id = models.CharField(max_length=20, unique=True, editable=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    commodity = models.CharField(max_length=100, choices=COMMODITY_CHOICES)
    destination_country = models.CharField(max_length=100)
    destination_country_state = models.CharField(max_length=100)
    destination_country_town = models.CharField(max_length=100)
    current_location = models.CharField(max_length=100, default='Processing', editable=False)
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('In Transit', 'In Transit'),
        ('At Customs', 'At Customs'),
        ('Delivered', 'Delivered'),
    ], default='Processing')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.tracking_id:
            self.tracking_id = self.generate_tracking_id()
        super().save(*args, **kwargs)

    def generate_tracking_id(self):
        return 'TRK-' + str(uuid.uuid4()).split('-')[0].upper()

    def __str__(self):
        return f"{self.tracking_id} - {self.full_name}"


