SPEC=grafana-pcp.spec

.PHONY: rpms
rpms:
	spectool -g -R $(SPEC)
	./make_deps.sh $(SPEC)
	rpmbuild -ba $(SPEC)
