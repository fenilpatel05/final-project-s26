build:
	docker build -t notes-app .

run:
	docker run -p 5001:5001 notes-app
