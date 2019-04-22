import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_lidarr_service(host):
    host.service('lidarr').is_running


def test_lidarr_page(host):
    cmd = host.run("curl 127.0.0.1:8686")
    cmd.rc == 0
    "Lidarr" in cmd.stdout
