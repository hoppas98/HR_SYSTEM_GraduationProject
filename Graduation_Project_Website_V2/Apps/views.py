from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pymongo import MongoClient

from Apps.models import ApplicantCV
from Apps.models import ContactUs
from Apps.models import PostsJobs

client = MongoClient(
    "mongodb+srv://hoppas98:hoppas98@cluster0.rr4of.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority")
db = client.get_database('HR_SYSTEM')
records = db.quiz_results


# Create your views here.
def home(request):
    return render(request, 'screens/homepage_assets/home.html')


def find_a_job(request):
    return render(request, 'screens/applicant_side/find_a_job.html')


def about_us(request):
    return render(request, 'screens/website_assets/about_us.html')


def mission_and_vision(request):
    return render(request, 'screens/website_assets/mission_and_vision.html')


@login_required
def waiting_quiz(request):
    return render(request, 'screens/applicant_side/waiting_quiz.html')


def show_jobs(request):
    showjobs = PostsJobs.objects.all()
    return render(request, 'screens/applicant_side/jobs_list.html', {'Jobs': showjobs})


@login_required
def add_job(request):
    if request.method == 'POST':
        email = request.POST['email']
        companyname = request.POST['companyname']
        jobtitle = request.POST['jobtitle']
        description = request.POST['description']
        post = PostsJobs.objects.create(
            Email=email,
            Company_Name=companyname,
            Job_Title=jobtitle,
            Description=description,
        )
        return redirect('index')
    return render(request, 'screens/company_side/add_job.html')


# def company_side(request):
#     return render(request, 'screens/homepage_assets/homepage_company.html')


def chatbot_quiz(request):
    return render(request, 'screens/applicant_side/chatbot_quiz.html')


def contact_us(request):
    if request.method == 'POST':
        email = request.POST['email']
        fullname = request.POST['fullname']
        message = request.POST['message']
        cv = ContactUs.objects.create(
            Email=email,
            Name=fullname,
            Message=message,
        )
        return redirect('index')
    return render(request, 'screens/website_assets/contact_us.html')


@login_required
def new_cv(request):
    if request.method == 'POST':
        email = request.POST['email']
        fullname = request.POST['fullname']
        street = request.POST['street_address']
        city = request.POST['city']
        country = request.POST['country']
        phone = request.POST['phone']

        job_title = request.POST['job_title']
        company = request.POST['company_work']
        city_town_work = request.POST['city_town_work']
        country_work = request.POST['country_work']
        start_date_work = request.POST['start_date_work']
        end_date_work = request.POST['end_date_work']

        school_name = request.POST['school_name']
        city_town_school = request.POST['city_town_school']
        country_school = request.POST['country_school']
        degree = request.POST['degree']
        graduation_year = request.POST['graduation_year']
        university_name = request.POST['university_name']

        skills_1 = request.POST['skills_1']
        skills_2 = request.POST['skills_2']
        skills_3 = request.POST['skills_3']
        skills_4 = request.POST['skills_4']
        skills_5 = request.POST['skills_5']
        skills_6 = request.POST['skills_6']
        skills_7 = request.POST['skills_7']
        skills_8 = request.POST['skills_8']
        skills_9 = request.POST['skills_9']
        pdf_cv = request.POST['pdf_cv']

        # user = User.objects.first()

        cv = ApplicantCV.objects.create(
            Email=email,
            Name=fullname,
            Street=street,
            City=city,
            Country=country,
            Phone=phone,

            Job_Title=job_title,
            Company=company,
            City_Town_Work=city_town_work,
            Country_Work=country_work,
            Start_Date_Work=start_date_work,
            End_Date_Work=end_date_work,

            School_Name=school_name,
            City_Town_School=city_town_school,
            Country_School=country_school,
            Degree=degree,
            Graduation_Date=graduation_year,
            University_Name=university_name,

            Skills_1=skills_1,
            Skills_2=skills_2,
            Skills_3=skills_3,
            Skills_4=skills_4,
            Skills_5=skills_5,
            Skills_6=skills_6,
            Skills_7=skills_7,
            Skills_8=skills_8,
            Skills_9=skills_9,
            pdf_cv=pdf_cv,
        )
        return redirect('/waiting_quiz')

    return render(request, 'screens/applicant_side/cv_form.html')


def view_applicant_report(request, user_email):
    Applicants = ApplicantCV.objects.all()
    interview_results = list(records.find())
    applicants_with_skills = []

    for x in range(len(interview_results)):
        if user_email == interview_results[x]['User_Email']:
            applicant_teamwork_skill_grade = 0
            if interview_results[x]['TeamWorker_A1'] == 'True':
                applicant_teamwork_skill_grade += 1
            if interview_results[x]['TeamWorker_A2'] == 'True':
                applicant_teamwork_skill_grade += 1
            if interview_results[x]['TeamWorker_A3'] == 'True':
                applicant_teamwork_skill_grade += 2

            applicants_with_skills.insert(x, (
                {'User_Email': interview_results[x]['User_Email'],
                 'TeamWorker_Q1': interview_results[x]['TeamWorker_Q1'],
                 'TeamWorker_Q2': interview_results[x]['TeamWorker_Q2'],
                 'TeamWorker_Q3': interview_results[x]['TeamWorker_Q3'],
                 'TeamWorker_A1': interview_results[x]['TeamWorker_A1'],
                 'TeamWorker_A2': interview_results[x]['TeamWorker_A2'],
                 'TeamWorker_A3': interview_results[x]['TeamWorker_A3'],
                 'TeamWorker_Grade': applicant_teamwork_skill_grade}))
    return render(request, 'screens/company_side/view_report.html',
                  {'Applicants': Applicants, 'user_email': user_email, 'applicant_report': applicants_with_skills})


@login_required
def getRequestedEmployees(request):
    # Retrieve data of interview and data of applicants
    all_applicants = ApplicantCV.objects.all()
    interview_results = list(records.find())

    applicants_with_skills = [[]]
    for x in range(len(interview_results)):
        applicant_teamwork_skill_grade = 0
        if interview_results[x]['TeamWorker_A1'] == 'True':
            applicant_teamwork_skill_grade += 1
        if interview_results[x]['TeamWorker_A2'] == 'True':
            applicant_teamwork_skill_grade += 1
        if interview_results[x]['TeamWorker_A3'] == 'True':
            applicant_teamwork_skill_grade += 2

        applicants_with_skills.insert(x, (
            [interview_results[x]['User_Email'], interview_results[x]['TeamWorker_Q1'],
             interview_results[x]['TeamWorker_Q2'],
             interview_results[x]['TeamWorker_Q3'], interview_results[x]['TeamWorker_A1'],
             interview_results[x]['TeamWorker_A2'],
             interview_results[x]['TeamWorker_A3'], applicant_teamwork_skill_grade]))
    return render(request, 'screens/company_side/results_employees.html',
                  {'Applicants': all_applicants, 'Interview_Results': interview_results,
                   'Grades': applicants_with_skills})
