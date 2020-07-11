NAME     = docker-clean-images
VERSION  = $(shell git describe --always --dirty)
DISTNAME = $(NAME)-$(VERSION)

sdist:
	rm -rf dist
	mkdir -p dist/$(DISTNAME)
	cp -p README.rst LICENSE src/* dist/$(DISTNAME)
	tar -C dist -c -f dist/$(DISTNAME).tar.gz -z $(DISTNAME)
	rm -rf dist/$(DISTNAME)
	sed -e 's/@VERSION@/$(VERSION)/' < $(NAME).spec > dist/$(NAME).spec

distclean:
	rm -rf dist


.PHONY: sdist distclean
