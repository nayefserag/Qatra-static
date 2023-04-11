from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

class ClearFormFieldsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_key = request.session.session_key
        if session_key:
            try:
                session = Session.objects.get(session_key=session_key)
                if not session.expire_date:
                    request.session.flush()
                else:
                    store = SessionStore(session_key=session_key)
                    if 'form_fields' in store:
                        del store['form_fields']
                        store.save()
            except Session.DoesNotExist:
                pass
        response = self.get_response(request)
        return response
