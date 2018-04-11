import connexion
import six

import googleapiclient.discovery
import json

from swagger_server.models.vm import VM  # noqa: E501
from swagger_server import util

# GCP_PROJECT and GCP_ZONE get added by the makefile

def vms_get():  # noqa: E501
    """vms_get

    Returns a list of VMs # noqa: E501


    :rtype: List[VM]
    """
    vms = []
    compute = googleapiclient.discovery.build('compute', 'v1')
    results = compute.instances().list(project=GCP_PROJECT,
                                       zone=GCP_ZONE).execute()
    for result in results['items']:
        vm = VM(id=result['id'],
                creation_timestamp=result['creationTimestamp'],
                name=result['name'],
                description=result['description'],
                machine_type=result['machineType'],
                status=result['status'],
                zone=result['zone'],
                can_ip_forward=result['canIpForward'])
        vms.append(vm)
    
    return vms


def vms_id_get(id):  # noqa: E501
    """vms_id_get

    Returns information on a VM instance # noqa: E501

    :param id: ID of VM to fetch
    :type id: str

    :rtype: VM
    """
    vms = vms_get()
    vm = vms['id'==id]
    
    return vm
