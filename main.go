package main

import (
	"fmt"
	"net/http"

	"github.com/LazarIgnjatovic/brm/api"
)

func main() {
	srv := api.NewServer()

	err := http.ListenAndServe(":8080", srv)
	if err != nil {
		fmt.Println(err)
	}
}
