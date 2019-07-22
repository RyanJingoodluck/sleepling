import json

import requests
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import list_route, detail_route
from rest_auth.app_settings import create_token, LoginSerializer
from rest_auth.models import TokenModel

from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @list_route(methods=['post', ])
    def wechat_login(self, request):
        # 前端发送code到后端,后端发送网络请求到微信服务器换取openid
        code = request.data.get('code')
        if not code:
            return Response({'message': '缺少code'}, status=status.HTTP_400_BAD_REQUEST)

        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&" \
              "grant_type=authorization_code".format(settings.WECHAT_APP_ID, settings.WECHAT_APP_KEY, code)

        r = requests.get(url)
        res = json.loads(r.text)
        openid = res['openid'] if 'openid' in res else None
        # session_key = res['session_key'] if 'session_key' in res else None
        if not openid:
            return Response({'message': '微信调用失败'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # 判断用户是否第一次登录
        user = User.objects.filter(openid=openid).first()
        if not user:
            # 微信用户第一次登陆,新建用户
            # username = request.data.get('nickname')
            # sex = request.data.get('sex')
            # avatar = request.data.get('avatar')
            user = User.objects.create(openid=openid,username=openid)
            # user.set_password(openid)

        serializer_class = LoginSerializer
        token_model = TokenModel
        token = create_token(token_model, user,
                             serializer_class)
        resp_data = {
            "token": token,
        }

        return Response(resp_data)
