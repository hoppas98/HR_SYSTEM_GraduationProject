from django.urls import path
from Apps import views


urlpatterns = [
    path('', views.home, name='index'),
    path('find_a_job', views.find_a_job, name='find_a_job'),
    path('cv_form', views.new_cv, name='new_cv'),
    path('waiting_quiz', views.waiting_quiz, name='waiting_quiz'),
    path('homepage_company', views.company_side, name='homepage_company'),
    path('result_employees', views.getRequestedEmployees, name='result_employees'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('chatbot_quiz', views.chatbot_quiz, name='chatbot_quiz'),
    path('add_job', views.add_job, name='add_job'),
    path('jobs', views.show_jobs, name='jobs'),
    path('about_us', views.about_us, name='about_us'),
    path('mission_and_vision', views.mission_and_vision, name='mission_and_vision'),
]
