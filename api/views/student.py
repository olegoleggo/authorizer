from rest_framework.views import APIView, Response
from api.service.student.collectInfo import CollectStudentInfo
from api.serializers.student.get import StudentIdSerializers
from loguru import logger


class StudentInfo(APIView, CollectStudentInfo):

    def get(self):
        user = self.request.user
        execute = self.collect(user)
        if execute.ERRORS:
            serializer = StudentIdSerializers(execute.RESPONSE_DATA)
            return Response(serializer, status=execute.RESPONSE_STATUS)
        else:
            logger.error(execute.ERRORS)
            return Response(status=execute.RESPONSE_STATUS)


