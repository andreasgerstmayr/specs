FROM registry.fedoraproject.org/fedora:rawhide

ENV SUMMARY="Performance Co-Pilot" \
    DESCRIPTION="Performance Co-Pilot is a system performance analysis toolkit."

LABEL name="${FGC}/pcp" \
      summary="${SUMMARY}" \
      description="${DESCRIPTION}" \
      usage="podman run -d --systemd always -p 44322:44322 -v pcp-archives:/var/log/pcp/pmlogger --name pcp ${FGC}/pcp" \
      maintainer="PCP Team <pcp-team@redhat.com>" \
      version="0" \
      com.redhat.component="pcp" \
      io.k8s.display-name="Performance Co-Pilot" \
      io.k8s.description="${DESCRIPTION}" \
      io.openshift.expose-services="44322:pmproxy" \
      io.openshift.tags="pcp,performance,monitoring"

RUN dnf install -y --setopt=tsflags=nodocs gettext pcp && \
    dnf clean all
RUN systemctl enable pmcd pmlogger pmproxy

COPY root /

VOLUME ["/var/log/pcp/pmlogger"]
EXPOSE 44322

ENTRYPOINT ["/usr/libexec/container-setup"]
CMD ["/usr/sbin/init"]
