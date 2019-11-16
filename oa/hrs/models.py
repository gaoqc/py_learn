from django.db import models


# Create your models here.
class Dept(models.Model):
    ''' 部门类 '''

    def __str__(self):
        return self.name

    no = models.IntegerField(primary_key=True, db_column='dno', verbose_name='编号')
    name = models.CharField(max_length=20, db_column='dname', verbose_name='名称')
    location = models.CharField(max_length=100, db_column='dloc', verbose_name='位置')
    class Meta:
        db_table = 'tb_dept'


class Emp(models.Model):
    '''员工类'''

    def __str__(self):
        return self.name


    no = models.IntegerField(primary_key=True, db_column='eno', verbose_name='员工编号')
    job = models.CharField(max_length=100, verbose_name='职位',help_text='职位名称吖')
    name = models.CharField(max_length=50, verbose_name='名字',unique=True)
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='主管')
    sal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='工资',default=15000)
    comm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='补贴')
    dept = models.ForeignKey(Dept, db_column='dno', on_delete=models.PROTECT, verbose_name='所在部门')

    class Meta:
        db_table = 'tb_emp'
        verbose_name='员工相关信息'
