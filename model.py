import torch
from diffusers import StableDiffusionPipeline

def create_image(prompt):
    try:
        # pipe = StableDiffusionPipeline.from_pretrained('runwayml/stable-diffusion-v1-5').to('mps')
        # pipe.enable_attention_slicing()

        # # modelのウォームアップ。Macの場合は必要
        # _ = pipe(prompt, num_inference_steps=1)

        # image = pipe(prompt).images[0]
        # image.save('./static/images/image.png')


        model_id = 'runwayml/stable-diffusion-v1-5'
        device = 'cuda'

        pipe = StableDiffusionPipeline.from_pretrained(model_id, revision='fp16', torch_dtype=torch.float16)
        pipe = pipe.to(device)

        generator = torch.Generator(device).manual_seed(42)
        with torch.autocast('cuda'):
            image = pipe(prompt, guidance_scale=7.5, generator=generator).images[0]
        image.save('./static/images/image.png')
        return True
    except:
        return False

if __name__ == '__main__':
    result = create_image('cat')
    if result:
        print('Image created successfully.')
    else:
        print('Image creation failed.')
