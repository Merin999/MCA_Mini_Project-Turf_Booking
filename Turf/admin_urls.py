from django.urls import path

from Turf.admin_views import IndexView, ManageOwner, ApproveOwner, ViewOwner, ApproveView, RejectView, ApproveUser, \
    ManageUser, ViewUser,  ManageTurf, \
    NewTurf, DisApproveTurf, ApproveTurf, ViewTurf, ViewFeedback, ViewRate, ViewTurfFeedback
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', IndexView.as_view()),
    path('ManageOwner', ManageOwner.as_view()),
    path('ApproveView', ApproveView.as_view()),
    path('RejectView', RejectView.as_view()),
    path('ApproveOwner', ApproveOwner.as_view()),
    path('ViewOwner', ViewOwner.as_view()),
    path('ManageUser', ManageUser.as_view()),
    path('ApproveUser', ApproveUser.as_view()),
    path('ViewUser', ViewUser.as_view()),

    path('ManageTurf', ManageTurf.as_view()),

    path('NewTurf', NewTurf.as_view()),
    path('ViewTurf', ViewTurf.as_view()),
    path('ApproveTurf', ApproveTurf.as_view()),
    path('DisApproveTurf', DisApproveTurf.as_view()),
    path('ViewFeedback', ViewFeedback.as_view()),
    path('ViewRate', ViewRate.as_view()),
    path('ViewTurfFeedback', ViewTurfFeedback.as_view()),



    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
    ),
        name='logout'
    ),


]


def urls():
    return urlpatterns, 'admin', 'admin'
