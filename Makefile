
PWD = $(shell pwd)
TAG = lineart
VOLUME = $(PWD):/code
DISABLE_LOGCAPTURE = DISABLE_NOSETEST_LOGCAPTURE=true
BUILD_CMD = sudo docker build -t $(TAG) .
RUN_CMD = sudo docker run
LOGCAPTURE =

ifneq ($(DISABLE_NOSETEST_LOGCAPTURE),)
  LOGCAPTURE = --nologcapture
endif

# External Commands
docker_test:
	$(BUILD_CMD)
	$(RUN_CMD) -v $(VOLUME) -t $(TAG) make test
docker_test_verbose:
	$(BUILD_CMD)
	$(RUN_CMD) -v $(VOLUME) -e $(DISABLE_LOGCAPTURE) -t $(TAG) make test 
docker_test_debug:
	$(BUILD_CMD)
	$(RUN_CMD) -v $(VOLUME) -i -t $(TAG) /bin/bash

# Internal Commands
init:
	python setup.py install
test:
	python setup.py nosetests $(LOGCAPTURE)

