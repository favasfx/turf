from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin_login', views.login,name= 'login'),

    path('booking', views.booking,name= 'booking'),

    path('dashboard', views.dashboard,name= 'dashboard'),

    path('feedbacks', views.feedbacks,name= 'feedbacks'),

    path('messages', views.messages,name= 'messages'),

    path('pending_bookings', views.pending_bookings,name= 'pending_bookings'),

    path('service_history', views.service_history,name= 'service_history'),

    path('total_booking', views.total_booking,name= 'total_booking'),

    path('completed_booking', views.completed_booking,name= 'completed_booking'),

    path('edit_Bookings',views.edit_bookings,name='edit_bookings'),

    path('cancel_feedback/<int:id>',views.cancelFeedback,name='cancel_feedback'),

    path('cancel_booking/<int:id>',views.cancelBooking,name='cancel_booking')


]