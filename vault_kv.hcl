job "vault" {
  datacenters = ["dc1"]
  type = "service"
  vault { policies = ["policy-demo"]}
  group "web" {
    count = 1
    restart {
      attempts = 2
      interval = "1m"
      delay = "15s"
      mode = "fail"
    }
    task "vatul-sercret" {
      driver = "docker"
      config {
        image = "i4spserrano/nomadvaultsecret:latest"
        port_map {
          http = 8080
        }
      }
      template {
          data = <<EOH
  				VAULT_SECRET="{{with secret "secret/data/demo"}}{{.Data.data.value}}{{end}}"
     		  EOH
        	destination = "secrets/vaultsecret.env"
        	env         = true
       	}
      resources {
        cpu    = 500 # 500 MHz
        memory = 256 # 256MB
        network {
          mbits = 10
          port "http" { static = 8080 }
        }
      }
     }
  }
}
