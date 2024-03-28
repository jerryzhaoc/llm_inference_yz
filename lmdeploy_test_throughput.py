"""(lmdeploy) Benchmarking script to test the throughput of openai service."""
import argparse
import json

import requests
import threading
import time

prompt = []
prompt.append("请以中国春节为题，用英文写一篇不少于500字的文章")
prompt.append("请以哈尔滨冰雕为题，用英文写一篇不少于500字的文章")
prompt.append("请以北京故宫为题，用英文写一篇不少于500字的文章")
prompt.append("请以苏州园林为题，用英文写一篇不少于500字的文章")
prompt.append("请以秋天为题，用英文写一篇不少于500字的文章")
prompt.append("请以梅花为题，用英文写一篇不少于500字的文章")
prompt.append("请以上海外滩为题，用英文写一篇不少于500字的文章")
prompt.append("请以迪斯尼乐园为题，用英文写一篇不少于500字的文章")

def main():

    headers = {"User-Agent": "openai client", "Content-Type": "application/json"}
    ploads = []
    for i in range(args.n_thread):
        j = i % args.n_thread
        request_para = {
            "model": args.model_name,
            "messages": [{"role": "user", "content": prompt[j]}],
            "temperature": 0.7,
            "top_p": 1,
            "n": 1,
            "max_tokens": 1024,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "repetition_penalty": 1,
            "session_id": -1,
            "top_k": 40
        }
        ploads.append(request_para)
    thread_api_addr = args.api_address

    def send_request(results, i):
        print(f"thread {i} goes to {thread_api_addr}")
        response = requests.post(
            thread_api_addr + "/v1/chat/completions",
            headers=headers,
            json=ploads[i],
            stream=False,
        )
        print(response.text)
        response_new_words = json.loads(response.text)["usage"]["completion_tokens"]
        #error_code = json.loads(response.text)["error_code"]
        print(f"=== Thread {i} ===, words: {response_new_words} ")
        results[i] = response_new_words

    # use N threads to prompt the backend
    tik = time.time()
    threads = []
    results = [None] * args.n_thread
    for i in range(args.n_thread):
        t = threading.Thread(target=send_request, args=(results, i))
        t.start()
        # time.sleep(0.5)
        threads.append(t)

    for t in threads:
        t.join()

    print(f"Time (POST): {time.time() - tik} s")
    n_words = sum(results)
    time_seconds = time.time() - tik
    print(
        f"Time (Completion): {time_seconds}, n threads: {args.n_thread}, "
        f"throughput: {n_words / time_seconds} words/s."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--api-address", type=str, default="http://127.0.0.1:23333")
    parser.add_argument("--model-name", type=str, default="llama2")
    parser.add_argument("--n-thread", type=int, default=8)
    args = parser.parse_args()

    main()
