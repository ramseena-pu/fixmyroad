from rest_framework import serializers
from reports.models import RoadIssue
class RoadIssueSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField()
    description=serializers.CharField()
    issue_type=serializers.ChoiceField(choices=RoadIssue.ISSUE_TYPES)
    priority=serializers.ChoiceField(choices=RoadIssue.PRIORITIES)
    status=serializers.ChoiceField(choices=RoadIssue.STATUS_CHOICES)
    location=serializers.CharField()
    landmark=serializers.CharField()
    latitude=serializers.FloatField()
    longitude=serializers.FloatField()
    reported_by=serializers.CharField()
    contact_number=serializers.CharField()
    image=serializers.ImageField(required=False)
    created_at=serializers.DateTimeField(read_only=True)
    updated_at=serializers.DateTimeField(read_only=True)
    
    