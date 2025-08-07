from .models import Note
from .serializer import NoteSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notes(request):
    user = request.user
    notes = Note.object.filter(owner=user)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)
