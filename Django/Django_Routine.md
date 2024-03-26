# Django_Routine

1. 가상 환경 venv 생성 : python -m venv venv
2. 가상 환경 활성화 : source venv/Scripts/activate
3. 가상 환경에 설치된 패키지 목록 확인 : pip list
4. Django 설치 : pip install django
5. 의존성 패키지 목록 생성 : pip freeze > requirements.txt
6. Django 프로젝트 생성 : django-admin startproject 프로젝트 이름 .
7. Django 서버 실행 : python manage.py runserver
8. 앱 생성 : python manage.py startapp 앱 이름 (복수형 s)
9. 앱 등록 : settings.py -> '앱 이름' 추가
10. 모델 정의 시 : python manage.py makemigrations , python manage.py migrate

10. Django에서 template를 인식하는 경로 규칭
    - app폴더/templates/articles/index.html
    - app폴더/templates/index.html

11. QuerySet API 세팅 : pip install ipython, pip install django-extensions
11-1 : settings.py에 'django_extensions', 추가

12. 관리자 계정 생성 - python manage.py createsuperuser
	- 원하는 사용자 이름 (username)
	- 이메일 주소 (email) - 건너뛰기 가능
	- 원하는 비밀번호 (password)
	- admin.py에 등록하기
	```python
	from django.contrib import admin
	from .models import Todo
	# Register your models here.

	admin.site.register(Todo)
	```