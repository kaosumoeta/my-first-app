from django.db import models


class Asmr(models.Model): #asmrクラス
    """ASMR"""
    name = models.CharField("動画url", max_length = 255)
    info = models.CharField("動画情報", max_length = 255, blank = True)
    genre = models.CharField("ジャンル", max_length = 255, blank = True)

    def __str__(self):
        return self.name



