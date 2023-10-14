from rest_framework import status
from Core.models import Student


class Info:
    RESPONSE_DATA = {}
    RESPONSE_STATUS = 'response_status'
    ERRORS = None


class CollectStudentInfo:
    collection_fields = {}

    def __init__(self):
        self._error = {}
        self._student = None
        self._status = None
        self._info = Info

    @property
    def get_group(self):
        return self._student.group

    @property
    def get_university(self):
        group = self.get_group
        return group.university

    @property
    def get_custom_user(self):
        return self._student.user

    def set_student(self, user):
        self._student = Student.objects.get(user=user)

    def collect(self, student):
        info = Info
        self.set_student(student)
        try:
            user = self.get_custom_user()
            group = self.get_group()
            university = self.get_university
            info.RESPONSE_DATA.update({'univercity': university.name})
            info.RESPONSE_DATA.update({'id': self._student.id})
            info.RESPONSE_DATA.update({'username': {'name': user.name, 'surname': user.surname,
                                                    'last_name': user.lastname}})
            info.RESPONSE_DATA.update({'birthDay': user.date_birth})
            info.RESPONSE_DATA.update({'validUntil': str(self._student)})
            info.RESPONSE_DATA.update({'studyGroup': {group.name, group.course}})
            info.RESPONSE_DATA.update({'photo': user.avatar})
            info.RESPONSE_DATA.update({'qr': user.qr})
            info.RESPONSE_STATUS = status.HTTP_200_OK
        except Exception as error:
            info.RESPONSE_STATUS = status.HTTP_400_BAD_REQUEST
            info.ERRORS = error

        return info
