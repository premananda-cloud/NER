from transformers import AutoModel, AutoTokenizer

model_name = "google-bert/bert-base-uncased"

# This downloads and loads the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# This downloads and loads the model weights
model = AutoModel.from_pretrained(model_name)
