# Grafana container

Grafana is an open source, feature rich metrics dashboard and graph editor for Graphite, Elasticsearch, OpenTSDB, Prometheus, InfluxDB and Performance Co-Pilot.

## Usage

```
$ podman run -d -p 3000:3000 -v grafana-data:/var/lib/grafana --name grafana registry.fedoraproject.org/grafana
```

## Volumes

### `/var/lib/grafana`

Grafana data directory.
Contains the default SQLite database with the configured dashboards and settings, and installed 3rd party plugins.

## Ports

### `3000/tcp`

The integrated web server listens on this port and serves the Grafana web application.

## Documentation

https://grafana.com/docs/grafana/
