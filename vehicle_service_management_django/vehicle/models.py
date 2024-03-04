from django.db import models
from django.contrib.auth.models import User


from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    # address = models.CharField(max_length=40)
    
    mobile = models.CharField(max_length=20,null=False)
    
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
    @property
    def get_username(self):
        return self.user.username



class Mechanic(models.Model):
    DRIVER = 'driver'
    JOB_CHOICES = (
        ('mechanic', 'Mechanic'),
        ('painter', 'Painter'),
        ('Tester','Tester'),
        ('Operator','Operator'),
        (DRIVER, 'Delivery Driver'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/MechanicProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    job_title = models.CharField(max_length=20, choices=JOB_CHOICES, default='select title')
    qualification_certificate = models.FileField(upload_to='qualification_certificates/', null=True, blank=True)
    salary=models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Request(models.Model):
    cat=(('two wheeler with gear','two wheeler with gear'),('two wheeler without gear','two wheeler without gear'),('three wheeler','three wheeler'),('four wheeler','four wheeler'))
    category=models.CharField(max_length=50,choices=cat,null=True)

    vehicle_no=models.PositiveIntegerField(null=True)
    vehicle_name = models.CharField(max_length=40,null=True)
    vehicle_model = models.CharField(max_length=40,null=True)
    vehicle_brand = models.CharField(max_length=40,null=True)

    problem_description = models.CharField(max_length=500,null=True)
    date=models.DateField(auto_now=True)
    cost=models.PositiveIntegerField(null=True)

    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)

    stat=(('Pending','Pending'),('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'),('Released','Released'))
    status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)

    def __str__(self):
        return self.problem_description

class Attendance(models.Model):
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)
    date=models.DateField()
    present_status = models.CharField(max_length=10)

class Feedback(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=40)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name

# category
class Category(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField()

    def __str__(self):
        return self.name
#subcategory
class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    # description = models.TextField()

    def __str__(self):
        return self.name
#subsubcategory means my service
from django.db.models import F, Sum
class SubSubcategory(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='subsubcategories/', null=True, blank=True)  # Add an image field
    description = models.TextField(null=True, blank=True)  # Add a description field
    
    
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Add a price field
    hours_taken = models.PositiveIntegerField(null=True, blank=True)  # Add hours taken field
    
    

        
    def __str__(self):
        return self.name
    
class CarModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return self.name
class CarName(models.Model):
    name = models.CharField(max_length=100)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='type_images/')

    def __str__(self):
        return self.name

class Booking(models.Model):
    # service_name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    Alternative_mobile = models.CharField(max_length=20)
    selected_service_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    
    selected_subsubcategory = models.ForeignKey(SubSubcategory, on_delete=models.CASCADE)

    selected_car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True)
    selected_car_name = models.ForeignKey(CarName, on_delete=models.CASCADE, null=True)
    selected_type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    pincode = models.CharField(max_length=35, null=True, blank=True)
    stat=(('Pending','Pending'),('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'),('Released','Released'))
    status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)
    driver = models.ForeignKey(Mechanic, on_delete=models.CASCADE, related_name='assigned_bookings', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    PAYMENT_CHOICES = [
        ('Cash', 'Cash on Service'),
        ('Online', 'Online Pay'),
    ]

    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES,null=True)
    PICKUP_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    pickup_service = models.CharField(max_length=5, choices=PICKUP_CHOICES, default='No', null=True)
    

    # def save(self, *args, **kwargs):
    #     if self.selected_subsubcategory:
    #         self.selected_service_price = self.selected_service_price or 0
    #     super().save(*args, **kwargs)



    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.pincode:
            # Extract latitude and longitude from the pincode field
            latitude, longitude = self.pincode.split(',')
            self.latitude = float(latitude.strip())
            self.longitude = float(longitude.strip())
        super().save(*args, **kwargs)
    

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Success', 'Success'),
    ]

    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    payment_date = models.DateTimeField(auto_now_add=True, null=True)  # Use auto_now_add=True for initial creation


    def __str__(self):
        return f"Payment ID: {self.id}, Status: {self.payment_status}"
    

# class Blog(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     is_approved = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True) 
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def author_name(self):
        return self.author.customer.get_name if hasattr(self.author, 'customer') else self.author.username

    def __str__(self):
        return self.title