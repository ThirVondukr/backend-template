{{- define "common.labels" }}
helm.sh/chart: {{ include "application.chart" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{ include "common.selectorLabels" . }}
{{- end }}

{{- define "common.selectorLabels" }}
app.kubernetes.io/name: {{ include "application.name" . }}
app.kubernetes.io/part-of: {{ .Release.Name }}
{{- end }}



{{- define "migrations.labels" }}
{{ include "common.labels" . }}
app.kubernetes.io/component: migrations
{{- end }}

{{- define "migrations.selectorLabels" }}
{{- include "common.selectorLabels" . }}
app.kubernetes.io/component: migrations
{{- end }}


{{- define "cronjob.labels" }}
{{ include "common.labels" . }}
app.kubernetes.io/component: cronjob
{{- end }}

{{- define "cronjob.selectorLabels" }}
{{- include "common.selectorLabels" . }}
app.kubernetes.io/component: cronjob
{{- end }}
