FROM registry.fedoraproject.org/fedora:latest

ENV SUMMARY="Grafana is an open source, feature rich metrics dashboard and graph editor" \
    DESCRIPTION="Grafana is an open source, feature rich metrics dashboard and graph editor for Graphite, Elasticsearch, OpenTSDB, Prometheus, InfluxDB and Performance Co-Pilot."

ENV VERSION=0 \
    ARCH=x86_64

LABEL name="${FGC}/grafana" \
      summary="${SUMMARY}" \
      description="${DESCRIPTION}" \
      version="$VERSION" \
      architecture="$ARCH" \
      usage="podman run -d -p 3000:3000 -v grafana-data:/var/lib/grafana --name grafana ${FGC}/grafana" \
      maintainer="PCP Team <pcp@groups.io>" \
      help="cat /README.md" \
      url="https://src.fedoraproject.org/container/grafana" \
      com.redhat.component="grafana" \
      io.k8s.display-name="Grafana" \
      io.k8s.description="${DESCRIPTION}" \
      io.openshift.expose-services="3000:grafana" \
      io.openshift.tags="grafana,monitoring,dashboard"

RUN dnf install -y --setopt=tsflags=nodocs grafana grafana-pcp && \
    dnf clean all

COPY root /

VOLUME ["/var/lib/grafana"]
EXPOSE 3000

USER grafana
WORKDIR /usr/share/grafana
ENTRYPOINT ["/usr/sbin/grafana-server"]
