from django import forms
from taskmanager.models import User
from taskmanager.models import Taskmodel


class Userform(forms.ModelForm):
    class Meta:

        model = User

        fields = ["username","first_name","last_name","password","email"]

        widgets={
            'username' : forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the name"}),
            'first_name' : forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the first name"}),
            'last_name' : forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the last name"}),
            'password' : forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter the password"}),
            'email' : forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter the name"})
        }
# excluded = ("username",)
# class UserForm(forms.Form):

#     username=forms.CharField(max_length=100)

#     firstname = forms.CharField(max_length=100)

#     lastname=forms.CharField(max_length=100)

#     email=forms.EmailField()
    
#     password=forms.CharField()


class LoginForm(forms.Form):
     

     username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the name"}))
     password=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the password"}))

class TaskForm(forms.ModelForm):
    class Meta:
        model=Taskmodel
        fields=["task_name","task_description","due_date","priority"]
        labels = {
            'task_description': 'Description', 
            'due_date':'Due Date',
            'priority':'Priority'
        }


class TaskForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        widget=forms.Select(attrs={"class": "form-control mb-3"})
    )

    class Meta:
        model = Taskmodel
        fields = ['task_name', 'task_description', 'due_date', 'priority']
        # labels = {
        #     'task_name': 'Task Name',
        #     'task_description': 'Description',
        #     'due_date': 'Due Date',
        #     'priority': 'Priority',
        # }
        widgets = {
            'task_name': forms.TextInput(attrs={
                "class": "form-control mb-3 p-2",
                "placeholder": "Enter task name"
            }),
            'task_description': forms.Textarea(attrs={
                "class": "form-control mb-3 p-2",
                "rows": 4,
                "style": "resize: none;",
                "placeholder": "Enter task details"
            }),
            'due_date': forms.DateInput(attrs={
                "class": "form-control mb-3 p-2",
                "type": "date"
            }),
        }

class TaskUpdateForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        widget=forms.Select(attrs={"class": "form-control mb-3"})
    )

    class Meta:
        model = Taskmodel
        fields = ['task_name', 'task_description', 'due_date', 'priority','status']
        # labels = {
        #     'task_name': 'Task Name',
        #     'task_description': 'Description',
        #     'due_date': 'Due Date',
        #     'priority': 'Priority',
        # }
        widgets = {
            'task_name': forms.TextInput(attrs={
                "class": "form-control mb-3 p-2",
                "placeholder": "Enter task name"
            }),
            'task_description': forms.Textarea(attrs={
                "class": "form-control mb-3 p-2",
                "rows": 4,
                "style": "resize: none;",
                "placeholder": "Enter task details"
            }),
            'due_date': forms.DateInput(attrs={
                "class": "form-control mb-3 p-2",
                "type": "date"
            }),
        }
