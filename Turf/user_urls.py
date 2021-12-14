from django.urls import path

from Turf.user_views import IndexView, AddFeedback, TurfDetails, ViewTurf, ViewTurfBooking, CancelBooking, BookTurfs, ViewProfile, AddRate, AddTurfFeedback, ViewTurfFeedback,PaymentView
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', IndexView.as_view()),

    path('AddFeedback', AddFeedback.as_view()),
    path('AddTurfFeedback', AddTurfFeedback.as_view()),
    path('ViewTurfFeedback', ViewTurfFeedback.as_view()),

    path('ViewTurf', ViewTurf.as_view()),
    path('TurfDetails', TurfDetails.as_view()),
    path('BookTurf', BookTurfs.as_view()),
    path('ViewTurfBooking', ViewTurfBooking.as_view()),
    path('CancelBooking', CancelBooking.as_view()),
    path('ViewProfile', ViewProfile.as_view()),
    path('AddRate', AddRate.as_view()),
    path('PaymentView', PaymentView.as_view()),





    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
    ),
        name='logout'
    ),


]


def urls():
    return urlpatterns, 'user', 'user'
