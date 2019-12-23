from django.db import models


class Place1(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)

    class Meta:
        verbose_name = '장소1'
        verbose_name_plural = '장소 목록'
        ordering = ['name']

    def __str__(self):
        return self.name


class Restaurant1(Place1):
    # 이름이 중복되어 블러오지 못하는 경우 일단 클래스 명을 바꾸고 이전까지 했던 Migration 을 삭제한다
    # ./manage.py migrate <취소하고자 하는 앱 이름> zero
    # ./manage.py showmigration 을 하면 해당 앱의 migration이 빈칸으로 되어있는 것을 확인가능하다.
    # 해당 migration 파일들을 직접 삭제해준다.
    # 그리고 다시 makemigration, migrate 실행

    # 명시적으로 multi-table inheritance를 구현하는 OneToOneField를 지칭
    place1_ptr = models.OneToOneField(Place1, parent_link=True, related_name='restaurant1', related_query_name='restaurant1_by_oto', on_delete=models.CASCADE)

    # 기본값을 사용할 경우, Place1의 relate_query_name이 겹칠 수 있는 ManyToManyField를 선언
    near_place = models.ManyToManyField(Place1, related_name='restaurant_set', related_query_name='restaurant1_by_near_places')

    hot_dogs = models.BooleanField(default=False)
    pizza = models.BooleanField(default=False)

    # 명시적으로 이렇게 이루어져있는 것으로 되어있다, 암시적으로 원투원필드와 연결되어있다.
    # place_ptr = models.OneToOneField(Place1, parent_link=True)

    def __str__(self):
        return f'{self.name} (핫도그: {self.hot_dogs}, 피자: {self.pizza})'
