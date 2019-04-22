lidarr
=========

Installs Lidarr.

Requirements
------------

* CentOS
* Internet Connected

Role Variables
--------------

```bash
lidarr_release_url: https://api.github.com/repos/Lidarr/Lidarr/releases.linux.tar.gz # API link for releases
```

Example Playbook
----------------

```plain
- hosts: lidarr
  roles:
  - {name: lidarr, become: yes}
```

References
----------

* [Lidarr](https://github.com/Lidarr/Lidarr/)
