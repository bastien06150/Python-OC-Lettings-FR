.PHONY: build run stop restart logs enter migrate loaddata

build:
	docker build -t oc-lettings .

run:
	docker rm -f oc-container || true
	docker run --env-file .env -p 8000:8000 --name oc-container -d oc-lettings
	docker exec oc-container python manage.py loaddata demo_data.json

stop:
	docker rm -f oc-container || true

restart: 
	stop run

logs:
	docker logs -f oc-container

enter:
	docker exec -it oc-container sh

migrate:
	docker exec oc-container python manage.py migrate

