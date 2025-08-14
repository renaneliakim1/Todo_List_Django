from django.db import models

#regras de como os dados serão organizados no DB.
class Tasks(models.Model):
    title = models.CharField("Título", max_length= 120)#campo de texto com tamanho máximo de 120 caracteres
    description = models.TextField("Descrição", blank=True)#campo de texto que pode ficar em branco
    done= models.BooleanField("Concluído", default=False)#se a tarefa foi concluída ou não
    created_at = models.DateTimeField("Criado em", auto_now_add=True) #data e hora do aparelho
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE) #relacionamento com a tabela user


    def __str__(self):
        
        return self.title
    



