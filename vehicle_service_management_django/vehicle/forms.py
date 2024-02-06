from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Category,Subcategory,SubSubcategory
from .models import CarModel,CarName,Type,Booking,Mechanic


from django.core.exceptions import ValidationError
from django.utils import timezone


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['mobile']

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class MechanicUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class MechanicForm(forms.ModelForm):
    job_title = forms.ChoiceField(
        choices=[('select title', 'select title'),('mechanic', 'Mechanic'), ('painter', 'Painter'), ('Tester','Tester'),
        ('Operator','Operator'), ('driver', 'Delivery Driver')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Job Title'
    )
    qualification_certificate = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='Qualification Certificate'
    )

    def clean_qualification_certificate(self):
        certificate = self.cleaned_data.get('qualification_certificate')
        if certificate:
            if not certificate.name.lower().endswith('.pdf'):
                raise forms.ValidationError('Please upload a PDF file for the qualification certificate.')
        return certificate

    class Meta:
        model=models.Mechanic
        fields=['address','mobile','profile_pic','job_title', 'qualification_certificate']
    
class MechanicSalaryForm(forms.Form):
    salary=forms.IntegerField();

class AssignDriverForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssignDriverForm, self).__init__(*args, **kwargs)
        self.fields['driver'].queryset = Mechanic.objects.filter(job_title='driver')

    driver = forms.ModelChoiceField(
        queryset=Mechanic.objects.filter(job_title='driver'),
        label='Select Driver',
        empty_label='Choose a driver'
    )

    class Meta:
        model = Booking
        fields = []
class RequestForm(forms.ModelForm):
    class Meta:
        model=models.Request
        fields=['category','vehicle_no','vehicle_name','vehicle_model','vehicle_brand','problem_description']
        widgets = {
        'problem_description':forms.Textarea(attrs={'rows': 3, 'cols': 30})
        }

class AdminRequestForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of customer model will be shown there in html
    customer=forms.ModelChoiceField(queryset=models.Customer.objects.all(),empty_label="Customer Name",to_field_name='id')
    mechanic=forms.ModelChoiceField(queryset=models.Mechanic.objects.all(),empty_label="Mechanic Name",to_field_name='id')
    cost=forms.IntegerField()

class AdminApproveRequestForm(forms.Form):
    mechanic=forms.ModelChoiceField(queryset=models.Mechanic.objects.all(),empty_label="Mechanic Name",to_field_name='id')

    stat=(('Pending','Pending'),('Approved','Approved'),('Released','Released'))
    status=forms.ChoiceField( choices=stat)


class UpdateCostForm(forms.Form):
    cost=forms.IntegerField()

class MechanicUpdateStatusForm(forms.Form):
    stat=(('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'))
    status=forms.ChoiceField( choices=stat)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['by','message']
        
        widgets = {
        'message':forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }

#for Attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()
class AskDateForm(forms.Form):
    date = forms.DateField()
       


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

# category
class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            # 'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Category Description'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        categories_count = Category.objects.count()

        # Check if the maximum number of entries (4) has been reached
        if categories_count >= 4:
            raise forms.ValidationError('You cannot add  categories no more.')

        return cleaned_data
#subcategory
class SubcategoryForm(forms.ModelForm):
    # Add a category field to select the associated category
    category = forms.ModelChoiceField(queryset=None, empty_label="Select a Category", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Subcategory
        fields = ['name', 'category']  # Include the 'category' field in the form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subcategory Name'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the queryset for the category field to display existing categories
        self.fields['category'].queryset = Category.objects.all()
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        category = cleaned_data.get('category')

        # Check if a subcategory with the same name and category already exists
        if Subcategory.objects.filter(name=name, category=category).exists():
            raise forms.ValidationError('.........A subcategory with the same name and category already exists.')

        # Check if the maximum number of entries (e.g., 5) has been reached
        if Subcategory.objects.count() >= 11:
            raise forms.ValidationError('.........You cannot add subcategories.')

        return cleaned_data

#subsubcategory
class SubSubcategoryForm(forms.ModelForm):
    # Add fields for image, description, price, and hours taken
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    # description_1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description 1'}))
    # price_1 = forms.DecimalField(required=False, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price 1'}))
    # description_2= forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description 2'}))
    # price_2 = forms.DecimalField(required=False, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price 2'}))
    # description_3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description 3'}))
    # price_3 = forms.DecimalField(required=False, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price 3'}))
    # description_4 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description 4'}))
    # price_4 = forms.DecimalField(required=False, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price 4'}))
    # description_5 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description 5'}))
    # price_5 = forms.DecimalField(required=False, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price 5'}))
    price = forms.DecimalField(required=False, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}))
    hours_taken = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hours Taken'}))

    class Meta:
        model = SubSubcategory
        fields = ['name', 'subcategory', 'image',  'price','hours_taken']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SubSubcategory Name'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        subcategory = cleaned_data.get('subcategory')

        # Check if a subsubcategory with the same name and subcategory already exists
        if SubSubcategory.objects.filter(name=name, subcategory=subcategory).exists():
            raise forms.ValidationError('A subsubcategory with the same name and subcategory already exists.')

        # Check if the maximum number of entries (e.g., 5) has been reached
        if SubSubcategory.objects.count() >= 5:
            raise forms.ValidationError('You cannot add more than 5 subsubcategories.')

        return cleaned_data


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Car Model Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        image = cleaned_data.get('image')

        # Check if a car model with the same name already exists
        if CarModel.objects.filter(name=name).exists():
            raise forms.ValidationError('A car model with the same name already exists.')

        # Check if the maximum number of entries (e.g., 5) has been reached
        if CarModel.objects.count() >= 5:
            raise forms.ValidationError('You cannot add car models.')

        # Check if the uploaded file is an image


        return cleaned_data
