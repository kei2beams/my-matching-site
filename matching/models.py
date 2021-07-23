from django.db import models

# Create your models here.

# pythonとDBの関係はORM(オブジェクトリレーショナルマッピング)という考え方。
# 基本的にはDBユーザとDB作成の初期設定だけで残りは、ライブラリでできるので直接DBを参照することはない。
# modelクラスを継承することで、modelを作成することができる。各フィールドに制約を色々設けることができる。
class User_mst(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )
    # age = models.IntegerField(
    #     blank=True,
    #     null=True,
    # )
    # created = models.DateTimeField(
    #     auto_now_add=True,
    #     editable=False,
    #     blank=False,
    #     null=False
    # )
    # updated = models.DateTimeField(
    #     auto_now=True,
    #     editable=False,
    #     blank=False,
    #     null=False
    # )

    def __str__(self) -> str:
        return self.name