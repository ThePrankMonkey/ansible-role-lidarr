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
radarr_release_url: https://api.github.com/repos/Lidarr/Lidrr/releases.linux.tar.gz # API link for releases
```

Example Playbook
----------------

```plain
- hosts: radarr
  roles:
  - {name: radarr, become: yes}
```

References
----------

* [Lidarr](https://github.com/Lidarr/Lidarr/)
