from django.db import models

class Studenti(models.Model):
      nome = models.CharField(max_length=10)
      cognome = models.CharField(max_length=10, blank=True)
      def __str__(self):
        return f"ciao {self.nome} {self.cognome}"