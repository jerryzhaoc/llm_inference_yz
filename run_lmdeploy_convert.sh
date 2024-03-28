lmdeploy convert llama2 /root/autodl-tmp/lmdeploy-llama2-70B-Chat-4bit \
--model-format awq \
--group-size 128 \
--tp 2
