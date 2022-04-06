from django.db import models


class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract  = True

# Create your models here.
class State(TimeBasedModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} State'


class LGA(TimeBasedModel):
    name = models.CharField(max_length=30)
    state = models.ForeignKey('poll.State', on_delete=models.CASCADE)
    lga_id = models.IntegerField()
    description = models.CharField(max_length=255)
    entered_by = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField(max_length=25)

    def __str__(self):
        return f'{self.name} LGA'


class Ward(TimeBasedModel):
    name = models.CharField(max_length=30)
    ward_id = models.IntegerField()
    lga = models.ForeignKey('poll.LGA', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    entered_by = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField(max_length=25)

    def __str__(self):
        return f'{self.name} Ward'


class PollingUnit(TimeBasedModel):
    polling_unit_id = models.IntegerField()
    name = models.CharField(max_length=30)
    ward = models.ForeignKey('poll.Ward', on_delete=models.SET_NULL, null=True, blank=True)
    lga = models.ForeignKey('poll.LGA', on_delete=models.SET_NULL, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    description  = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    entered_by = models.CharField(max_length=40, null=True, blank=True)
    ip_address = models.GenericIPAddressField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f'{self.name} Unit'



class Agent(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField()
    polling_unit = models.OneToOneField('poll.PollingUnit', on_delete=models.CASCADE)

    def __str__(self):
        return f'Agent {self.first_name} {self.last_name}'


class Party(TimeBasedModel):
    name =  models.CharField(max_length=15)
    abbreviation =  models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name} Party'


class Result(TimeBasedModel):
    polling_unit = models.ForeignKey('poll.PollingUnit', on_delete=models.CASCADE)
    party = models.ForeignKey('poll.Party', on_delete=models.CASCADE)
    score = models.IntegerField()
    entered_by = models.CharField(max_length=30, null=True, blank=True)
    ip_address = models.GenericIPAddressField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f'{self.polling_unit} {self.party} scored {self.score}'
    


