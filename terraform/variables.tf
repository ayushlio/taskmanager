variable "namespace" {
  description = "Kubernetes namespace"
  type        = string
  default     = "taskmanager"
}

variable "image_name" {
  description = "Docker image name"
  type        = string
  default     = "yourusername/taskmanager-api"
}

variable "image_tag" {
  description = "Docker image tag"
  type        = string
  default     = "latest"
}

variable "replicas" {
  description = "Number of API replicas"
  type        = number
  default     = 3
}

variable "db_password" {
  description = "PostgreSQL password"
  type        = string
  sensitive   = true
  default     = "taskpass123"
}
