from django.shortcuts import render, redirect
from .models import Student, determine_grade
from .forms import StudentForm
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
 
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()  # This will now calculate and save the grade
            return redirect('add_student')
    else:
        form = StudentForm()
 
    students = Student.objects.all()
    return render(request, 'reports/add_student.html', {'form': form, 'students': students})
 
def download_pdf(request):
    students = Student.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="student_marks_report.pdf"'
 
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
 
    # Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, height - 50, "Student Marks Report")
 
    # Header
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, height - 80, "Name")
    p.drawString(250, height - 80, "Subject")
    p.drawString(400, height - 80, "Marks")
    p.drawString(480, height - 80, "Grade")
    # Draw horizontal line under header
    p.line(80, height - 85, width - 80, height - 85)
 
    # Set font for the body
    p.setFont("Helvetica", 12)
 
    # Y position for student entries
    y = height - 100
 
    # Loop through students and add their data to the PDF
    for student in students:
        p.drawString(100, y, student.name)
        p.drawString(250, y, student.subject)
        p.drawString(400, y, str(student.marks))
        p.drawString(480, y, student.grade)  # Use the calculated grade
        y -= 20  # Move down for the next student entry
 
        # Draw horizontal line after each student entry
        p.line(80, y + 15, width - 80, y + 15)
 
    p.showPage()
    p.save()
    return response