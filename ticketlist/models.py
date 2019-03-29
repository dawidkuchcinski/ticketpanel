from django.db import models

# Create your models here.
#Temat
#Treść
#Status
#Typ
#Data utworzenia
#data modyfikowania
#Program w kótrym jest problem
#firma, do której należy program

class Status(models.Model):
    status_name = models.CharField(max_length=254,unique=True)

    def __str__(self):
        return self.status_name

class Ticket(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    data_ostatniej_modyfikacji = models.DateTimeField(auto_now=True)
    uzytkownik = models.CharField(max_length=254, default=0)
    firma = models.CharField(max_length=254)

    def __str__(self):
        id2 = str(self.id)
        return id2

class Damage(models.Model):
    damagename = models.CharField(max_length=254)
    damagetype = models.CharField(max_length=254, default="wizualne")
    repairprice = models.IntegerField()

    def __str__(self):
        return self.damagename

class Devicemodel(models.Model):
    modelname = models.CharField(max_length=254)

    def __str__(self):
        return self.modelname
    
class Device(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    model = models.ForeignKey(Devicemodel, on_delete=models.CASCADE)
    serialnumber = models.CharField(max_length=254)

    def __str__(self):
        return self.serialnumber
    
class Devicedamage(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=1)
    damagedpart = models.ForeignKey(Damage, on_delete=models.CASCADE)
    damagedescription = models.TextField()

    def __str__(self):
        return self.damagedescription
