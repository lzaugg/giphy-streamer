# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import resource_group_pb2 as resource__group__pb2


class ResourceGroupServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetResourceGroup = channel.unary_unary(
        '/io.spoud.sdm.logistics.service.resource_group.v1.ResourceGroupService/GetResourceGroup',
        request_serializer=resource__group__pb2.GetResourceGroupRequest.SerializeToString,
        response_deserializer=resource__group__pb2.GetResourceGroupResponse.FromString,
        )
    self.UpdateResourceGroup = channel.unary_unary(
        '/io.spoud.sdm.logistics.service.resource_group.v1.ResourceGroupService/UpdateResourceGroup',
        request_serializer=resource__group__pb2.UpdateResourceGroupRequest.SerializeToString,
        response_deserializer=resource__group__pb2.UpdateResourceGroupResponse.FromString,
        )
    self.CreateResourceGroup = channel.unary_unary(
        '/io.spoud.sdm.logistics.service.resource_group.v1.ResourceGroupService/CreateResourceGroup',
        request_serializer=resource__group__pb2.CreateResourceGroupRequest.SerializeToString,
        response_deserializer=resource__group__pb2.CreateResourceGroupResponse.FromString,
        )
    self.DeleteResourceGroup = channel.unary_unary(
        '/io.spoud.sdm.logistics.service.resource_group.v1.ResourceGroupService/DeleteResourceGroup',
        request_serializer=resource__group__pb2.DeleteResourceGroupRequest.SerializeToString,
        response_deserializer=resource__group__pb2.DeleteResourceGroupResponse.FromString,
        )
    self.ListResourceGroups = channel.unary_unary(
        '/io.spoud.sdm.logistics.service.resource_group.v1.ResourceGroupService/ListResourceGroups',
        request_serializer=resource__group__pb2.ListResourceGroupsRequest.SerializeToString,
        response_deserializer=resource__group__pb2.ListResourceGroupsResponse.FromString,
        )


class ResourceGroupServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetResourceGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateResourceGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateResourceGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteResourceGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListResourceGroups(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ResourceGroupServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetResourceGroup': grpc.unary_unary_rpc_method_handler(
          servicer.GetResourceGroup,
          request_deserializer=resource__group__pb2.GetResourceGroupRequest.FromString,
          response_serializer=resource__group__pb2.GetResourceGroupResponse.SerializeToString,
      ),
      'UpdateResourceGroup': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateResourceGroup,
          request_deserializer=resource__group__pb2.UpdateResourceGroupRequest.FromString,
          response_serializer=resource__group__pb2.UpdateResourceGroupResponse.SerializeToString,
      ),
      'CreateResourceGroup': grpc.unary_unary_rpc_method_handler(
          servicer.CreateResourceGroup,
          request_deserializer=resource__group__pb2.CreateResourceGroupRequest.FromString,
          response_serializer=resource__group__pb2.CreateResourceGroupResponse.SerializeToString,
      ),
      'DeleteResourceGroup': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteResourceGroup,
          request_deserializer=resource__group__pb2.DeleteResourceGroupRequest.FromString,
          response_serializer=resource__group__pb2.DeleteResourceGroupResponse.SerializeToString,
      ),
      'ListResourceGroups': grpc.unary_unary_rpc_method_handler(
          servicer.ListResourceGroups,
          request_deserializer=resource__group__pb2.ListResourceGroupsRequest.FromString,
          response_serializer=resource__group__pb2.ListResourceGroupsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'io.spoud.sdm.logistics.service.resource_group.v1.ResourceGroupService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
