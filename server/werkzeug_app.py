#!/usr/bin/env python3

from werkzeug.wrappers import Request, Response


@Request.application
def application(request):
    print(f"This web server if running at {request.remote_addr}")
    return Response('Hello beep borp I am a robot!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )