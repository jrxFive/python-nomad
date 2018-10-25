# COMPILATION IMAGE
FROM golang:1.9.2
LABEL version=0.1.9

RUN mkdir /go/src/vaultsecret

WORKDIR /go/src/vaultsecret/

COPY /src/ /go/src/vaultsecret

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o vaultsecret .

# REAL IMAGE
FROM scratch
COPY --from=0 /go/src/vaultsecret/vaultsecret /
ENTRYPOINT ["/vaultsecret"]
