import time
import typing

import grpc
import grpc._channel

import grpc_interceptor
import grpc.experimental.gevent as grpc_gevent

grpc_gevent.init_gevent()


class LocustGRPCInterceptor(grpc_interceptor.ClientInterceptor):
    def __init__(self, environment, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.env = environment

    def intercept(
        self,
        method: typing.Callable,
        request_or_iterator: typing.Any,
        call_details: grpc.ClientCallDetails,
    ):
        response = None
        exception = None
        start_perf_counter = time.perf_counter()
        response_length = 0
        try:
            response = method(request_or_iterator, call_details)
            # _MultiThreadedRendezvous is not working with gevent
            # because of extra thread for result() call
            if not isinstance(response, grpc._channel._MultiThreadedRendezvous):
                response_length = response.result().ByteSize()
            else:
                response = [result for result in response]
        except grpc.RpcError as e:
            exception = e

        self.env.events.request.fire(
            request_type="grpc",
            name=call_details.method,
            response_time=(time.perf_counter() - start_perf_counter) * 1000,
            response_length=response_length,
            response=response,
            context=None,
            exception=exception,
        )
        return response
