from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("query/places/<str:q>", views.query, name="query"),
    path("flight", views.flight, name="flight"),
    path("review", views.review, name="review"),
    path("flight/ticket/book", views.book, name="book"),
    path("flight/ticket/payment", views.payment, name="payment"),
    path('flight/ticket/api/<str:ref>', views.ticket_data, name="ticketdata"),
    path('flight/ticket/print',views.get_ticket, name="getticket"),
    path('flight/bookings', views.bookings, name="bookings"),
    path('flight/ticket/cancel', views.cancel_ticket, name="cancelticket"),
    path('flight/ticket/resume', views.resume_booking, name="resumebooking"),
    path('contact', views.contact, name="contact"),
    path('privacy-policy', views.privacy_policy, name="privacypolicy"),
    path('terms-and-conditions', views.terms_and_conditions, name="termsandconditions"),
    path('about-us', views.about_us, name="aboutus"),
    path('valid', views.fvalid, name="fvalid"),
    path("login", views.login_view, name="login"),
    #from nazmul sir#
    path('admindash/', views.admindash, name='admindash'),

    path('error/', views.error, name='error'),
    path('charts/', views.charts, name='charts'),
    path('piechart/', views.piechart, name='piechart'),
    # path('bar-chart/', views.bar_chart, name='bar-chart'),
    # path('showchart/', views.showchart, name='showbarchart'),
    # path('group_by_dept/', views.group_by_dept, name='group_by_dept'),
]