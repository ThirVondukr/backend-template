{{- define "redis.selectorLabels" -}}
{{- include "common.selectorLabels" . }}
app.kubernetes.io/component: redis
{{- end }}


{{- define "redis.labels" -}}
{{- include "common.labels" . }}
app.kubernetes.io/component: redis
{{- end }}
