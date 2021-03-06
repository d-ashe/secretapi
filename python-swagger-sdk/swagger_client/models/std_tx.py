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


class StdTx(object):
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
        'msg': 'list[Msg]',
        'fee': 'StdTxFee',
        'memo': 'str',
        'signatures': 'list[StdTxSignatures]'
    }

    attribute_map = {
        'msg': 'msg',
        'fee': 'fee',
        'memo': 'memo',
        'signatures': 'signatures'
    }

    def __init__(self, msg=None, fee=None, memo=None, signatures=None):  # noqa: E501
        """StdTx - a model defined in Swagger"""  # noqa: E501

        self._msg = None
        self._fee = None
        self._memo = None
        self._signatures = None
        self.discriminator = None

        if msg is not None:
            self.msg = msg
        if fee is not None:
            self.fee = fee
        if memo is not None:
            self.memo = memo
        if signatures is not None:
            self.signatures = signatures

    @property
    def msg(self):
        """Gets the msg of this StdTx.  # noqa: E501


        :return: The msg of this StdTx.  # noqa: E501
        :rtype: list[Msg]
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this StdTx.


        :param msg: The msg of this StdTx.  # noqa: E501
        :type: list[Msg]
        """

        self._msg = msg

    @property
    def fee(self):
        """Gets the fee of this StdTx.  # noqa: E501


        :return: The fee of this StdTx.  # noqa: E501
        :rtype: StdTxFee
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this StdTx.


        :param fee: The fee of this StdTx.  # noqa: E501
        :type: StdTxFee
        """

        self._fee = fee

    @property
    def memo(self):
        """Gets the memo of this StdTx.  # noqa: E501


        :return: The memo of this StdTx.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this StdTx.


        :param memo: The memo of this StdTx.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def signatures(self):
        """Gets the signatures of this StdTx.  # noqa: E501


        :return: The signatures of this StdTx.  # noqa: E501
        :rtype: list[StdTxSignatures]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this StdTx.


        :param signatures: The signatures of this StdTx.  # noqa: E501
        :type: list[StdTxSignatures]
        """

        self._signatures = signatures

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
        if issubclass(StdTx, dict):
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
        if not isinstance(other, StdTx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
