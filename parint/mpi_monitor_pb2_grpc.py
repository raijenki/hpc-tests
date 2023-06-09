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
        self.Scale = channel.unary_unary(
                '/mpi_monitor.Monitor/Scale',
                request_serializer=mpi__monitor__pb2.additionalNodes.SerializeToString,
                response_deserializer=mpi__monitor__pb2.Confirmation.FromString,
                )
        self.RetrieveKeys = channel.unary_unary(
                '/mpi_monitor.Monitor/RetrieveKeys',
                request_serializer=mpi__monitor__pb2.nodeName.SerializeToString,
                response_deserializer=mpi__monitor__pb2.SSHKeys.FromString,
                )
        self.JobInit = channel.unary_unary(
                '/mpi_monitor.Monitor/JobInit',
                request_serializer=mpi__monitor__pb2.nodeName.SerializeToString,
                response_deserializer=mpi__monitor__pb2.Confirmation.FromString,
                )
        self.activeServer = channel.unary_unary(
                '/mpi_monitor.Monitor/activeServer',
                request_serializer=mpi__monitor__pb2.Dummy22.SerializeToString,
                response_deserializer=mpi__monitor__pb2.Confirmation.FromString,
                )
        self.checkpointing = channel.unary_unary(
                '/mpi_monitor.Monitor/checkpointing',
                request_serializer=mpi__monitor__pb2.Dummy22.SerializeToString,
                response_deserializer=mpi__monitor__pb2.Confirmation.FromString,
                )
        self.endExec = channel.unary_unary(
                '/mpi_monitor.Monitor/endExec',
                request_serializer=mpi__monitor__pb2.Dummy22.SerializeToString,
                response_deserializer=mpi__monitor__pb2.Confirmation.FromString,
                )


class MonitorServicer(object):
    """Interface exported by the server.
    """

    def Scale(self, request, context):
        """We order the server to scale (from: scheduler, to: MPIServer)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveKeys(self, request, context):
        """We send the files for updating all our hosts (from: scaled client, to: MPIServer)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JobInit(self, request, context):
        """We tell that our auxiliary pods are ready to start the job
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def activeServer(self, request, context):
        """This should be used for checking whether the master is alive
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def checkpointing(self, request, context):
        """This should be used for telling server that checkpointing is done
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def endExec(self, request, context):
        """This should be used for telling server that execution is over
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Scale': grpc.unary_unary_rpc_method_handler(
                    servicer.Scale,
                    request_deserializer=mpi__monitor__pb2.additionalNodes.FromString,
                    response_serializer=mpi__monitor__pb2.Confirmation.SerializeToString,
            ),
            'RetrieveKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveKeys,
                    request_deserializer=mpi__monitor__pb2.nodeName.FromString,
                    response_serializer=mpi__monitor__pb2.SSHKeys.SerializeToString,
            ),
            'JobInit': grpc.unary_unary_rpc_method_handler(
                    servicer.JobInit,
                    request_deserializer=mpi__monitor__pb2.nodeName.FromString,
                    response_serializer=mpi__monitor__pb2.Confirmation.SerializeToString,
            ),
            'activeServer': grpc.unary_unary_rpc_method_handler(
                    servicer.activeServer,
                    request_deserializer=mpi__monitor__pb2.Dummy22.FromString,
                    response_serializer=mpi__monitor__pb2.Confirmation.SerializeToString,
            ),
            'checkpointing': grpc.unary_unary_rpc_method_handler(
                    servicer.checkpointing,
                    request_deserializer=mpi__monitor__pb2.Dummy22.FromString,
                    response_serializer=mpi__monitor__pb2.Confirmation.SerializeToString,
            ),
            'endExec': grpc.unary_unary_rpc_method_handler(
                    servicer.endExec,
                    request_deserializer=mpi__monitor__pb2.Dummy22.FromString,
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
    def Scale(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mpi_monitor.Monitor/Scale',
            mpi__monitor__pb2.additionalNodes.SerializeToString,
            mpi__monitor__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveKeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mpi_monitor.Monitor/RetrieveKeys',
            mpi__monitor__pb2.nodeName.SerializeToString,
            mpi__monitor__pb2.SSHKeys.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JobInit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mpi_monitor.Monitor/JobInit',
            mpi__monitor__pb2.nodeName.SerializeToString,
            mpi__monitor__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def activeServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mpi_monitor.Monitor/activeServer',
            mpi__monitor__pb2.Dummy22.SerializeToString,
            mpi__monitor__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def checkpointing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mpi_monitor.Monitor/checkpointing',
            mpi__monitor__pb2.Dummy22.SerializeToString,
            mpi__monitor__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def endExec(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mpi_monitor.Monitor/endExec',
            mpi__monitor__pb2.Dummy22.SerializeToString,
            mpi__monitor__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
