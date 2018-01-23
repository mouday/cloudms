from django.db import models

# Create your models here.

class MsgData(models.Model):
    msg_id = models.AutoField(primary_key=True)
    send_name =models.CharField(max_length = 20)
    receive_name = models.CharField(max_length = 20)
    message = models.TextField()
    send_time = models.CharField(max_length = 20)

    def __str__(self):
        return (msg_id, send_name, receive_name, message, send_time)
