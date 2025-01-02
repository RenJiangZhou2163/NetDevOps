



```shell
sh start.sh
```




```shell
#!/bin/bash
# Keep install script for docker compose

echo "Creating state directory."
mkdir -p state
test -e state
echo "Changing directory ownership to non-privileged user."
chown -R 999:999 state || echo "Unable to change directory ownership, changing permissions instead." && chmod -R 0777 state
which curl &> /dev/null || echo "curl not installed"
# curl https://raw.githubusercontent.com/keephq/keep/main/docker-compose.yml --output docker-compose.yml
# curl https://raw.githubusercontent.com/keephq/keep/main/docker-compose.common.yml --output docker-compose.common.yml

docker compose up -d
```



docker-compose.yml包含3个服务：

- keep-backend - 作为 API 服务器的 fastapi 服务。

- keep-frontend - 一个作为 Keep UI 界面的 nextjs 应用程序。

- keep-websocket-server - Soketi（推送器兼容的 websocket 服务器）用于实时警报。