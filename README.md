# Make sure you have upgraded version of pip
Windows
```
py -m pip install --upgrade pip
```

Linux/MAC OS
```
python3 -m pip install --upgrade pip
```

## install package
be sure you are in directory of project
```
pip install setup.py
```

## add required configurations to django settings.py

add this two line in REST_FRAMEWORK to settings

```
'EXCEPTION_HANDLER': 'django_exception_handler.custom_handler.custom_exception_handler'
'DEFAULT_RENDERER_CLASSES': ['django_exception_handler.renderer.ProjectRender']
```

add this config of your handler in settings
```
EXCEPTIONS_HOG = {
    "EXCEPTION_REPORTING": "django_exception_handler.exception_handler.handler.exception_reporter",
    "ENABLE_IN_DEBUG": False,
    "NESTED_KEY_SEPARATOR": ".",
    "SUPPORT_MULTIPLE_EXCEPTIONS": True,
    "FARSI_EXCEPTION": True
}
```

if FARSI_EXCEPTION is true, you should add your persian dict and errors in settings.py
```
PERSIAN_DICT = yourPersianDict
PERSIAN_ERROR_CODES = yourErrorCode
```