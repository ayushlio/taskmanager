#output "namespace" {
#  value = kubernetes_namespace.taskmanager.metadata[0].name
#}

output "api_replicas" {
  value = var.replicas
}

output "image" {
  value = "${var.image_name}:${var.image_tag}"
}
