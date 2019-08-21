SPEC=grafana-pcp.spec

.PHONY: rpms
rpms:
	./check_bundled_pkgs.py $(SPEC)
	spectool -g -R $(SPEC)
	./make_deps.sh $(SPEC)
	rpmbuild -ba $(SPEC)
