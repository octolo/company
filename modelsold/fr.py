
class CompanyFR(Base):
    siren = models.CharField(max_length=9, unique=True)
    ape = models.CharField(_.corebusiness, max_length=5)
    legalform = models.CharField(_.legalform, max_length=4)

CHOICES_ANNOUNCE = sorted(list(choices.ANNOUNCE), key=lambda x: x[1])
class Balo(Base):
    announce = models.CharField(choices=CHOICES_ANNOUNCE, max_length=3, null=True)
    company = models.ForeignKey(conf.ForeignKey.Company, on_delete=models.CASCADE)
    case = models.PositiveIntegerField()
    link = models.URLField()
    file_link = models.URLField()
    date = models.DateField()

    class Meta(Base.Meta):
        abstract = True

    def save(self, *args, **kwargs):
        self.date = datetime.datetime.strptime(self.date, conf.Announce.Balo_dateformat).date()
        super().save()
