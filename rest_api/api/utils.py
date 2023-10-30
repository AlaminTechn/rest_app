from rest_framework import status
from rest_framework.response import Response

def custom_response(data, status_code, message=None, error=None):
    response = {
        "message": message,
        "status_code": status_code,
        "data": data,
        "error": error
    }
    return Response(response, status=status_code)
