package main

import (
	"net/http"
	"os"
	"strings"
)

func saySecret(w http.ResponseWriter, r *http.Request) {
	message := r.URL.Path
	message = strings.TrimPrefix(message, "/")
	secret := os.Getenv("VAULT_SECRET")
	if len(secret) == 0 {
		secret = "NOT FOUND"
	}
	message = message + secret
	w.Write([]byte(message))
}
func main() {
	http.HandleFunc("/", saySecret)
	if err := http.ListenAndServe(":8080", nil); err != nil {
		panic(err)
	}
}
