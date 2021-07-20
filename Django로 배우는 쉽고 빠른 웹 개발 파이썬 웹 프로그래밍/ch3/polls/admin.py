from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#         ('Question Statement', {'fields': ['question_text']}),
#     ]
#     # fields = ['pub_date', 'question_text']

# 외래키를 본 테이블과 참조 테이블을 한 화면에서 보여주기

# 스택 형식으로 보여주기
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 2

# 테이블 형식으로 보여주기
class ChoiceInline(admin.TabularInline):
    model = Choice
    extrea = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date') # 출력되는 컬럼 지정
    list_filter = ['pub_date']  # 컬럼(필드) 필터
    search_fields = ['question_text']   # 컬럼(필드) 검색

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)