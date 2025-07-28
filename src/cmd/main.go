package main

import (
	"fmt"
	"log"
	"net/http"
	"github.com/vindennt/akasha-showdown-server/src/config"
	"github.com/vindennt/akasha-showdown-server/src/middleware"

	// Routes
	"github.com/vindennt/akasha-showdown-server/services"
)


func main() {
	// Load configuration
	cfg, cfgErr := config.LoadConfig()
	if cfgErr != nil {
		log.Fatalf("Could not load config: %v", cfgErr)
	}

	// Init server
	port := fmt.Sprintf(":%s", cfg.Port)
	mux := http.NewServeMux()

	// Register routes
	api.RegisterRoutes(mux, cfg)

	// Apply CORS middleware
	handler := middleware.CORS(cfg.AllowedOrigin)(mux)

	// Start the server
	fmt.Printf("Server running on port %s\n", port)
	err := http.ListenAndServe(port, handler)
	if err != nil {
		log.Fatalf("Could not start server: %v", err)
	}
}