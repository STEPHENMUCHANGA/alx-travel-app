```python
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

In `__init__.py` of the `alx_travel_app` folder:
```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```

---
