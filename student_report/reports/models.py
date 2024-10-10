from django.db import models
 
class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)  # Ensure this field exists
    marks = models.IntegerField()
    grade = models.CharField(max_length=2, blank=True)  # Optional if you're calculating on the fly
 
    def save(self, *args, **kwargs):
        # Calculate grade before saving
        self.grade = determine_grade(self.marks)
        super().save(*args, **kwargs)
 
def determine_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'f'
 