from django.db import models
from django.db.models import JSONField

# The Search Form stuff
STATE_CHOICES = [
    ("","Select State"),
    ("AL","AL"),
    ("AK","AK"),
    ("AZ","AZ"),
    ("AR","AR"),
    ("CA","CA"),
    ("CO","CO"),
    ("CT","CT"),
    ("DE","DE"),
    ("DC","DC"),
    ("FL","FL"),
    ("GA","GA"),
    ("HI","HI"),
    ("ID","ID"),
    ("IL","IL"),
    ("IN","IN"),
    ("IA","IA"),
    ("KS","KS"),
    ("KY","KY"),
    ("LA","LA"),
    ("ME","ME"),
    ("MD","MD"),
    ("MA","MA"),
    ("MI","MI"),
    ("MN","MN"),
    ("MS","MS"),
    ("MO","MO"),
    ("MT","MT"),
    ("NE","NE"),
    ("NV","NV"),
    ("NH","NH"),
    ("NJ","NJ"),
    ("NM","NM"),
    ("NY","NY"),
    ("NC","NC"),
    ("ND","ND"),
    ("OH","OH"),
    ("OK","OK"),
    ("OR","OR"),
    ("PA","PA"),
    ("RI","RI"),
    ("SC","SC"),
    ("SD","SD"),
    ("TN","TN"),
    ("TX","TX"),
    ("UT","UT"),
    ("VA","VA"),
    ("VT","VT"),
    ("WA","WA"),
    ("WV","WV"),
    ("WI","WI"),
    ("WY","WY"),
]
class Search(models.Model):
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    genre = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class save_Ticket(models.Model):
    data = JSONField()