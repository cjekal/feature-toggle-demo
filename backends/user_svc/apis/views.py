from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class UserProfileView(APIView):
    def get(self, request, pk):
        print(f"request.data: {request.data}")
        user_profile = {
            "id": pk,
            "user_name": f"user with id: {pk}",
            "payment_limit": pk * 100
        }
        return Response(user_profile)
