from django.db import models


# class UserMixin(models.Model):
#     # nickname = models.CharField(max_length=30, blank=True)
#     pass
#
#     class Meta:
#         abstract = True


class BaseUser(models.Model):
    is_superuser = models.BooleanField(default=False)

    def show_pk(self):
        print(self.pk)


class NormalUser(BaseUser):

    # user class를 만든다음에 각 클래스별로 하는일을 정해주는 것
    # 필드자체가 더 필요한건 아니지만 용도를 구분하고싶을때 proxy 모델을 사용
    # 커스텀 메서드들이 많이 생겨나는데, 용도가 다 다른데, 모든 용도에 대한 커스텀메서드들은
    # 유저 클래스는 그대로 있되 어드민에서만 쓰는 함수 등 이럴때에는
    # 프록시 모델을 만들어서 갖다 쓰면 된다.
    # 다른곳에서는 굳이 볼 필요가 없고.. 용도에 따라 모델 클래스를 사용할때 프록시 모델을 사용
    class Meta:
        proxy = True
        # 프록시 모델에만 오더링이 필요한경우 사용가능하다.
        # ordering = ['~']

        # 그리고 프록시 모델은 반드시 한개의 클래스만을 상속받아야 한다.
        # 즉, 다중상속을 허용하지 않음 (파이썬은 허용하되 쓰지말라고 한다)
        # 정상적으로 사용가능한 클래스를 동시에 상속받으면 우선순위의 문제가 생길 수 있고, 프로그램 구조 파악이 어려워진다.
        # 그래서 상속이 되기 위해서만 사용되는 클래스에만 다중상속을 사용한다.
        # 다중상속을 받게되면 각각이 가진 필드를 상속받은 프록시 모델은 불가능
        # 프록시모델은 딱 하나의 테이블에만 들어갈 수 있다.
        # 서로다른 모델을(테이블 2개) 상속받게 되면 프록시 모델은 자신만의 테이블을 갖지 않고
        # BaseUser를 기반으로 만들고 있기 때문에 반드시 하나의 비 산정 프록시 모델만
        # 근데 필드가 없다면 받을 수 있다.
        # 필드가 없는 추상모델은 얼마든지 상속 받을 수 있다.


# SuperUser모델에서 사용할 Manager
class SuperUserManager(models.Manager):
    def get_queryset(self):
        # 기본 Queryset을 제한
        return super().get_queryset().filter(is_superuser=True)


class SuperUser(BaseUser):
    # 프록시 모델에 Manager 지정
    objects = SuperUserManager()

    class Meta:
        proxy = True

    # 이 클래스에만 유저를 지우는 함수를 생성
    def delete_user(self, pk):
        BaseUser.objects.get(pk=pk).delete()


# multiple inheritance
# class Book(models.Model):
#     pass
#
#
# # class Article(models.Model):
# #     pass
#
#
# class BookReview(Book):
#     pass

