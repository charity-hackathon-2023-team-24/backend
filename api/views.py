from django.http import HttpRequest, JsonResponse


def dummy_json(request: HttpRequest) -> JsonResponse:  # noqa:ARG001
    return JsonResponse({"title": "hello from backend", "body": "You successfully received data"})
