from django.contrib.auth.decorators import login_required
# karim
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from pymongo import MongoClient

from Apps.models import ApplicantCV
from Apps.models import ContactUs
from Apps.models import NewsletterSubscriptions
from Apps.models import PostsJobs

client = MongoClient(
    "mongodb+srv://hoppas98:hoppas98@cluster0.rr4of.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority")
db = client.get_database('HR_SYSTEM')
records = db.quiz_results
email_check_cv = db.Apps_applicantcv
email_check_newspaper = db.Apps_newslettersubscriptions


# Create your views here.
def home(request):
    emails = list(email_check_newspaper.find())
    if request.method == 'POST':

        found = False
        email = request.POST['email']
        for x in range(len(emails)):
            if emails[x]['Email'] == email:
                found = False
        if found == True:
            subscription = NewsletterSubscriptions.objects.create(
                Email=email,
            )
        return redirect('index')
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
        template = render_to_string('screens/applicant_side/email_template.html')
        send_mail('HRChatbotSystem', template, 'hrchatbotsystem@gmail.com', [request.user.email], fail_silently=True)
        return redirect('index')
    return render(request, 'screens/website_assets/contact_us.html')


@login_required
def new_cv(request):
    applicants_cvs = list(email_check_cv.find())
    print(len(applicants_cvs))
    found = False
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

        # Find if it's already exist
        for x in range(len(applicants_cvs)):
            if applicants_cvs[x]['Email'] == email:
                found = True
        if found == False:
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
    return render(request, 'screens/applicant_side/cv_form.html')


@login_required
def get_requested_employees(request):
    # Retrieve all applicants and their results
    all_applicants = ApplicantCV.objects.all()
    interview_results = list(records.find())

    applicants_with_skills = []
    decision_making_q1 = [0, 25, 50, 75, 100]
    decision_making_q2 = [0, 25, 50, 75, 100]
    decision_making_q3 = [0, 25, 50, 75, 100]
    decision_making_q4 = [0, 25, 50, 75, 100]
    decision_making_q5 = [0, 25, 50, 75, 100]
    decision_making_q6 = [0, 25, 50, 75, 100]
    decision_making_q7 = [0, 25, 50, 75, 100]

    behavioral_skill_q1 = [0, 25, 50, 75, 100]
    behavioral_skill_q2 = [0, 25, 50, 75, 100]
    behavioral_skill_q3 = [0, 25, 50, 75, 100]
    behavioral_skill_q4 = [0, 25, 50, 75, 100]
    behavioral_skill_q5 = [0, 25, 50, 75, 100]

    Communication_skill_q1 = [0, 25, 50, 75, 100]
    Communication_skill_q2 = [0, 25, 50, 75, 100]
    Communication_skill_q3 = [0, 25, 50, 75, 100]
    Communication_skill_q4 = [0, 25, 50, 75, 100]
    Communication_skill_q5 = [0, 25, 50, 75, 100]

    for x in range(len(interview_results)):
        # Decision Making Skill
        float
        decision_making_score = 25

        # Team Work Skill
        float
        team_worker_score = 25

        # Behavioral Skill
        float
        behavioral_skill_score = 25

        # Communication Skill
        float
        communication_skill_score = 25

        # Total Rate
        float
        total_rate = 1800

        float
        rate = 25

        decision_making_score = ((decision_making_q1[int(interview_results[x]['DM_A1'])] +
                                  decision_making_q2[int(interview_results[x]['DM_A2'])] +
                                  decision_making_q3[int(interview_results[x]['DM_A3'])] +
                                  decision_making_q4[int(interview_results[x]['DM_A4'])] +
                                  decision_making_q5[int(interview_results[x]['DM_A5'])] +
                                  decision_making_q6[int(interview_results[x]['DM_A6'])] +
                                  decision_making_q7[int(interview_results[x]['DM_A7'])]) * 100) / 700
        behavioral_skill_score = ((behavioral_skill_q1[int(interview_results[x]['BS_A1'])] +
                                   behavioral_skill_q2[int(interview_results[x]['BS_A2'])] +
                                   behavioral_skill_q3[int(interview_results[x]['BS_A3'])] +
                                   behavioral_skill_q4[int(interview_results[x]['BS_A4'])] +
                                   behavioral_skill_q5[int(interview_results[x]['BS_A5'])]) * 100) / 500
        communication_skill_score = ((Communication_skill_q1[int(interview_results[x]['CS_A1'])] +
                                      Communication_skill_q2[int(interview_results[x]['CS_A2'])] +
                                      Communication_skill_q3[int(interview_results[x]['CS_A3'])] +
                                      Communication_skill_q4[int(interview_results[x]['CS_A4'])] +
                                      Communication_skill_q5[int(interview_results[x]['CS_A5'])]) * 100) / 500

        decision_making_score = round(decision_making_score, 2)
        behavioral_skill_score = round(behavioral_skill_score, 2)
        team_worker_score = round(team_worker_score, 2)
        communication_skill_score = round(communication_skill_score, 2)

        total_rate = (
                             decision_making_score + behavioral_skill_score + team_worker_score + communication_skill_score) * 100 / total_rate

        scores = {'DecisionMaking': decision_making_score, 'TeamWorker': team_worker_score,
                  'BehavioralSkill': behavioral_skill_score, 'CommunicationSkill': communication_skill_score}

        applicants_with_skills.insert(x, (
            [interview_results[x]['User_Email'], scores]))

    return render(request, 'screens/company_side/results_employees.html',
                  {'Applicants': all_applicants, 'Interview_Results': interview_results,
                   'applicants_with_skills': applicants_with_skills})


