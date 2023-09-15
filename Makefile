init:
	pip3 install -r ftf/requirements.txt
	touch ftf/.env
.PHONY: init

start:
	python3 ftf/manage.py runserver
.PHONY: start

migrate:
	python3 ftf/manage.py makemigrations
	python3 ftf/manage.py migrate
.PHONY: migrate

clean:
	find . | grep -E "(/__pycache__)" | xargs rm -rf
	find . -name "*.pyc" -exec rm -f {} \;
.PHONY: cleanc