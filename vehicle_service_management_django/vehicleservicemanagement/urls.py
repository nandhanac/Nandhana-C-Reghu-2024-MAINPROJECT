"""
vehicle
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from vehicle import views
from django.contrib.auth.views import LoginView,LogoutView
from vehicle.views import ResetPasswordView, ChangePasswordView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from vehicle.views import map_view

urlpatterns = [
    path('admin/', admin.site.urls),
path('', include('vehicle.urls')),
    path('',views.home_view,name='home'),
path('service_one',views.service_one,name='service_one'),
path('service_two/<int:category_id>/', views.service_two, name='service_two'),
path('service_three', views.service_three, name='service_three'),
path('service_four', views.service_four, name='service_four'),

path('car-models/', views.car_models, name='car-models'),
path('selectcar/<int:subsubcategory_id>/', views.selectcar, name='selectcar'),
path('create_car_name/', views.create_car_name, name='create_car_name'),
path('delete-car-name/<int:car_name_id>/', views.delete_car_name, name='delete_car_name'),
path('types/', views.types, name='types'),

 path('book/<int:subsubcategory_id>/', views.book_service, name='book_service'),
path('confirmation/<int:payment_amount>/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),

 path('bookconfirm_cash/<int:booking_id>/', views.bookconfirm_cash, name='bookconfirm_cash'),  
   
   
   
    path('adminclick', views.adminclick_view),
    path('customerclick', views.customerclick_view),
    path('mechanicsclick', views.mechanicsclick_view),

     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Password/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='Password/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

 re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('mechanicsignup', views.mechanic_signup_view,name='mechanicsignup'),

    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('payment_confirmation', views.payment_confirmation, name='payment_confirmation'),

path('invoice/<int:booking_id>/', views.invoice, name='invoice'),
path('generate_invoice_pdf/<int:booking_id>/', views.generate_invoice_pdf, name='generate_invoice_pdf'),


    path('customerlogin', LoginView.as_view(template_name='vehicle/customerlogin.html'),name='customerlogin'),
    path('mechaniclogin', LoginView.as_view(template_name='vehicle/mechaniclogin.html'),name='mechaniclogin'),
    path('adminlogin', LoginView.as_view(template_name='vehicle/adminlogin.html'),name='adminlogin'),

 path('admin-service', views.admin_service_view,name='admin-service'),
path('admin-category', views.admin_category_view,name='admin-category'),
path('update-category/<int:category_id>/', views.update_category, name='update-category'),
path('delete-category/<int:category_id>/', views.delete_category, name='delete-category'),
path('admin_subcategory_view', views.admin_subcategory_view, name='admin_subcategory_view'),
path('update_subcategory/<int:subcategory_id>/', views.update_subcategory, name='update-subcategory'),
path('delete_subcategory/<int:subcategory_id>/', views.delete_subcategory, name='delete-subcategory'),
path('admin_subsubcategory_view', views.admin_subsubcategory_view, name='admin_subsubcategory_view'),
 path('update-subsubcategory/<int:subsubcategory_id>/', views.update_subsubcategory_view, name='update-subsubcategory'),
path('delete-subsubcategory/<int:subsubcategory_id>/', views.delete_subsubcategory_view, name='delete-subsubcategory'),



    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-customer', views.admin_customer_view,name='admin-customer'),
    path('admin-view-customer',views.admin_view_customer_view,name='admin-view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('admin-add-customer', views.admin_add_customer_view,name='admin-add-customer'),
    path('admin-view-customer-enquiry', views.admin_view_customer_enquiry_view,name='admin-view-customer-enquiry'),
    path('admin-view-customer-invoice', views.admin_view_customer_invoice_view,name='admin-view-customer-invoice'),


    path('admin-request', views.admin_request_view,name='admin-request'),
    path('admin-view-request',views.admin_view_request_view,name='admin-view-request'),
    path('change-status/<int:pk>', views.change_status_view,name='change-status'),
    path('admin-delete-request/<int:pk>', views.admin_delete_request_view,name='admin-delete-request'),
    path('admin-add-request',views.admin_add_request_view,name='admin-add-request'),
    path('admin-approve-request',views.admin_approve_request_view,name='admin-approve-request'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    
    path('admin-view-service-cost',views.admin_view_service_cost_view,name='admin-view-service-cost'),
    path('update-cost/<int:pk>', views.update_cost_view,name='update-cost'),

    path('admin-mechanic', views.admin_mechanic_view,name='admin-mechanic'),
    path('admin-view-mechanic',views.admin_view_mechanic_view,name='admin-view-mechanic'),
    path('delete-mechanic/<int:pk>', views.delete_mechanic_view,name='delete-mechanic'),
    path('update-mechanic/<int:pk>', views.update_mechanic_view,name='update-mechanic'),
    path('admin-add-mechanic',views.admin_add_mechanic_view,name='admin-add-mechanic'),
    path('admin-approve-mechanic',views.admin_approve_mechanic_view,name='admin-approve-mechanic'),
    path('approve-mechanic/<int:pk>', views.approve_mechanic_view,name='approve-mechanic'),
    path('delete-mechanic/<int:pk>', views.delete_mechanic_view,name='delete-mechanic'),
    path('admin-view-mechanic-salary',views.admin_view_mechanic_salary_view,name='admin-view-mechanic-salary'),
    path('update-salary/<int:pk>', views.update_salary_view,name='update-salary'),

    path('admin-mechanic-attendance', views.admin_mechanic_attendance_view,name='admin-mechanic-attendance'),
    path('admin-take-attendance', views.admin_take_attendance_view,name='admin-take-attendance'),
    path('admin-view-attendance', views.admin_view_attendance_view,name='admin-view-attendance'),
    path('admin-feedback', views.admin_feedback_view,name='admin-feedback'),

    path('admin-report', views.admin_report_view,name='admin-report'),

    path('mechanic-dashboard', views.mechanic_dashboard_view,name='mechanic-dashboard'),
    path('mechanic-work-assigned', views.mechanic_work_assigned_view,name='mechanic-work-assigned'),
    path('mechanic-update-status/<int:pk>', views.mechanic_update_status_view,name='mechanic-update-status'),
    path('mechanic-feedback', views.mechanic_feedback_view,name='mechanic-feedback'),
    path('mechanic-salary', views.mechanic_salary_view,name='mechanic-salary'),
    path('mechanic-profile', views.mechanic_profile_view,name='mechanic-profile'),
    path('edit-mechanic-profile', views.edit_mechanic_profile_view,name='edit-mechanic-profile'),

    path('mechanic-attendance', views.mechanic_attendance_view,name='mechanic-attendance'),



    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('customer-request', views.customer_request_view,name='customer-request'),
    path('customer-add-request',views.customer_add_request_view,name='customer-add-request'),

    path('customer-profile', views.customer_profile_view,name='customer-profile'),
    path('edit-customer-profile', views.edit_customer_profile_view,name='edit-customer-profile'),
    path('customer-feedback', views.customer_feedback_view,name='customer-feedback'),
    path('customer-invoice', views.customer_invoice_view,name='customer-invoice'),
    path('customer-view-request',views.customer_view_request_view,name='customer-view-request'),
    path('customer-delete-request/<int:pk>', views.customer_delete_request_view,name='customer-delete-request'),
    path('customer-view-approved-request',views.customer_view_approved_request_view,name='customer-view-approved-request'),
    path('customer-view-approved-request-invoice',views.customer_view_approved_request_invoice_view,name='customer-view-approved-request-invoice'),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='vehicle/index.html'),name='logout'),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),

    path('driver-dashboard/', views.driver_dashboard, name='driver-dashboard'),
    path('assigned-bookings/', views.assigned_bookings_view, name='assigned-bookings'),
    path('assign-driver/<int:booking_id>/', views.assign_driver_view, name='assign-driver'),
    path('send_email_to_driver/<int:booking_id>/', views.assign_driver_view, name='send_email_to_driver'),
    path('map/<int:booking_id>/', map_view, name='map_view'),

    path('admin-blogs', views.admin_blogs_view,name='admin-blogs'),
    path('blogs', views.blog_submission, name='blog_submission'),
    path('approve-blog/<int:blog_id>/', views.approve_blog, name='approve_blog'),
    path('reject_blog/<int:blog_id>/', views.reject_blog, name='reject_blog'),
    path('admin-blog-approval', views.admin_blog_approval, name='admin_blog_approval'),
    path('approved-blogs/', views.approved_blogs, name='approved_blogs'),
    path('like/<int:blog_id>/', views.like_blog, name='like_blog'),
     path('add-item/', views.add_item_price, name='add_item_price'),
    path('update-item/<int:item_id>/', views.update_item_price, name='update-item_price'),
    path('delete-item/<int:item_id>/', views.delete_item_price, name='delete-item_price'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

