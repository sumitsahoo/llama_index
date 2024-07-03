from typing import Dict, Optional

API_CATALOG_MODELS: Dict[str, int] = {
    "01-ai/yi-large": 16384,
    "aisingapore/sea-lion-7b-instruct": 1024,
    "databricks/dbrx-instruct": 2048,
    "google/codegemma-1.1-7b": 1024,
    "google/codegemma-7b": 4096,
    "google/gemma-2b": 4096,
    "google/recurrentgemma-2b": 1024,
    "ibm/granite-34b-code-instruct": 2048,
    "ibm/granite-8b-code-instruct": 4096,
    "mediatek/breeze-7b-instruct": 1024,
    "meta/codellama-70b": 1024,
    "meta/llama3-70b-instruct": 8192,
    "meta/llama3-8b-instruct": 8192,
    "microsoft/phi-3-medium-4k-instruct": 1024,
    "microsoft/phi-3-mini-128k-instruct": 2048,
    "microsoft/phi-3-mini-4k-instruct": 2048,
    "microsoft/phi-3-small-128k-instruct": 2048,
    "microsoft/phi-3-small-8k-instruct": 2048,
    "mistralai/codestral-22b-instruct-v0.1": 32768,
    "mistralai/mistral-7b-instruct-v0.2": 16384,
    "mistralai/mistral-7b-instruct-v0.3": 32768,
    "mistralai/mistral-large": 16384,
    "mistralai/mixtral-8x22b-instruct-v0.1": 65536,
    "mistralai/mixtral-8x7b-instruct-v0.1": 16384,
    "nvidia/llama3-chatqa-1.5-70b": 1024,
    "nvidia/llama3-chatqa-1.5-8b": 1024,
    "nvidia/nemotron-4-340b-instruct": 2048,
    "seallms/seallm-7b-v2.5": 4096,
    "upstage/solar-10.7b-instruct": 4096,
}


def catalog_modelname_to_contextsize(modelname: str) -> Optional[int]:
    return API_CATALOG_MODELS.get(modelname, None)
