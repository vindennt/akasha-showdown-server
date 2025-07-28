package middleware

import (
	"log"
	"net/http"
	"time"
)

// Define a custom response writer type
type responseWriter struct {
	http.ResponseWriter
	statusCode int
}

func (rw *responseWriter) WriteHeader(code int) {
	rw.statusCode = code // Capture the status code
	rw.ResponseWriter.WriteHeader(code)
}

// Logging middleware to log request and response details
func Logging(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		startTime := time.Now()

		// Log the request details
		log.Printf(
			"> r | Method: %s | Path: %s | SourceIP: %s | Protocol: %s",
			r.Method,
			r.URL.Path,
			r.RemoteAddr,
			r.Proto,
		)

		rw := &responseWriter{ResponseWriter: w, statusCode: http.StatusOK}
		next.ServeHTTP(rw, r)

		duration := time.Since(startTime)

		// Log the response details
		log.Printf("< s | Method: %s  | Path: %s | DestIP: %s | Status: %d | Duration: %v",
			r.Method,
			r.URL.Path,
			r.RemoteAddr,
			rw.statusCode,
			duration,
		)
	})
}

// CORS middleware to handle Cross-Origin Resource Sharing
// It allows requests from a specified origin and handles preflight requests.
func CORS(allowedOrigin string) func(http.Handler) http.Handler {
	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			w.Header().Set("Access-Control-Allow-Origin", allowedOrigin)
			w.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
			w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")

			if r.Method == "OPTIONS" {
				w.WriteHeader(http.StatusOK)
				return
			}

			next.ServeHTTP(w, r)
		})
	}
}
