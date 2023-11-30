
{{- define "api.labels" }}
{{- include "common.labels" . }}
app.kubernetes.io/component: api
{{- end }}

{{- define "api.selectorLabels" }}
{{- include "common.selectorLabels" . }}
app.kubernetes.io/component: api
{{- end }}


{{- define "api.tmpfsVolumeName" -}}
tmpfs
{{- end -}}


{{- define "api.serviceName" -}}
{{- include "app.fullname" . }}
{{- end -}}

{{- define "api.portName" -}}
http
{{- end -}}

