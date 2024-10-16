
{{- define "worker.labels" }}
{{- include "common.labels" . }}
app.kubernetes.io/component: worker
{{- end }}

{{- define "worker.selectorLabels" }}
{{- include "common.selectorLabels" . }}
app.kubernetes.io/component: worker
{{- end }}
