NAME     = docker-clean-images
VERSION  = $(shell git describe --always --dirty)
DISTNAME = $(NAME)-$(VERSION)

sdist:
	rm -rf dist
	mkdir -p dist/$(DISTNAME)
	cp -p README.rst src/* dist/$(DISTNAME)
	tar -C dist -c -f dist/$(DISTNAME).tar.gz -z $(DISTNAME)
	rm -rf dist/$(DISTNAME)

distclean:
	rm -rf dist
