python -m vllm.entrypoints.openai.api_server \
--model /root/autodl-tmp/TheBloke_Llama-2-70B-Chat-AWQ \
--served-model-name Llama2-70B-Chat-AWQ \
--trust-remote-code \
--max-model-len 4096 -q awq \
-tp 2 \
--gpu-memory-utilization 1 \
--enforce-eager
