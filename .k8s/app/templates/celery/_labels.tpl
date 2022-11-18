{{- define "celery-worker.labels" }}
{{ include "common.labels" . }}
app.kubernetes.io/component: celery-worker
{{- end }}

{{- define "celery-worker.selectorLabels" }}
{{ include "common.selectorLabels" . }}
app.kubernetes.io/component: celery-worker
{{- end }}


{{- define "celery-beat.labels" }}
{{ include "common.labels" . }}
app.kubernetes.io/component: celery-beat
{{- end }}

{{- define "celery-beat.selectorLabels" }}
{{ include "common.selectorLabels" . }}
app.kubernetes.io/component: celery-beat
{{- end }}

{{- define "celery.redisConfigMapName" -}}
{{ include "app.fullname" .}}-celery-redis
{{- end -}}
