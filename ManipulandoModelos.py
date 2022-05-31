# ManipulandoModels
# >>> python manage.py shell
# >>> import os
# >>> os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_model.settings')
# >>> import django
# >>> django.setup()
# >>> from exemplo.models import Empresa
# >>> google = Empresa(nome='Google')
# >>> google.save()
# >>> facebook = Empresa.objects.create(nome='Facebook')
# >>> ibm = Empresa.objects.create(nome='IBM')
# >>> lista = Empresa.objects.all()
# >>> lista
# >>> lista = Empresa.objects.filter(id=2)
# >>> lista = Empresa.objects.filter(nome__contains='oo')
# >>> lista = Empresa.objects.filter(nome__icontains='Oo')  # o filter traz uma lista
# >>> objeto = Empresa.objects.get(id=4)
# >>> 
