from transformers import pipeline
from langchain_core.prompts import PromptTemplate
# from langchain.chains.llm import LLMChain
from langchain_ollama.llms import OllamaLLM
from kokoro import KPipeline
from IPython.display import display,Audio
from misaki import zh
from pypinyin import lazy_pinyin
import soundfile as sf