def view_applicant_report(request, user_email):
    # Retrieve all applicants and their results
    all_applicants = ApplicantCV.objects.all()
    interview_results = list(records.find())

    applicants_with_skills = []
    decision_making_q1 = [0, 25, 50, 75, 100]
    decision_making_q2 = [0, 25, 50, 75, 100]
    decision_making_q3 = [0, 25, 50, 75, 100]
    decision_making_q4 = [0, 25, 50, 75, 100]
    decision_making_q5 = [0, 25, 50, 75, 100]
    decision_making_q6 = [0, 25, 50, 75, 100]
    decision_making_q7 = [0, 25, 50, 75, 100]

    behavioral_skill_q1 = [0, 25, 50, 75, 100]
    behavioral_skill_q2 = [0, 25, 50, 75, 100]
    behavioral_skill_q3 = [0, 25, 50, 75, 100]
    behavioral_skill_q4 = [0, 25, 50, 75, 100]
    behavioral_skill_q5 = [0, 25, 50, 75, 100]

    Communication_skill_q1 = [0, 25, 50, 75, 100]
    Communication_skill_q2 = [0, 25, 50, 75, 100]
    Communication_skill_q3 = [0, 25, 50, 75, 100]
    Communication_skill_q4 = [0, 25, 50, 75, 100]
    Communication_skill_q5 = [0, 25, 50, 75, 100]

    for x in range(len(interview_results)):
        # Decision Making Skill
        float
        decision_making_score = 25

        # Team Work Skill
        float
        team_worker_score = 25

        # Behavioral Skill
        float
        behavioral_skill_score = 25

        # Communication Skill
        float
        communication_skill_score = 25

        # Total Rate
        float
        total_rate = 1800

        float
        rate = 25

        decision_making_score = ((decision_making_q1[int(interview_results[x]['DM_A1'])] +
                                  decision_making_q2[int(interview_results[x]['DM_A2'])] +
                                  decision_making_q3[int(interview_results[x]['DM_A3'])] +
                                  decision_making_q4[int(interview_results[x]['DM_A4'])] +
                                  decision_making_q5[int(interview_results[x]['DM_A5'])] +
                                  decision_making_q6[int(interview_results[x]['DM_A6'])] +
                                  decision_making_q7[int(interview_results[x]['DM_A7'])]) * 100) / 700
        behavioral_skill_score = ((behavioral_skill_q1[int(interview_results[x]['BS_A1'])] +
                                   behavioral_skill_q2[int(interview_results[x]['BS_A2'])] +
                                   behavioral_skill_q3[int(interview_results[x]['BS_A3'])] +
                                   behavioral_skill_q4[int(interview_results[x]['BS_A4'])] +
                                   behavioral_skill_q5[int(interview_results[x]['BS_A5'])]) * 100) / 500
        communication_skill_score = ((Communication_skill_q1[int(interview_results[x]['CS_A1'])] +
                                      Communication_skill_q2[int(interview_results[x]['CS_A2'])] +
                                      Communication_skill_q3[int(interview_results[x]['CS_A3'])] +
                                      Communication_skill_q4[int(interview_results[x]['CS_A4'])] +
                                      Communication_skill_q5[int(interview_results[x]['CS_A5'])]) * 100) / 500
        rate = ((
                        decision_making_score + behavioral_skill_score + team_worker_score + communication_skill_score) * 5) / 400
        decision_making_score = round(decision_making_score, 2)
        behavioral_skill_score = round(behavioral_skill_score, 2)
        team_worker_score = round(team_worker_score, 2)
        print(rate)
        rate = round(rate, 1)
        scores = {'DecisionMaking': decision_making_score, 'TeamWorker': team_worker_score,
                  'BehavioralSkill': behavioral_skill_score, 'CommunicationSkill': communication_skill_score,
                  'Rate': rate, }

        applicants_with_skills.insert(x, (
            [interview_results[x]['User_Email'], scores]))

    return render(request, 'screens/company_side/view_report.html',
                  {'Applicants': all_applicants, 'user_email': user_email,
                   'applicants_with_skills': applicants_with_skills})
