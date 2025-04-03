
import torch
print(torch.__version__)
print("CUDA Available:", torch.cuda.is_available())


from transformers import pipeline
pipe = pipeline("automatic-speech-recognition", model="mesolitica/malaysian-whisper-large-v2")