class CarNameForm(forms.ModelForm):
    class Meta:
        model = CarName
        fields = ['name', 'car_model']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the car_model field queryset to show only car models.
        self.fields['car_model'].queryset = CarModel.objects.all()

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        car_model = cleaned_data.get('car_model')

        # Check if a car name with the same name and car model already exists
        if CarName.objects.filter(name=name, car_model=car_model).exists():
            raise forms.ValidationError('A car name with the same name and car model already exists.')

        # Check if the maximum number of entries (e.g., 5) has been reached
        if CarName.objects.count() >= 5:
            raise forms.ValidationError('You cannot add  car names.')

        return cleaned_data


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name', 'image']
    def clean(self):
        cleaned_data = super().clean()

        # Check the number of existing entries
        existing_entries_count = Type.objects.count()

        # Set a maximum allowed number of entries
        max_entries_allowed = 3  # Change this value to your desired limit

        if existing_entries_count >= max_entries_allowed:
            raise forms.ValidationError(
                f"Cannot add more entries. Maximum allowed entries is {max_entries_allowed}."
            )

        return cleaned_data



    def clean_image(self):
        image = self.cleaned_data.get('image')

        # Add your validation rules for the image field
        # For example, you can check file type, size, etc.
        if image:
            # Check if the file is an image
            if not image.content_type.startswith('image'):
                raise forms.ValidationError("Uploaded file is not an image.")

            # Check file size
            if image.size > 5 * 1024 * 1024:  # 5 MB
                raise forms.ValidationError("Image file size should not exceed 5 MB.")


# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['appointment_date', 'name', 'address', 'Alternative_mobile']
#         widgets = {
#         'appointment_date': forms.DateInput(attrs={'type': 'date'}),'address': forms.Textarea(attrs={'rows': 3, 'cols': 30}),}
#     def clean_appointment_date(self):
#         appointment_date = self.cleaned_data.get('appointment_date')
#         if appointment_date:
#             # Get the current date
#             current_date = timezone.now().date()

#             # Check if the appointment date is in the future and within the current year
#             if appointment_date < current_date:
#                 raise ValidationError('Appointment date must be the current year and tomorrow or later.')

#         return appointment_date



# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['appointment_date', 'name', 'address', 'Alternative_mobile']
#         widgets = {
#             'appointment_date': forms.DateInput(attrs={
#                 'type': 'date',
#                 'min': (timezone.now() + timezone.timedelta(days=1)).strftime('%Y-%m-%d'),  # Set min date to next day
#                 'max': (timezone.now().replace(month=12, day=31)).strftime('%Y-%m-%d'),  # Set max date to the end of the current year
#             }),
            
#         }
            
from django.core.exceptions import ValidationError
class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ['appointment_date', 'name', 'address','pincode', 'Alternative_mobile','payment_method','pickup_service']
        widgets = {
            'appointment_date': forms.DateInput(attrs={
                'type': 'date',
                'min': (timezone.now() + timezone.timedelta(days=1)).strftime('%Y-%m-%d'),  # Set min date to next day
                'max': (timezone.now().replace(month=12, day=31)).strftime('%Y-%m-%d'),  # Set max date to the end of the current year
                'class': 'form-control',  # Add Bootstrap class for styling
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',  # Add Bootstrap class for styling
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                  'placeholder': 'Enter please valid address  ',  # Add Bootstrap class for styling
                'rows': 3,
                'cols': 30,
            }),
            'pincode': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a 6-digit pincode',  # Placeholder text
                'pattern': '6[0-9]{5}',  # Pattern for 6-digit pincode starting with 6
            }),
            'Alternative_mobile': forms.TextInput(attrs={
                'class': 'form-control',  # Add Bootstrap class for styling
                'placeholder': 'Enter 10-digit phone number',  # Placeholder text
                'pattern': '[0-9]{10}',  # Pattern for 10-digit phone number
            }),
    
        } 
        payment_method = forms.ChoiceField(
        choices=Booking.PAYMENT_CHOICES,  # Provide the choices from your model
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),  # Render as a dropdown
    )
        pickup_service = forms.ChoiceField(
        choices=Booking.PICKUP_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )
    def clean_appointment_date(self):
        appointment_date = self.cleaned_data.get('appointment_date')
        
        # Check if there are already three appointments for the selected date
        existing_appointments_count = Booking.objects.filter(appointment_date=appointment_date).count()

        if existing_appointments_count >= 3:
            raise ValidationError('Maximum appointments reached for this date.! please select another date')

        if appointment_date:
            if appointment_date.weekday() == 6:  # Sunday is weekday 6
                raise ValidationError("Sundays are not allowed for appointments!  please select another date")
        
        return appointment_date
    
    def clean_address(self):
        address = self.cleaned_data.get('address')

        # Your custom validation logic for the address field
        if not address:
            raise ValidationError("Address field is required")

        return address

    def clean_Alternative_mobile(self):
        mobile_number = self.cleaned_data.get('Alternative_mobile')

        # Your custom validation logic for the mobile number field
        if not mobile_number:
            raise ValidationError("Mobile number is required")

        return mobile_number
    def clean_pincode(self):
        pincode = self.cleaned_data.get('pincode')
        allowed_pincodes = ['686505', '686502', '686503','686506']  # Example list of allowed pincodes

        if pincode not in allowed_pincodes:
            self.cleaned_data['pickup_service'] = 'No'  # Set pickup service to 'No'
            raise ValidationError('Sorry, pickup service is not available for this pincode.')

        # If the pincode matches, set pickup service to 'Yes'
        self.cleaned_data['pickup_service'] = 'Yes'
        return pincode


