from django.db import models

#regras de como os dados serão organizados no DB.
class Tasks(models.Model):
    title = models.CharField("Título", max_length= 120)
    description = models.TextField("Descrição", blank=True)
    done= models.BooleanField("Concluído", default=False)
    created_at = models.DateTimeField("Criado em", auto_now_add=True) #data e hora do aparelho

    def __str__(self):
        return self.title
    



