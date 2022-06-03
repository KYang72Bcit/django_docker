from django.shortcuts import render, redirect
from app01.models import Department, Userinfor
from app01 import models
from django import forms


# Create your views here.
def department(request):
    # fetch data from DB
    department_data = Department.objects.all()
    return render(request, 'admin.html', {'department_data': department_data})


def add_department(request):
    """add department"""
    if request.method == 'GET':
        return render(request, 'department_add.html')
    title = request.POST.get('title')
    Department.objects.create(title=title)
    return redirect('/depart/list')


def delete_department(request):
    """delete department"""
    uid = request.GET.get('uid')
    Department.objects.filter(id=uid).delete()
    return redirect('/depart/list')


# http://127.0.0.1/department/1/edit
def edit_department(request, uid):
    """edit department"""
    data = Department.objects.filter(id=uid).first()
    return render(request, 'department_edit.html', {'department_data': data})


def users(req):
    """show user list"""
    employees = Userinfor.objects.all()
    # for employee in employees:
    # print(employee.depart.title)
    # print(employee.get_gender_display())

    return render(req, 'user_admin.html', {'users': employees})


def add_user(req):
    if req.method == 'GET':
        departments = Department.objects.all()
        gender_choices = Userinfor.gender_choices
        # print(gender_choices)
        return render(req, 'add_user.html', {'departments': departments, 'gender_choices': gender_choices})

    name = req.POST.get('name')
    age = req.POST.get('age')
    create_time = req.POST.get('create_date')
    gender = req.POST.get('gender')
    depart_id = req.POST.get('depart')
    Userinfor.objects.create(name=name, age=age, create_time=create_time, gender=gender, depart_id=depart_id)
    return redirect('/user/list/')


###########ModelFrom example ##########


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.Userinfor
        fields = ['name', 'age', 'create_time', 'gender', 'depart']
        # widgets = {
        #     "name": forms.TextInput(attrs={'class': 'form-control'}),
        #     "age": forms.NumberInput(attrs={'class': 'form-control'}),
        #     "create_time": forms.DateInput(attrs={'class': 'form-control'}),
        #     "gender": forms.TextInput(attrs={'class': 'form-control'})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def add_user_modelForm(req):
    """add user based on Model Form"""
    if req.method == "GET":
        form = UserModelForm()
        return render(req, 'user_model.html', {'form': form})

    # verity POST data
    form = UserModelForm(data=req.POST)
    #如果数据合法，保存到数据库
    if form.is_valid():
        print(form.cleaned_data)
        #{'name': 'Daisy', 'age': 35, 'create_time': datetime.date(2021, 12, 3), 'gender': 2, 'depart': <Department: DevOps>}
        form.save()
        return redirect('/user/list')
    else:
        #校验失败
        print()
        return render(req, 'user_model.html', {'form': form})
