FROM registry.fedoraproject.org/fedora:latest

ENV SUMMARY="Performance Co-Pilot" \
    DESCRIPTION="Performance Co-Pilot is a system performance analysis toolkit."

ENV VERSION=0 \
    ARCH=x86_64

LABEL name="${FGC}/pcp" \
      summary="${SUMMARY}" \
      description="${DESCRIPTION}" \
      version="$VERSION" \
      architecture="$ARCH" \
      usage="podman run -d --systemd always -p 44322:44322 -v pcp-archives:/var/log/pcp/pmlogger --name pcp ${FGC}/pcp" \
      maintainer="PCP Team <pcp@groups.io>" \
      help="cat /README.md" \
      url="https://src.fedoraproject.org/container/pcp" \
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
