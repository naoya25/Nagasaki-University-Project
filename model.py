from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

pipe = pipe.to("mps")

pipe.enable_attention_slicing()

prompt = "a photo of an astronaut riding a horse on mars"

# modelのウォームアップ。Macの場合は必要
_ = pipe(prompt, num_inference_steps=1)

image = pipe(prompt).images[0]
image.save('image.png')
