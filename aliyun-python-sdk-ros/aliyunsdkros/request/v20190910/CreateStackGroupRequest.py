# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkros.endpoint import endpoint_data

class CreateStackGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ROS', '2019-09-10', 'CreateStackGroup','ros')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_TemplateBody(self):
		return self.get_query_params().get('TemplateBody')

	def set_TemplateBody(self,TemplateBody):
		self.add_query_param('TemplateBody',TemplateBody)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_ExecutionRoleName(self):
		return self.get_query_params().get('ExecutionRoleName')

	def set_ExecutionRoleName(self,ExecutionRoleName):
		self.add_query_param('ExecutionRoleName',ExecutionRoleName)

	def get_TemplateURL(self):
		return self.get_query_params().get('TemplateURL')

	def set_TemplateURL(self,TemplateURL):
		self.add_query_param('TemplateURL',TemplateURL)

	def get_StackGroupName(self):
		return self.get_query_params().get('StackGroupName')

	def set_StackGroupName(self,StackGroupName):
		self.add_query_param('StackGroupName',StackGroupName)

	def get_Parameterss(self):
		return self.get_query_params().get('Parameterss')

	def set_Parameterss(self, Parameterss):
		for depth1 in range(len(Parameterss)):
			if Parameterss[depth1].get('ParameterValue') is not None:
				self.add_query_param('Parameters.' + str(depth1 + 1) + '.ParameterValue', Parameterss[depth1].get('ParameterValue'))
			if Parameterss[depth1].get('ParameterKey') is not None:
				self.add_query_param('Parameters.' + str(depth1 + 1) + '.ParameterKey', Parameterss[depth1].get('ParameterKey'))

	def get_AdministrationRoleName(self):
		return self.get_query_params().get('AdministrationRoleName')

	def set_AdministrationRoleName(self,AdministrationRoleName):
		self.add_query_param('AdministrationRoleName',AdministrationRoleName)