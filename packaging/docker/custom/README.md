




```
docker build \
  -f Dockerfile.grafana \
  --build-arg "GRAFANA_VERSION=11.3.3" \
  --build-arg "GF_INSTALL_PLUGINS=grafana-clock-panel,alexanderzobnin-zabbix-app,camptocamp-prometheus-alertmanager-datasource,grafana-opensearch-datasource,marcusolsson-csv-datasource,volkovlabs-grapi-datasource,marcusolsson-json-datasource,yesoreyeram-infinity-datasource" \
  -t grafana/grafana-custom:11.3.3 .
```