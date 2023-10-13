from diffusers import StableDiffusionPipeline

def create_image(prompt):
    try:
        pipe = StableDiffusionPipeline.from_pretrained('runwayml/stable-diffusion-v1-5').to('mps')
        pipe.enable_attention_slicing()

        # modelのウォームアップ。Macの場合は必要
        _ = pipe(prompt, num_inference_steps=1)

        image = pipe(prompt).images[0]
        image.save('./static/image.png')
        return True
    except:
        return False


if __name__ == '__main__':
    create_image('cat')
