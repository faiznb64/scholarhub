from django.db import models

class Subject(models.Model):
    sub_name=models.CharField(max_length=100)
    sub_discription=models.TextField()
    
    def __str__(self):
        return self.sub_name


class Mentor(models.Model):
    men_name=models.CharField(max_length=255)
    men_spec=models.CharField(max_length=255)
    sub_name=models.ForeignKey(Subject,on_delete=models.CASCADE)
    men_image=models.ImageField(upload_to='mentor')

    def __str__(self):
        return 'Mr. '+ self.men_name + ' (' + self.men_spec + ')'

class Booking(models.Model):
    s_name=models.CharField(max_length=255)
    s_phone=models.CharField(max_length=10)
    s_email=models.EmailField()
    men_name=models.ForeignKey(Mentor,on_delete=models.CASCADE,)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)