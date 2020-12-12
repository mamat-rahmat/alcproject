from django.urls import path, include
from django.conf.urls.static import static
from alcproject import settings
from .forms import UserProfileRegistrationForm
from .views import (
    index,
    ProgramListView,
    MyProgramListView,
    SpecialProgramListView,
    ProgramDetailView,
    exam_detail,
    UserProfileRegistrationView,
    edit_profile,
    topic_list,
    topic_detail,
    topic_create
)


urlpatterns = [
    path('accounts/register/', UserProfileRegistrationView.as_view(), name='registration_register'),
    path('accounts/edit', edit_profile, name='edit-profile'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', index, name='index'),
    path('program', ProgramListView.as_view(), name='program-list'),
    path('myprogram', MyProgramListView.as_view(), name='my-program-list'),
    path('sprogram', SpecialProgramListView.as_view(), name='special-program-list'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program-detail'),
    path('program/<int:pk_program>/exam/<int:pk_exam>', exam_detail, name='exam-detail'),
    path('program/<int:pk_program>/topic', topic_list, name='topic-list'),
    path('program/<int:pk_program>/topic/<int:pk_topic>', topic_detail, name='topic-detail'),   
    path('program/<int:pk_program>/topic/create', topic_create, name='topic-create'),   
]
