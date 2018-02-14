import connexion
import six

from swagger_server.models.vm import VM  # noqa: E501
from swagger_server import util


def vms_get():  # noqa: E501
    """vms_get

    Returns a list of VMs # noqa: E501


    :rtype: List[VM]
    """
    return 'do some magic!'


def vms_id_get():  # noqa: E501
    """vms_id_get

    Returns information on a VM instance # noqa: E501


    :rtype: VM
    """
    return 'do some magic!'
