FROM registry.fedoraproject.org/fedora:rawhide

ENV SUMMARY="Grafana is an open source, feature rich metrics dashboard and graph editor" \
    DESCRIPTION="Grafana is an open source, feature rich metrics dashboard and graph editor for Graphite, Elasticsearch, OpenTSDB, Prometheus, InfluxDB and Performance Co-Pilot."

LABEL name="${FGC}/grafana" \
      summary="${SUMMARY}" \
      description="${DESCRIPTION}" \
      usage="podman run -d -p 3000:3000 -v grafana-data:/var/lib/grafana --name grafana ${FGC}/grafana" \
      maintainer="PCP Team <pcp-team@redhat.com>" \
      version="0" \
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
