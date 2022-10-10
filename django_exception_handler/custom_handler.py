from http import HTTPStatus

# from googletrans import Translator
from .handler import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 400:
            http_code_to_message = {v.value: v.description for v in HTTPStatus}
            new_response = {"status_code": response.status_code,
                            "message": http_code_to_message[response.status_code],
                            "is_success": False,
                            "error_details": response.data,
                            "response": None,
                            }
            response.data = new_response
        else:
            http_code_to_message = {v.value: v.description for v in HTTPStatus}

            new_response = {"status_code": response.status_code,
                            "message": http_code_to_message[response.status_code],
                            "is_success": False,
                            "error_details": response.data,
                            "response": None,
                            }
            response.data = new_response

    return response
