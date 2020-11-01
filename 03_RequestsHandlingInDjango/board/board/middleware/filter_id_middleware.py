from django.core.exceptions import PermissionDenied
import os
import time
import datetime

DELAY_TIME = 5
DELAY_NUMBER = 3


class WhiteListIPMiddleware:  # task 1 lesson 3.3
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ip = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ip:
            raise PermissionDenied

        response = self.get_response(request)

        return response


class BlackListIPMiddleware:  # task 2 lesson 3.3
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ip = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')
        if ip in allowed_ip:
            raise PermissionDenied

        response = self.get_response(request)

        return response


class DelayIPMiddleware:  # task 3 lesson 3.3
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):
        self.count += 1
        if self.count % DELAY_NUMBER == 0:
            time.sleep(DELAY_TIME)
        response = self.get_response(request)

        return response


class LogWriter:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_file = 'log.txt'

    def __call__(self, request):
        log_path = os.path.join(os.getcwd(), self.log_file)
        response = self.get_response(request)
        with open(log_path, mode='a', encoding='utf8') as file:
            split_request = str(request).split(' ')
            file.write(f'{datetime.datetime.now()};  {split_request[1]}  {split_request[2][:-1]}\n')

        return response
