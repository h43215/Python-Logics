from re import S
from django.http import HttpResponse
from django.shortcuts import render
from .models import StudentInfo,TeacherInfo

# Create your views here.

def index(request):
    print(request.user)
    return HttpResponse("Hello")


def Create_Student(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST.get("email")
        DOB = request.POST.get("bday")
        print(fname, lname, email, DOB)
        ins = StudentInfo.objects.create(fname=fname,lname=lname,email=email,DOB=DOB)
        print(ins.id)
        return HttpResponse("success")
    else:
        return render(request, 'student.html')

# def get_student(request):                                #Student all data add in one variable and other method use in single def functions
#     if request.method == "GET":
#         data_dict = {}
#         data_list = []
#         student = StudentInfo.objects.all()
#         for x in student:
#             data = {
#                 "id":x.id,
#                 "fname":x.fname,
#                 "lname":x.lname,
#                 "dob":x.DOB,
#                 "email":x.email
#             }
#             data_list.append(data)
#         data_dict["students"] = data_list
#         return JsonResponse(data_dict)


def create_teacher(request):
    if request.method == "POST":
       fname = request.POST["fname"] 
       lname = request.POST["lname"]
       subject = request.POST["subject"]
       tc = TeacherInfo.objects.create(fname= fname,lname=lname,subject=subject)
       print(tc.id)
       return HttpResponse("Success")
    else:
        return render(request,'tc.html')
      


def principal(request):
    if request.method == "POST":
        print(request.POST)
        # manage_staff = request.POST["manage_staff"]
        # manage_salary = request.POST["manage_salary"]
        # PM = Principal.objects.create(manage_staff=manage_staff, manage_salary=manage_salary)
        # print(PM.id)
        data_dict = {}
        data_list = []
        if request.POST.get("radio")=="Student":    # data faching to redio  (id=id)
            # its secound method
            # are you print (id=id)
            # id = request.POST.get("id")
            # student = StudentInfo.objects.filter(id=id)

            student = StudentInfo.objects.filter(id=request.POST.get("id")) # student filler
            for x in student:
                data = {
                    "id":x.id,
                    "fname":x.fname,
                    "lname":x.lname,
                    "dob":x.DOB,
                    "email":x.email
                }
                data_list.append(data)
            data_dict["students"] = data_list
        else:
            teacher = TeacherInfo.objects.filter(id=request.POST.get("id"))
            for y in teacher:
                data = {
                    "id":y.id,
                    "fname":y.fname,
                    "lname":y.lname,
                    "subject":y.subject
                }
                data_list.append(data)
            data_dict["teachers"] =data_list
        print(data_dict)
        return render(request, 'principal.html',{"data":data_dict})
    else:

        return render(request, 'principal.html')
         
        


# Post and get method
# Both side is same but some change's in method  
# "POST"= in this method data will show on Dic. 
# "POST".get =  in this method data will show on list


# data = {
#     "email":"pragnesh"
# }


# print(data)
# print(data["email"])  POST
# print(data.get("email")) POST.get 

