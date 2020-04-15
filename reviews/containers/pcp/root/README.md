# Performance Co-Pilot container

Performance Co-Pilot is a system performance analysis toolkit.

## Usage

```
$ podman run -d \
    --systemd always \
    -p 44322:44322 \
    -v pcp-archives:/var/log/pcp/pmlogger \
    --name pcp \
    registry.fedoraproject.org/pcp
```

**Note:** On SELinux enabled systems, the following boolean needs to be set: `sudo setsebool -P container_manage_cgroup true`

### Enabling host processes, network and container metrics

```
$ sudo podman run -d \
    --privileged \
    --net host \
    --systemd always \
    -v pcp-archives:/var/log/pcp/pmlogger \
    -v /:/host:ro,rslave \
    -e HOST_MOUNT=/host \
    --name pcp \
    registry.fedoraproject.org/pcp
```

## Environment Variables

### `HOST_MOUNT`

Path inside the container to the bind mount of `/` on the host.

### `REDIS_SERVERS`

Redis connection spec(s) - could be any individual cluster host, and all hosts in the cluster will be automatically discovered.
Alternately, use comma-separated hostspecs (non-clustered setup)

## Volumes

### `/var/log/pcp/pmlogger`

Performance Co-Pilot archive files with historical metrics.

## Ports

### `44322/tcp`

The pmproxy daemon listens on this port and exposes a REST API to access metrics.

## Documentation

https://pcp.io
