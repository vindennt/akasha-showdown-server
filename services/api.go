package api

import (
	"fmt"
	"net/http"

	"github.com/vindennt/akasha-showdown-server/src/config"
)

func RegisterRoutes(mux *http.ServeMux, cfg *config.Config) {
	// Add handlers here
	mux.HandleFunc("GET /ping", pingHandler)

	// mux.HandleFunc("/user/create", user.CreateHandler)
}

func pingHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "pong")
}

