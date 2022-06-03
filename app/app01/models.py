from django.db import models


# Create your models here.
class Department(models.Model):
    """department table"""
    def __str__(self):
        return self.title

    id = models.BigAutoField(verbose_name='ID', primary_key=True)  # 定义了这是自增的， 也是pk
    title = models.CharField(verbose_name='department title', max_length=32)

class Userinfor(models.Model):
    """employee table"""
    name = models.CharField(verbose_name='name', max_length=16)

    age = models.IntegerField(verbose_name='age')
    # 最大位数是10，小数点2位，defaul值是0
    #account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name='start date')

    gender_choices = (
        (1, "male"),
        (2, "female")
    ) #在内存里创建了变量
    gender = models.SmallIntegerField(verbose_name='gender', choices=gender_choices)

    #如何些foreign key
    # to 与哪张表关联
    # to_field 与哪一列关联
    # django会自动命名depart_id
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE, verbose_name='department')