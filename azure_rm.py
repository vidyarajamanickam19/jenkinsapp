{
   "azure": [
    "ansibleMaster"
  ],
  "westeurope": [
    "ansibleMaster"
  ],
  "ansibleMasterNSG": [
    "ansibleMaster"
  ],
  "ansiblelab": [
    "ansibleMaster"
  ],
  "_meta": {
    "hostvars": {
      "ansibleMaster": {
        "powerstate": "running",
        "resource_group": "ansiblelab",
        "tags": {},
        "image": {
          "sku": "7.3",
          "publisher": "OpenLogic",
          "version": "latest",
          "offer": "CentOS"
        },
        "public_ip_alloc_method": "Dynamic",
        "os_disk": {
          "operating_system_type": "Linux",
          "name": "osdisk_vD2UtEJhpV"
        },
        "provisioning_state": "Succeeded",
        "public_ip": "52.174.19.210",
        "public_ip_name": "masterPip",
        "private_ip": "192.168.1.4",
        "computer_name": "ansibleMaster",
        ...
      }
    }
  }
}
