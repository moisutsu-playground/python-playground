from transformers import T5ForConditionalGeneration, T5Tokenizer


def main():
    model_name = "sonoisa/t5-base-japanese"
    model = T5ForConditionalGeneration.from_pretrained(model_name).eval()
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    tokenizer.do_lower_case = True

    # <extra_id_0>
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
