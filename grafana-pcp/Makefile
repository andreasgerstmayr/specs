SPEC=grafana-pcp.spec

rpms:
	$(eval VER := $(shell cat grafana-pcp.spec | grep Version | awk '{print $$2}'))
	./create_dependency_bundle.sh $(VER) ~/rpmbuild/SOURCES/grafana-pcp-deps-$(VER).tar.xz
	cp -f create_dependency_bundle.sh ~/rpmbuild/SOURCES
	./check_bundled_pkgs.py $(SPEC) ~/rpmbuild/SOURCES/grafana-pcp-deps-$(VER).tar.xz
	spectool -g -R $(SPEC)
	rpmbuild -ba $(SPEC)

lint:
	rpmlint ~/rpmbuild/RPMS/*/* ~/rpmbuild/SRPMS/*

clean-rpmbuild:
	rm -rf ~/rpmbuild
	mkdir -p ~/rpmbuild/SOURCES
