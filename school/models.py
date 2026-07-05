from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="teachers"
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Class(models.Model):
    name = models.CharField(max_length=10, unique=True)
    study_year = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    school_class = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="students"
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Schedule(models.Model):
    DAYS = [
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday")
    ]
    day = models.CharField(max_length=10, choices=DAYS)
    start_time = models.TimeField()

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.day} {self.start_time}"


class Grade(models.Model):
    grade = models.PositiveIntegerField()
    date = models.DateField()

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.grade)
