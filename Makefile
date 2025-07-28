.PHONY: run

run:
# 	go run src/cmd/main.go
	docker build -t akasha-showdown-server .
	docker run -p 8181:8181 akasha-showdown-server
