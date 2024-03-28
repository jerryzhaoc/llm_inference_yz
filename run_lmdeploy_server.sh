lmdeploy serve api_server ./workspace \
--server-name 0.0.0.0 \
--server-port 23333 \
--max-batch-size 64 \
--tp 2
