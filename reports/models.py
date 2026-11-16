from django.db import models

# Create your models here.
# title,location,latitude,longitude,posted_by,sataus,category,posted_date
#image(null)

from django.db import models


class RoadIssue(models.Model):

    ISSUE_TYPES = [
        ("POTHOLE", "Pothole"),
        ("ROAD_DAMAGE", "Road Damage"),
        ("WATERLOGGING", "Waterlogging"),
        ("OPEN_DRAIN", "Open Drain"),
        ("OTHER", "Other"),
    ]

    PRIORITIES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
    ]

    STATUS_CHOICES = [
        ("REPORTED", "Reported"),
        ("IN_PROGRESS", "In Progress"),
        ("RESOLVED", "Resolved"),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField()

    issue_type = models.CharField(
        max_length=20,
        choices=ISSUE_TYPES,
        default="POTHOLE"
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITIES,
        default="MEDIUM"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="REPORTED"
    )

    location = models.CharField(max_length=255)
    landmark = models.CharField(max_length=150, blank=True)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    reported_by = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, blank=True)

    image = models.ImageField(
        upload_to="road_issues/",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
