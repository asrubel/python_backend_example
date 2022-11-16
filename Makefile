up:
	sudo docker-compose --env-file ./.env.list up

show:
	sudo docker ps
show_all:
	sudo docker ps -a

clean:
	sudo docker-compose --env-file ./.env.list down
	sudo docker image prune -a
	sudo docker volume prune
