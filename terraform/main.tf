provider "google" {
  project = "my-devops-489815"
  region  = "us-central1"
  zone    = "us-central1-a"
}

resource "google_compute_instance" "vm_instance" {
  name         = "notes-app-vm"
  machine_type = "e2-micro"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata_startup_script = <<-EOF
    #!/bin/bash
    apt update
    apt install -y docker.io git
    systemctl start docker
    git clone https://github.com/fenilpatel05/final-project-s26.git /home/app
    cd /home/app
    docker build -t notes-app .
    docker run -d -p 5001:5001 notes-app
  EOF
}
