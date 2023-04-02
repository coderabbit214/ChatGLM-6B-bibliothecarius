#  ChatGLM-6B-bibliothecarius

> 本项目用于ChatGLM-6B 接入 [bibliothecarius](https://github.com/coderabbit214/bibliothecarius)

## 快速开始

### 下载本项目

```bash
git clone git@github.com:coderabbit214/ChatGLM-6B-bibliothecarius.git
cd ChatGLM-6B-bibliothecarius
```

### [下载模型](https://huggingface.co/THUDM/chatglm-6b)

模型下载后放入`./model`文件夹中

文件列表`ls -l model/`

```bash
total 26850464
-rw-r--r--@ 1 coderabbit  staff         697 Mar 29 09:51 config.json
-rw-r--r--@ 1 coderabbit  staff        3976 Apr  1 22:21 configuration_chatglm.py
-rw-r--r--@ 1 coderabbit  staff     2699926 Mar 15 10:37 ice_text.model
-rw-r--r--@ 1 coderabbit  staff       50244 Apr  1 22:21 modeling_chatglm.py
-rw-r--r--@ 1 coderabbit  staff  1904491802 Mar 15 11:52 pytorch_model-00001-of-00008.bin
-rw-r--r--@ 1 coderabbit  staff  1879731432 Mar 15 10:49 pytorch_model-00002-of-00008.bin
-rw-r--r--@ 1 coderabbit  staff  1980385902 Mar 15 10:50 pytorch_model-00003-of-00008.bin
-rw-r--r--@ 1 coderabbit  staff  1913294120 Mar 15 10:49 pytorch_model-00004-of-00008.bin
-rw-r--r--@ 1 coderabbit  staff  1879722289 Mar 15 10:50 pytorch_model-00005-of-00008.bin
-rw-r--r--@ 1 coderabbit  staff  1879731496 Mar 15 10:50 pytorch_model-00006-of-00008.bin
-rw-r--r--@ 1 coderabbit  staff  1074103621 Mar 15 10:47 pytorch_model-00007-of-00008.bin
-rw-r--r--@ 1 coderabbit  staff  1233126123 Mar 15 10:48 pytorch_model-00008-of-00008.bin
-rw-r--r--@ 1 coderabbit  staff       33416 Mar 29 09:51 pytorch_model.bin.index.json
-rw-r--r--@ 1 coderabbit  staff       14472 Mar 29 09:51 quantization.py
-rw-r--r--@ 1 coderabbit  staff       12522 Mar 29 09:51 tokenization_chatglm.py
-rw-r--r--@ 1 coderabbit  staff         416 Mar 29 09:51 tokenizer_config.json
```

### 使用Docker

```
docker-compose up -d
```

### 进行测试

```bash
curl --location --request POST 'http://127.0.0.1:8000/chat' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input":"hi"
}'
```

## 参考

- https://github.com/THUDM/ChatGLM-6B
