import torch
from diffusers import StableDiffusionXLPipeline, UNet2DConditionModel, EulerDiscreteScheduler
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file


class SDXLGenerator:
    BASE = "stabilityai/stable-diffusion-xl-base-1.0"
    REPO = "ByteDance/SDXL-Lightning"
    CKPT = "sdxl_lightning_4step_unet.safetensors"

    def __init__(self):
        self.device = "cuda"
        self.dtype = torch.float16

        # Loading the model and pipeline
        self.unet = UNet2DConditionModel.from_config(self.BASE,
                                                     subfolder="unet").to(
                                                         self.device,
                                                         self.dtype)
        self.unet.load_state_dict(
            load_file(hf_hub_download(self.REPO, self.CKPT),
                      device=self.device))

        # Loading the pipeline
        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            self.BASE, unet=self.unet, torch_dtype=self.dtype,
            variant="fp16").to(self.device)

        # Setting the scheduler
        self.pipe.scheduler = EulerDiscreteScheduler.from_config(
            self.pipe.scheduler.config, timestep_spacing="trailing")

    def generate_image(self,
                       prompt,
                       output_path,
                       num_steps=4,
                       guidance_scale=0):
        image = self.pipe(prompt,
                          num_inference_steps=num_steps,
                          guidance_scale=guidance_scale).images[0]
        image.save(output_path)
        return output_path
