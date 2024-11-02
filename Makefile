# Name image docker
IMAGE_NAME = tox-binaryrepr

default: build runtox

# target for building image
build:
	docker build -f Dockerfile -t $(IMAGE_NAME) .

# target for executing image Docker with option
runtox:
	@if [ -z "$(filter py%,$(MAKECMDGOALS))" ]; then \
		docker run $(IMAGE_NAME):latest run; \
	else \
		docker run $(IMAGE_NAME):latest run -e $(filter py%,$(MAKECMDGOALS)); \
	fi

# run pytest locally
runpytest:
	pytest .  --cov --cov-append --cov-report=html -s -rf --html-report=./report --title='REPORT Binary repr' 
	@echo "open result html is report/pytest_html_report.html"
	@echo "open coverage result is htmlcov/index.html"

# run lint
checkstyle:
	flake8 --extend-ignore E501 --statistics --max-line-length=100 binaryrepr.py

clean:
	rm -rf binaryrepr.egg-info
	rm -rf build dist
	rm -rf htmlcov report archive
	rm -f output.json pytest_html_report.html .coverage


# Eviter les erreurs "No rule to make target" pour les paramètres positionnels
py37 py38 py39 py310 py311 py312:
	@:

%:
	@:
