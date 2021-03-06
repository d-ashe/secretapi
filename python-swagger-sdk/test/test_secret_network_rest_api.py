# coding: utf-8

"""
    API for Secret Network by ChainofSecrets.org

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.secret_network_rest_api import SecretNetworkRESTApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSecretNetworkRESTApi(unittest.TestCase):
    """SecretNetworkRESTApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.secret_network_rest_api.SecretNetworkRESTApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_node_info_get(self):
        """Test case for node_info_get

        The properties of the connected node  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
