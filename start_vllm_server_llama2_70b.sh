python -m vllm.entrypoints.openai.api_server \
--model /disk1/jerry.zhao/models/Llama2-70B-chat-AWQ \
--served-model-name Llama2-70B-chat-AWQ \
--trust-remote-code \
--max-model-len 2048 -q awq \
-tp 2 \
--gpu-memory-utilization 1 \
--enforce-eager
