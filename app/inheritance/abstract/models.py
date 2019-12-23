from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']  # name 순서대로 정렬이 됨


class Student(CommonInfo):
    school = models.CharField(max_length=30)

    class Meta:  # ordering 이 없어짐
        verbose_name = '학생'
        verbose_name_plural = '학생 목록'

    # class Meta(CommonInfo.Meta): # 이렇게 쓰면 부모클래스의 메타속성을 그대로 가져오면서 내 메타속성을 적용시킬 수 있음
    #     verbose_name = '학생'
    #     verbose_name_plural = '학생 목록'

    def __str__(self):
        return f'{self.name}의 학교: {self.school}'


class Instructor(CommonInfo):
    academy = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}의 학원: {self.academy}'


# Be careful with related_name and related_query_name

class Base(models.Model):
    m2m = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s')
    # 실제 데이터베이스에는 변경된 사항 없이 고유한 related_name 이 생성된다.

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class Childb(Base):
    pass