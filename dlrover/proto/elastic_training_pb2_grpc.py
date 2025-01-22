# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dlrover.proto import elastic_training_pb2 as dlrover_dot_proto_dot_elastic__training__pb2


class MasterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.report = channel.unary_unary(
                '/elastic.Master/report',
                request_serializer=dlrover_dot_proto_dot_elastic__training__pb2.Message.SerializeToString,
                response_deserializer=dlrover_dot_proto_dot_elastic__training__pb2.Response.FromString,
                )
        self.get = channel.unary_unary(
                '/elastic.Master/get',
                request_serializer=dlrover_dot_proto_dot_elastic__training__pb2.Message.SerializeToString,
                response_deserializer=dlrover_dot_proto_dot_elastic__training__pb2.Message.FromString,
                )


class MasterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def report(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MasterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'report': grpc.unary_unary_rpc_method_handler(
                    servicer.report,
                    request_deserializer=dlrover_dot_proto_dot_elastic__training__pb2.Message.FromString,
                    response_serializer=dlrover_dot_proto_dot_elastic__training__pb2.Response.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=dlrover_dot_proto_dot_elastic__training__pb2.Message.FromString,
                    response_serializer=dlrover_dot_proto_dot_elastic__training__pb2.Message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'elastic.Master', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Master(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def report(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elastic.Master/report',
            dlrover_dot_proto_dot_elastic__training__pb2.Message.SerializeToString,
            dlrover_dot_proto_dot_elastic__training__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/elastic.Master/get',
            dlrover_dot_proto_dot_elastic__training__pb2.Message.SerializeToString,
            dlrover_dot_proto_dot_elastic__training__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
