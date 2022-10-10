from http import HTTPStatus

from rest_framework import renderers


class ProjectRender(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']
        if response.status_code in range(200, 300):
            http_code_to_message = {v.value: v.description for v in HTTPStatus}
            new_response = {"status_code": response.status_code,
                            "message": http_code_to_message[response.status_code],
                            "is_success": True,
                            "error_details": None,
                            "response": data,
                            }
            return super(ProjectRender, self).render(new_response, accepted_media_type, renderer_context)
        else:
            return super(ProjectRender, self).render(response.data, accepted_media_type, renderer_context)
