from django.db import models
from django.db.models.functions import Cast, Coalesce
from datetime import datetime

date_real = Coalesce('date_report', 'date_assembly')