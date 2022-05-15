from lib2to3.pgen2 import token

from transformers import GPT2LMHeadModel, T5Tokenizer


def main():
    model_name = "rinna/japanese-gpt2-xsmall"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    tokenizer.do_lower_case = True

    while True:
        prompt = input("Prompt: ")
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(
            input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2
        )
        generated_text = tokenizer.batch_decode(output, skip_special_tokens=True)
        print(generated_text)


if __name__ == "__main__":
    main()
