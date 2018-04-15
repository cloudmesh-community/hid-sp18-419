import connexion
import six
import os
import googleapiclient.discovery
import json

from swagger_server.models.vm import VM  # noqa: E501
from swagger_server import util

creds = os.environ['HOME'] + '/.cloudmesh/configuration_gce_419.json'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = creds

with open(creds) as json_data:
    d = json.load(json_data)
    project = d['project_id']

def vms_get():  # noqa: E501
    """vms_get

    Returns a list of VMs # noqa: E501


    :rtype: List[VM]
    """
    vms = []
    compute = googleapiclient.discovery.build('compute', 'v1')

    zones = compute.zones().list(project=project).execute()
    results=[]
    
    for zone in zones['items']:
        instances = compute.instances().list(project=project, zone=zone['name']).execute()
        if 'items' in instances.keys():
            results = results + instances['items']
    
    for result in results:
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
