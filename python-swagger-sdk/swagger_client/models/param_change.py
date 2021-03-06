# coding: utf-8

"""
    API for Secret Network by ChainofSecrets.org

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ParamChange(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'subspace': 'str',
        'key': 'str',
        'subkey': 'str',
        'value': 'object'
    }

    attribute_map = {
        'subspace': 'subspace',
        'key': 'key',
        'subkey': 'subkey',
        'value': 'value'
    }

    def __init__(self, subspace=None, key=None, subkey=None, value=None):  # noqa: E501
        """ParamChange - a model defined in Swagger"""  # noqa: E501

        self._subspace = None
        self._key = None
        self._subkey = None
        self._value = None
        self.discriminator = None

        if subspace is not None:
            self.subspace = subspace
        if key is not None:
            self.key = key
        if subkey is not None:
            self.subkey = subkey
        if value is not None:
            self.value = value

    @property
    def subspace(self):
        """Gets the subspace of this ParamChange.  # noqa: E501


        :return: The subspace of this ParamChange.  # noqa: E501
        :rtype: str
        """
        return self._subspace

    @subspace.setter
    def subspace(self, subspace):
        """Sets the subspace of this ParamChange.


        :param subspace: The subspace of this ParamChange.  # noqa: E501
        :type: str
        """

        self._subspace = subspace

    @property
    def key(self):
        """Gets the key of this ParamChange.  # noqa: E501


        :return: The key of this ParamChange.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ParamChange.


        :param key: The key of this ParamChange.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def subkey(self):
        """Gets the subkey of this ParamChange.  # noqa: E501


        :return: The subkey of this ParamChange.  # noqa: E501
        :rtype: str
        """
        return self._subkey

    @subkey.setter
    def subkey(self, subkey):
        """Sets the subkey of this ParamChange.


        :param subkey: The subkey of this ParamChange.  # noqa: E501
        :type: str
        """

        self._subkey = subkey

    @property
    def value(self):
        """Gets the value of this ParamChange.  # noqa: E501


        :return: The value of this ParamChange.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ParamChange.


        :param value: The value of this ParamChange.  # noqa: E501
        :type: object
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ParamChange, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ParamChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
