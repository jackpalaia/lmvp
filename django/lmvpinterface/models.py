from django.db import models
from rest_framework import serializers
from hashlib import sha1
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=64, unique=True)
    contributing_users = models.ManyToManyField('User')

class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField('time user created', auto_now_add=True)

class Commit(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    hash = models.BinaryField(max_length=49, unique=True) #SHA1 is 160 bits or 49 decimal digits
    created = models.DateTimeField('time commit created', auto_now_add=True)
    file = models.FileField(blank=True) #django docs suggest using ModelFormWithFileField in views
    def save(self, *args, **kwargs):
        hasher = sha1()
        hasher.update(self.author.encode('utf-8'))
        hasher.update(self.project.encode('utf-8'))
        hasher.update(self.created.encode('utf-8'))
        if file:
            hasher.update(self.file.path.encode('utf-8')) # TODO actually hash the file contents, also
        self.hash = hasher.digest()
        super().save(*args, **kwargs)

class BaseAttribute(models.Model):
    class Meta:
        abstract = True
    commit = models.ForeignKey(Commit, related_name="%(class)ss", on_delete=models.CASCADE) #now Commit has a field called metrics
    name = models.CharField(max_length=128)
class Metric(BaseAttribute):
    value = models.FloatField()
class Property(BaseAttribute):
    value = models.CharField(max_length=128, blank=True)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #exclude = ['created', ] #TODO how to allow GETting this field but not POSTing it?
class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        exclude = ['file', 'hash'] # for now, until we figure out how to deal with uploads
    metrics = serializers.HyperlinkedRelatedField(many=True, view_name='metric-detail', read_only=True) #all the metrics related to this commit
    properties = serializers.HyperlinkedRelatedField(many=True, view_name='property-detail', read_only=True) #all the metrics related to this commit
#TODO: metrics can get added to each commit. when showing in a table, how to handle too many columns? Edit metrics through API?
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'
