# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mpi_monitor_pb2 as mpi__monitor__pb2


class MonitorStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendResources = channel.unary_unary(
                '/mpi_monitor.Monitor/SendResources',
                request_serializer=mpi__monitor__pb2.availNodes.SerializeToString,
                response_deserializer=mpi__monitor__pb2.Confirmation.FromString,
                )
        self.activeNode = channel.unary_unary(
                '/mpi_monitor.Monitor/activeNode',
                request_serializer=mpi__monitor__pb2.nodeName.SerializeToString,
                response_deserializer=mpi__monitor__pb2.Confirmation.FromString,
                )


class MonitorServicer(object):
    """Interface exported by the server.
    """

    def SendResources(self, request, context):
        """This should be used for sending resources to the server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def activeNode(self, request, context):
        """This should be used for sending shutdown notices for the clients
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendResources': grpc.unary_unary_rpc_method_handler(
                    servicer.SendResources,
                    request_deserializer=mpi__monitor__pb2.availNodes.FromString,
                    response_serializer=mpi__monitor__pb2.Confirmation.SerializeToString,
            ),
            'activeNode': grpc.unary_unary_rpc_method_handler(
                    servicer.activeNode,
                    request_deserializer=mpi__monitor__pb2.nodeName.FromString,
                    response_serializer=mpi__monitor__pb2.Confirmation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mpi_monitor.Monitor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Monitor(object):
    """Interface exported by the server.
    """

    @staticmethod
    def SendResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mpi_monitor.Monitor/SendResources',
            mpi__monitor__pb2.availNodes.SerializeToString,
            mpi__monitor__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def activeNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mpi_monitor.Monitor/activeNode',
            mpi__monitor__pb2.nodeName.SerializeToString,
            mpi__monitor__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
